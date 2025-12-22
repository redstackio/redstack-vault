---
id: b7a04a36-0278-472d-89a9-b4f9d3a5833e
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.208314+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - mysql-comment
  - sqli
  - injection
platforms:
  - Database
validated: true
---

# MySQL-Comment-Syntax-Examples

## Code

```sql
# MYSQL Comment
-- comment [Note the space after the double dash]
/* MYSQL Comment */
/*! MYSQL Special SQL */
/*!32302 10*/ Comment for MYSQL version 3.23.02
```

## Description

This code snippet demonstrates the three primary MySQL comment syntaxes used in SQL injection attacks to obfuscate payloads and bypass filters. Single-line comments (--) terminate queries early, multi-line (/* */) encapsulate blocked code, and version-specific (/*! */) provide conditional execution based on MySQL version, allowing targeted injections without affecting incompatible systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is static syntax; substitute comment content with malicious SQL (e.g., 'UNION SELECT') | N/A |

## Usage

Embed these comments in SQL injection payloads submitted to vulnerable web inputs. For example, in a union-based attack: `' UNION SELECT version()--` uses single-line to comment out trailing query parts. Use in red team exercises to test WAF bypass or during pentests to evade input validation. Reference in procedures like [[procedures/MySQL-Comment-Injection]] for crafting obfuscated queries.

## Detection

- Monitor SQL logs for unusual comment patterns near injectable keywords (e.g., UNION inside /* */).
- WAF rules detecting --, /*, or /*! sequences in user inputs.
- Anomaly detection in query execution times or error rates when comments alter query structure.
