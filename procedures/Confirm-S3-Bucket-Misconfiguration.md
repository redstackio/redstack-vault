---
id: proc-uuid-2
tags:
  - aws
  - s3
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:58.510Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Confirm-S3-Bucket-Misconfiguration

## Summary

This procedure confirms an S3 bucket's public access misconfiguration by observing unrestricted content listing, highlighting the lack of authentication controls.

## Description

After initial URL access, this step involves manual inspection to verify that all contents are exposed. In the DoD incident, this revealed directories like admin and production without barriers, enabling broad data exposure. It serves as a discovery step before automated enumeration.

## Requirements

1. Successful Step 1 from attack chain
2. Web browser for manual browsing
3. Basic understanding of S3 directory structure

## Defense

Defensive measures and detection strategies:

- Implement least-privilege bucket policies
- Use AWS Trusted Advisor to scan for public buckets
- Set up alerts on S3 access logs for public requests

## Objectives

1. Validate no access restrictions
2. Scope the exposed data types
3. Identify high-value directories

## Instructions

### Step 1: Inspect Bucket Listing

**Context**: Review the public page to confirm open access.

**Command** (Browser):
```bash
# No CLI; use browser to view https://██████.s3.amazonaws.com/
```

> The page lists all root contents publicly. Look for indicators like no login prompt and full file visibility.

### Step 2: Explore Subdirectories

**Context**: Click into folders to test depth of exposure.

**Command** (Manual Navigation):
```bash
# Navigate to paths like /admin/ or /production/
```

> Expected output: Subdirectory contents load, showing sensitive DoD files.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- aws
- s3
- discovery
