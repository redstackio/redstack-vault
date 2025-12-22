---
tags:
  - historical-data
  - pagination-exploit
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:30:47.133Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 51dc9cc2-f88f-4285-9fed-083037506f0b
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Retrieve-Older-ELMAH-Logs

## Summary

This procedure paginates through ELMAH to access older error logs, expanding the scope of exposed data to historical entries.

## Description

By increasing the page parameter, attackers fetch logs from earlier periods (e.g., December), each containing similar sensitive details. This reveals long-term error patterns and additional PII, increasing the attack surface for reconnaissance and exploitation.

## Requirements

1. Basic log listing successful
2. Knowledge of total log count (~75,000)
3. Pagination support in endpoint

## Defense

Defensive measures and detection strategies:

- Limit log retention and pagination depth
- Block excessive page requests
- Rotate or purge old logs regularly

## Objectives

1. Access historical logs
2. Broaden data exposure
3. Identify persistent vulnerabilities

## Instructions

### Step 1: Paginate to Older Logs

**Context**: Adjust page to retrieve dated entries.

**Command** ([[commands/curl-access-url]]):
```bash
curl https://proze.yelp.com/tmwebapi/elmah.axd?page=100&size=100
```

> Expected output: Logs from early dates like December.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[historical-data]]
- [[pagination-exploit]]
