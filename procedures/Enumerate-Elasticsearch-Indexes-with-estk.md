---
tags:
  - elasticsearch
  - discovery
  - index-enumeration
type: procedure
tools:
  - '[[tools/estk]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/estk-list-indexes]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-30T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.288Z'
sub_techniques: []
id: b60e1233-afcc-4b71-9a5e-48a371ab73d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate-Elasticsearch-Indexes-with-estk

## Summary

This procedure uses the estk tool to list all available indexes in an unauthenticated Elasticsearch instance, revealing document counts and sizes to identify valuable data targets.

## Description

Once initial access is confirmed, attackers enumerate indexes to map the data landscape. Targeting Elasticsearch 2.7.0 on port 9200, this leverages the lack of auth to query index metadata. Prerequisites include tool installation and URL knowledge. Outcomes: Visibility into data volume (e.g., 2212 documents, 5.9 MB), enabling prioritization of sensitive indexes like 'aim_high' for exfiltration.

## Requirements

1. estk tool installed (Go-based, via `go install`)
2. Network access to https://elasticsearch.example.com:9200
3. Basic command-line familiarity

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) in Elasticsearch
- Log and alert on _cat/indices API calls
- Use network segmentation to limit exposure

## Objectives

1. List all indexes and metadata
2. Assess data quantities for impact evaluation
3. Identify high-value targets like user or log indexes

## Instructions

### Step 1: Run Index List Command

**Context**: Query the Elasticsearch _cat/indices endpoint via estk to retrieve index details without auth.

**Command** ([[commands/estk-list-indexes]]):
```bash
estk --url=https://elasticsearch.example.com:9200 list
```

> This detects the version (2.7.0), lists indices (e.g., 3 total, aim_high with 2211 docs), and shows sizes, confirming unrestricted discovery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/estk-list-indexes]]

## Tools Used

- [[tools/estk]]

## Tags

- [[elasticsearch]]
- [[Discovery]]
