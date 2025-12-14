---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - download
  - exfiltration
  - sensitive-data
type: procedure
tools:
  - '[[tools/gsutil]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/gsutil-list-javascripts-dir]]'
verified: false
platforms:
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1213.003]]'
updated_at: '2025-12-14T17:29:28.475Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Download-Sensitive-Files-from-GCS-Bucket

## Summary

This procedure focuses on retrieving specific sensitive files from the public GCS bucket, such as XML reports and JSON data containing PII and tokens, to achieve data exfiltration.

## Description

Following enumeration, attackers target files like all-releases.xml (HackerOne reports) and db-0881eaf3.json (phones, tokens). The scenario involves public GCS in GCP. Prerequisites: Prior listing via gsutil or browser. Outcomes: Local copies of sensitive data for analysis or further attacks like social engineering.

## Requirements

1. gsutil tool for efficient downloads
2. Knowledge of file paths from enumeration
3. Local storage for exfiltrated files

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive objects and restrict public downloads
- Use VPC Service Controls to limit data egress
- Alert on high-volume object downloads from anomalous sources

## Objectives

1. Download files with undisclosed security details
2. Extract staff PII and tokens for potential abuse
3. Access internal links for chained exploitation

## Instructions

### Step 1: Enumerate Target Directory

**Context**: Refine listing to focus on sensitive areas.

**Command** ([[commands/gsutil-list-javascripts-dir]]):
```bash
gsutil ls gs://about.gitlab.com/javascripts/
```

> Lists JS files and others; use to identify download targets. Expected output: Paths to files like roulette.json.

### Step 2: Download Specific Files

**Context**: Retrieve key files using direct URLs or gsutil cp.

For example: gsutil cp gs://about.gitlab.com/all-releases.xml .

> Or browser download from https://storage.googleapis.com/about.gitlab.com/_nuxt/content/db-0881eaf3.json. Expected output: Files saved, contents parsed for tokens and PII.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used

- [[commands/gsutil-list-javascripts-dir]]

## Tools Used

- [[tools/gsutil]]

## Tags

- [[data-exfiltration]]
- [[gcs-download]]
- [[pii-leak]]
