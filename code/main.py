#!/usr/bin/env python3
"""
Entry point for the HackerRank Orchestrate Support Triage Agent.

Usage:
  python main.py --input ../support_tickets/support_tickets.csv \\
                 --output ../support_tickets/output.csv

See agent.py for full implementation details.
"""
from agent import main

if __name__ == "__main__":
    main()
