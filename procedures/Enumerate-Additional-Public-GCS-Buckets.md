---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567895
tags:
  - bucket-enumeration
  - gsutil
  - expansion
type: procedure
tools:
  - '[[tools/gsutil]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/gsutil-list-review-bucket]]'
  - '[[commands/gsutil-list-gitlab-bucket]]'
verified: false
platforms:
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:28.468Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Enumerate-Additional-Public-GCS-Buckets

## Summary

This procedure extends discovery by checking related GCS buckets for public access, identifying further exposures like app review directories in GitLab's infrastructure.

## Description

After initial bucket access, attackers probe similar names like gs://about.gitlab-review.app. Uses gsutil for ls operations. Target: GCP cloud storage. Prerequisites: gsutil ready. Outcomes: Mapping of public assets, e.g., directories with update files.

## Requirements

1. gsutil tool
2. List of potential bucket names (e.g., from domain variations)
3. Internet access

## Defense

Defensive measures and detection strategies:

- Audit all buckets for public ACLs using gsutil iam
- Implement organization-wide policies via Cloud IAM
- Log and alert on ls attempts to non-existent or private buckets

## Objectives

1. Discover additional public buckets
2. Enumerate their contents for more data
3. Differentiate public from private to scope impact

## Instructions

### Step 1: List Related Bucket

**Context**: Target a variant bucket to check exposure.

**Command** ([[commands/gsutil-list-review-bucket]]):
```bash
gsutil ls gs://about.gitlab-review.app
```

> Expected output: Directories like 1006-qa-fix-color-on-links-for-campus-page/, indicating app reviews.

### Step 2: Test Private Bucket

**Context**: Verify boundaries by attempting access to production.

**Command** ([[commands/gsutil-list-gitlab-bucket]]):
```bash
gsutil ls gs://gitlab
```

> Expected output: 403 error confirming restricted access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/gsutil-list-review-bucket]]
- [[commands/gsutil-list-gitlab-bucket]]

## Tools Used

- [[tools/gsutil]]

## Tags

- [[bucket-discovery]]
- [[gcp]]
- [[recon]]
