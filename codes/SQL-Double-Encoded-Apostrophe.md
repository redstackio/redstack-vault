---
id: c2937d8e-cb4b-4f81-a0a2-59d04ebee734
name: SQL-Double-Encoded-Apostrophe
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:36.110340+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sqli
  - encoding
  - bypass
validated: true
---

# SQL-Double-Encoded-Apostrophe

## Code

```sql
%%2727
%25%27
```

## Description

This snippet demonstrates double-encoded apostrophes, where %27 (') is further encoded as %25%27. It bypasses filters that perform single-level URL decoding before SQL processing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static payloads for injection | %%2727 |

## Usage

Inject into parameters like ?id=%%2727 to test if the app decodes twice, allowing the apostrophe to reach the SQL query and cause a syntax break.

## Detection

- Logs of multi-encoded inputs.
- Anomalous query parsing errors after decoding.
- IDS signatures for nested percent encodings.

## Related

- [[procedures/SQL-Injection-Entry-Point-Detection]]
