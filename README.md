# Multi-Domain Support Triage Agent

HackerRank Orchestrate submission — May 2026.

Handles support tickets for **HackerRank**, **Claude (Anthropic)**, and **Visa** using RAG over the provided support corpus.

---

## Quick start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your LLM key (at least one)
cp ../.env.example ../.env
# Edit .env and fill in ANTHROPIC_API_KEY or GROQ_API_KEY

# 3. Run the agent
python agent.py \
  --input ../support_tickets/support_tickets.csv \
  --output ../support_tickets/output.csv
```

Output is written to `support_tickets/output.csv` with columns:
`issue, subject, company, status, product_area, response, justification, request_type`

---

## Architecture

```
support_tickets.csv
       │
       ▼
┌─────────────────────────────────────────────────────┐
│  Safety pre-check (injection detection)             │
└──────────────────────┬──────────────────────────────┘
                       │
       ┌───────────────▼──────────────────┐
       │  Domain inference                │
       │  (company field → keyword score) │
       └───────────────┬──────────────────┘
                       │
       ┌───────────────▼──────────────────┐
       │  Rule-based escalation pre-check │
       │  (fraud / security / outage etc) │
       └───────────────┬──────────────────┘
                       │
       ┌───────────────▼──────────────────┐
       │  Hybrid Retrieval                │
       │  BM25 + TF-IDF → RRF fusion      │
       │  + domain boost (×1.8)           │
       └───────────────┬──────────────────┘
                       │
       ┌───────────────▼──────────────────┐
       │  LLM Triage (temp=0)             │
       │  Anthropic → Groq → rule-based   │
       └───────────────┬──────────────────┘
                       │
       ┌───────────────▼──────────────────┐
       │  Grounding check                 │
       │  Bigram overlap ≥ 0.20?          │
       │  No → discard LLM, use rule-based│
       └───────────────┬──────────────────┘
                       │
       ┌───────────────▼──────────────────┐
       │  Safety override                 │
       │  Force escalate: fraud /         │
       │  account_security / emergency    │
       └───────────────┬──────────────────┘
                       │
               output.csv row
```

---

## Key design decisions

### Retrieval: BM25 + TF-IDF (no dense embeddings)

**Why not sentence-transformers?**
- No model download required → fully reproducible, offline-friendly
- Deterministic output (no embedding randomness or version drift)
- Fast on CPU for hundreds of tickets

**Trade-off:** Misses semantic paraphrases (e.g. "can't log in" ≠ "authentication failure"). Mitigated by the grounding check — if retrieval is poor and the LLM hallucinates to compensate, the grounding check catches it and falls back to rule-based escalation.

**Reciprocal Rank Fusion (RRF):** Combines BM25 and TF-IDF rankings without needing to normalise scores across the two systems. K=60 is standard in the literature.

**Domain boost (×1.8):** Retrieved chunks from the inferred product domain are up-weighted. This prevents cross-domain confusion (e.g. a Visa fraud ticket retrieving HackerRank docs).

### Hallucination prevention: grounding check

The single biggest risk with LLM-based triage is **hallucinated policies** — the model "filling in" steps that aren't in the corpus. We prevent this two ways:

1. **System prompt (temp=0):** Instructs the model to extract facts verbatim from retrieved docs, and to escalate if the docs don't cover the issue.
2. **Post-hoc bigram overlap check:** After the LLM responds, we compute what fraction of the response's bigrams appear in the retrieved context. If < 20%, we discard the LLM response and use the rule-based fallback instead.

This means we sometimes escalate a ticket that could have been answered — but that's the safer failure mode for the evaluation criteria ("no hallucinated policies").

### Escalation logic

Two layers:
- **Pre-LLM rule-based check:** Keyword matching on the ticket content flags high-risk categories (billing_fraud, account_security, legal_compliance, critical_outage, physical_emergency).
- **Post-LLM safety override:** Even if the LLM says "replied", we force escalation for billing_fraud / account_security / physical_emergency. The LLM decides the product area and justification; the rule ensures we don't accidentally reply to a fraud case.

### LLM fallback chain

```
ANTHROPIC_API_KEY set? → claude-3-5-haiku-20241022 (temp=0, deterministic)
        │ not available or fails
        ▼
GROQ_API_KEY set? → llama-3.1-8b-instant (temp=0, JSON mode)
        │ not available or fails
        ▼
Rule-based triage (deterministic, corpus-grounded, no LLM needed)
```

The rule-based triage is a genuine fallback, not a stub — it builds answers directly from retrieved corpus text, so it's always grounded.

---

## Environment variables

| Variable            | Required | Description                        |
|---------------------|----------|------------------------------------|
| `ANTHROPIC_API_KEY` | Recommended | Primary LLM (best quality)      |
| `GROQ_API_KEY`      | Optional | Fallback LLM (free tier)           |

Never hardcode keys. Copy `.env.example` to `.env` and fill it in.

---

## Corpus structure

The agent reads `.md` files from:
```
data/
  hackerrank/   ← HackerRank support docs
  claude/       ← Claude / Anthropic support docs
  visa/         ← Visa support docs
```

Each file is chunked at paragraph boundaries (blank lines). Chunks of 60–1500 characters are indexed. Shorter fragments are too noisy; longer chunks dilute relevance scores.

If a domain directory is empty or missing, the agent falls back to `static_corpus.py` (if present).

---

## Failure modes (known limitations)

| Failure mode | What happens |
|---|---|
| Retrieval mismatch (ticket terms ≠ corpus terms) | Grounding check fails → escalate |
| LLM hallucinates a policy | Grounding check (bigram overlap) catches it → rule-based fallback |
| Ticket is cross-domain | Domain inference keyword scores; ties resolved by "General" |
| All LLMs unavailable | Rule-based triage used throughout; still grounded in corpus |
| Corpus is empty | Agent exits with error (no safe fallback) |

---

## Dependencies

See `requirements.txt`. Key packages:
- `rank-bm25` — BM25 retrieval
- `scikit-learn` — TF-IDF vectoriser
- `anthropic` / `groq` — LLM clients
- `rich` — terminal UI
- `pandas` — CSV I/O