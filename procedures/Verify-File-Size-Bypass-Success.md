---
id: proc-uuid-4
tags:
  - verification
  - bypass
  - s3
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-download-from-s3]]'
verified: false
platforms:
  - Cloud (AWS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T05:32:10.038Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Verify-File-Size-Bypass-Success

## Summary

Confirm the bypass by checking the uploaded file's size and accessibility in S3, ensuring it exceeds app limits without errors.

## Description

Post-upload, verify via direct S3 access or app integration. Without additional policies, the file persists, proving the bypass. Use for proof-of-concept in reports.

## Requirements

1. S3 object key from presigned URL
2. Read access to bucket (public or signed GET)
3. Rails app access for integrity check

## Defense

Defensive measures and detection strategies:

- Post-upload size checks in Rails
- S3 lifecycle policies for auto-deletion
- Audit logs for size discrepancies

## Objectives

1. Download and measure file size
2. Check app behavior on access
3. Document impact (e.g., costs)

## Instructions

### Step 1: Attempt Download from S3

**Context**: Use GET to fetch and inspect the file.

Execute [[commands/curl-download-from-s3]] (assuming public or signed):

```bash
curl -o downloaded.txt "https://bucket.s3.amazonaws.com/key"
ls -lh downloaded.txt
```

> Expected: File size matches large upload (e.g., 100M), no errors.

### Step 2: Check Rails App Integration

**Context**: See if app recognizes the blob without size rejection.

Access via app URL or download method; expect success despite mismatch.

> Rails download(key) should not raise FileNotFoundError for valid key.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/curl-download-from-s3]]

## Tools Used

- [[tools/curl]]

## Tags

- verification
- bypass
