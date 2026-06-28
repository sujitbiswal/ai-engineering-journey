# AP Invoice Analyzer

A Python tool that ingests raw accounts-payable invoice data and produces an automated payables summary — status breakdown, total liability, and high-value flagging — replacing manual line-by-line review.

## Overview

Accounts-payable teams routinely receive invoice data as flat files and review it by hand to answer three questions: *what do we owe, what's the status of each invoice, and which ones are large enough to need sign-off?* This tool automates that triage. It reads a raw invoice file, converts each row into a structured invoice record, skips malformed data without crashing, and prints a clean payables report.

The logic encodes a real treasury rule: rejected invoices are excluded from the total payable (they are not amounts owed) but retained in the status breakdown for audit visibility.

## What it does

- Reads invoice data from a CSV file
- Parses each row into an `Invoice` object
- Skips malformed rows (e.g. a non-numeric amount) with a logged warning instead of failing
- Calculates total payable, excluding rejected invoices
- Produces a status breakdown (Approved / Pending / Rejected)
- Flags all high-value invoices above a ₹10,000 threshold

## Skills demonstrated

- Object-oriented design — invoice data modelled as a class with its own behaviour
- File handling and parsing of raw delimited text
- Error handling — surviving dirty data with `try`/`except`
- Aggregation logic — totals, grouping, and filtering over a collection
- Domain reasoning — encoding a treasury rule (rejected ≠ payable) into the calculation

## How to run

```bash
python day11_invoice_analyzer.py
```

The tool reads `invoices.csv` from the same folder. Each row is `invoice_id,vendor,amount,status`.

## Sample output

```
==================================================
AP PAYABLES SUMMARY
==================================================
INV-001 | Acme Corp          | ₹   8500 | Approved
INV-002 | Globex             | ₹   3200 | Pending
INV-003 | Initech            | ₹  15000 | Approved
INV-004 | Umbrella           | ₹    920 | Rejected
INV-005 | Stark Industries   | ₹  42000 | Approved
INV-006 | Wayne Enterprises  | ₹   7600 | Pending
INV-008 | Tyrell Corp        | ₹  11200 | Approved
--------------------------------------------------
Total payable: ₹87500
Status breakdown: {'Approved': 4, 'Pending': 2, 'Rejected': 1}

High-value invoices (>₹10,000):
  Initech — ₹15000
  Stark Industries — ₹42000
  Tyrell Corp — ₹11200
```

The malformed row (`INV-007`, with a non-numeric amount) is detected and skipped at load time, so it never reaches the report.

## Built with

Python 3 — standard library only, no external dependencies.
