---
tags:
  - elasticsearch
  - data-exfiltration
  - collection
type: procedure
tools:
  - '[[tools/estk]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/estk-dump-index]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-30T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.285Z'
sub_techniques: []
id: 9b0af1a1-2a1a-48f4-83b9-addf19bab5cf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Data-from-Elasticsearch-Index-with-estk

## Summary

This procedure dumps all documents from a specific Elasticsearch index using estk, enabling unauthorized data exfiltration in the absence of authentication.

## Description

Following index enumeration, attackers target specific stores like 'aim_high' to extract full datasets. This exploits the open Elasticsearch 2.7.0 on port 9200, querying the _search endpoint for all docs. Prerequisites: estk and target URL. Outcomes: Complete JSON export of sensitive data, risking privacy breaches and service impacts if modified.

## Requirements

1. estk tool installed
2. Known index name (e.g., from prior enumeration)
3. Write access to local storage for output files

## Defense

Defensive measures and detection strategies:

- Enable query logging and alert on large _search requests
- Apply index-level permissions
- Regularly audit exposed services with tools like Nuclei

## Objectives

1. Retrieve all documents from targeted index
2. Export data in parsable JSON format
3. Demonstrate full read access for impact assessment

## Instructions

### Step 1: Dump Index Data

**Context**: Use estk's dump function to fetch and output all index contents, verifying exfiltration capability.

**Command** ([[commands/estk-dump-index]]):
```bash
estk dump --url=https://elasticsearch.example.com:9200 --index=aim_high
```

> Outputs JSON documents to stdout; pipe to file (e.g., > data.json) for persistence. Success shows full dataset without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/estk-dump-index]]

## Tools Used

- [[tools/estk]]

## Tags

- [[elasticsearch]]
- [[data-exfiltration]]
