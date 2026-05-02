# Support Triage Agent — `code/`

A multi-domain support ticket triage agent built for HackerRank Orchestrate (May 2026).

---

## Architecture

```
Ticket (issue, subject, company)
   │
   ├─ 1. Injection detection   → hard-block malicious inputs before any LLM call
   ├─ 2. Domain inference      → HackerRank / Claude / Visa (uses `company` field first)
   ├─ 3. Out-of-scope check    → reply "invalid" for clearly unrelated requests
   ├─ 4. Rule-based escalation → safety net for fraud / security / outage patterns
   ├─ 5. Hybrid retrieval      → BM25 + TF-IDF + RRF over local data/ corpus
   ├─ 6. LLM call              → Anthropic Claude → Groq → rule-based fallback
   ├─ 7. Grounding check       → discard LLM output if bigram overlap < 0.20
   └─ 8. Safety override       → force escalation for high-risk categories
```

**Retrieval**: Hybrid BM25 + TF-IDF with Reciprocal Rank Fusion (RRF) over all `.md` files in `data/`. No network calls for corpus content — fully offline and reproducible.

**LLM**:  Groq (Llama 3.1 8B instant). Full rule-based deterministic fallback if no key is set.

---

## Quick start

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key (never hardcode!)
copy ..\.env.example ..\.env       # Windows
# cp ../.env.example ../.env       # macOS/Linux
# then edit .env and add your GROQ_API_KEY (and/or ANTHROPIC_API_KEY)

# 4. Run on the full ticket set
python main.py --input ../support_tickets/support_tickets.csv \
               --output ../support_tickets/output.csv


```

---

## Output schema

| Column          | Allowed values                                           |
|-----------------|----------------------------------------------------------|
| `status`        | `replied`, `escalated`                                   |
| `product_area`  | support category label (e.g. `assessment_management`)    |
| `response`      | user-facing answer grounded in the local corpus          |
| `justification` | 1–2 sentence internal rationale                          |
| `request_type`  | `product_issue`, `feature_request`, `bug`, `invalid`     |

---

## Files

| File               | Purpose                                  |
|--------------------|------------------------------------------|
| `agent.py`         | All logic: corpus loader, retriever, LLM, pipeline |
| `main.py`          | CLI entry point (calls `agent.main()`)   |
| `static_corpus.py` | Hardcoded fallback corpus (17+10+10 chunks) |
| `requirements.txt` | Python dependencies                      |

---

## Design decisions (for the AI Judge interview)

- **Why BM25 + TF-IDF instead of semantic embeddings?** No model downloads, fully deterministic, fast at startup, and sufficient for keyword-rich support content.
- **Why Groq Llama 3.1 8B instant?** Lowest latency + cost, ideal for structured JSON output triage.
- **Why a strict 20% bigram Grounding Check?** To prevent LLM hallucination. If an LLM response shares < 20% of its bigrams with the retrieved context, we discard it and fallback to safe deterministic rules.
- **Why a rule-based escalation layer?** LLMs can be unpredictable on high-stakes cases (fraud, security). Hard rules ensure we never auto-reply to identity theft or billing fraud tickets.
- **Why read from `data/` instead of scraping?** The problem statement requires using only the provided corpus. Scraping introduces non-determinism, rate limits, and policy violations.
- **Failure modes**: Very long tickets may exceed context; non-English tickets may reduce retrieval quality; tickets with no matching corpus content default to escalation (safe).

---

## Environment variables

| Variable            | Required | Purpose                                      |
|---------------------|----------|----------------------------------------------|
| `GROQ_API_KEY`      | Optional | Primary fallback LLM inference (Llama 3.1)   |
| `ANTHROPIC_API_KEY` | Optional | Highest quality LLM (Claude 3.5 Haiku)       |
