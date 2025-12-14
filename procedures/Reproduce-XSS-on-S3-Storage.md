---
tags:
  - s3
  - reproduction
  - storage-backend
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.458Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 618adb77-cefa-4137-b043-b2381bcccf98
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reproduce-XSS-on-S3-Storage

## Summary

This procedure verifies the XSS vulnerability when Active Storage is configured with S3 as the backend, ensuring the exploit is not limited to local storage.

## Description

Active Storage abstracts storage services, but MIME type detection occurs before upload. The .mml file retains its extension and MIME type when pushed to S3, and the signed URL serves it identically, allowing the same MathML rendering and JS execution in Firefox.

## Requirements

1. Rails app configured with S3 storage (AWS credentials)
2. Prepared math.mml payload
3. Firefox for testing

## Defense

Defensive measures and detection strategies:

- Configure S3 bucket policies to reject executable MIME types
- Use Rails middleware to rewrite MIME headers on serve
- Monitor S3 access logs for unusual file views

## Objectives

1. Upload to S3 via Active Storage
2. Access S3 URL and trigger XSS
3. Confirm backend independence

## Instructions

### Step 1: Configure S3 in Rails

**Context**: Set up Active Storage for S3.

In config/storage.yml, define S3 service with bucket and credentials; set config.active_storage.service = :s3.

> Restart Rails server if needed.

### Step 2: Upload and Test

**Context**: Repeat upload and access steps.

Upload math.mml using the app interface, retrieve the S3-generated URL, open in Firefox, and click to trigger.

> Expected: Identical alert execution as local storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- s3
- reproduction
- storage-backend
