---
tags:
  - token
  - gcp
  - api-access
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-bigquery-projects]]'
platforms:
  - GCP
techniques:
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 914d364d-37da-4aab-89a0-126ade0dbb08
created_at: '2025-12-13T09:00:27.779Z'
updated_at: '2025-12-13T09:00:27.779Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Access GCP Services with Fetched Token

## Summary

This procedure uses a stolen service account token to authenticate and access GCP APIs, potentially exposing data in services like BigQuery and Cloud Storage.

## Description

With the token obtained via XXE/SSRF, an attacker can make authenticated requests to GCP endpoints, listing projects and accessing resources in the development environment.

## Requirements

1. Valid service account token
2. curl or similar HTTP client
3. Knowledge of GCP API endpoints

## Defense

Defensive measures and detection strategies:

- Restrict service account permissions
- Monitor API access logs for anomalies

## Objectives

1. Query GCP projects and services
2. Confirm unauthorized access
3. Potential data exfiltration

## Instructions

### Step 1: Query BigQuery Projects

**Context**: Use token to access BigQuery API.

**Command** ([[commands/curl-bigquery-projects]]):
```bash
TOKEN="████████"
curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
```

> Returns JSON list of projects.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/curl-bigquery-projects]]

## Tools Used

- [[tools/curl]]

## Tags

- [[token]]
- [[gcp]]
- [[api-access]]
