---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - gsutil
  - enumeration
  - gcs
type: procedure
tools:
  - '[[tools/gsutil]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/gsutil-list-main-bucket]]'
verified: false
platforms:
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:28.478Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# List-GCS-Bucket-Contents-with-gsutil

## Summary

This procedure uses the gsutil command-line tool to enumerate objects in a public GCS bucket, providing a structured list of exposed files and directories for targeted exploitation.

## Description

gsutil is Google's CLI for GCS interactions. In this attack, it's used to list contents of gs://about.gitlab.com/ anonymously. The target environment is GCP with public buckets. Prerequisites: gsutil installed via Google Cloud SDK. Expected outcomes: Full object inventory, revealing sensitive paths like XML files with security reports.

## Requirements

1. gsutil installed (part of Google Cloud SDK)
2. Internet access to the public bucket
3. No authentication configured for public reads

## Defense

Defensive measures and detection strategies:

- Disable public access and use signed URLs for shares
- Monitor gsutil-like API calls via Cloud Logging
- Implement bucket policies denying anonymous ls operations

## Objectives

1. Enumerate all objects in the target bucket
2. Identify directories and files for further access
3. Confirm public exposure without errors

## Instructions

### Step 1: Install gsutil if Needed

**Context**: Ensure the tool is available for enumeration.

Download from https://cloud.google.com/storage/docs/gsutil_install and run setup.

### Step 2: List Root Bucket Contents

**Context**: Perform a top-level scan to discover all objects.

**Command** ([[commands/gsutil-list-main-bucket]]):
```bash
gsutil ls gs://about.gitlab.com/
```

> This command lists objects like gs://about.gitlab.com/all-releases.xml, gs://about.gitlab.com/javascripts/. Expected output: No 403 errors; complete enumeration.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/gsutil-list-main-bucket]]

## Tools Used

- [[tools/gsutil]]

## Tags

- [[tools/gsutil]]
- [[gcs-enumeration]]
- [[Discovery]]
