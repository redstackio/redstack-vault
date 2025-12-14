---
id: proc-uuid-2
tags:
  - intercept
  - s3-upload
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.197Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-CSV-and-Intercept-S3-Request

## Summary

This procedure involves uploading a CSV file via TaxJar's import feature while intercepting the underlying S3 request to capture upload parameters for CSRF exploitation.

## Description

Logged in as the attacker on app.taxjar.com, the CSV import triggers a multipart POST to AWS S3 (taxjar-prod-bucket). Interception reveals signed policy, key (e.g., uploads/{uuid}/{filename}), and other params. This sets up the file for cross-account import without completing the attacker's upload.

## Requirements

1. Attacker account logged in
2. Burp Suite configured as proxy
3. Malicious CSV file with transaction data prepared

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints
- Log and monitor S3 upload patterns for anomalies

## Objectives

1. Capture S3 upload details
2. Prepare file for CSRF reuse
3. Avoid completing import in attacker account

## Instructions

### Step 1: Prepare and Initiate Upload

**Context**: Select and submit the CSV to trigger the S3 request.

In the TaxJar dashboard, go to CSV imports, choose a file with arbitrary transactions, and submit the form. Ensure Burp is intercepting traffic to s3.amazonaws.com.

### Step 2: Inspect Intercepted Request

**Context**: Analyze the POST for key parameters.

Examine the multipart/form-data: utf8=true, key=uploads/{uuid}/{filename}, acl=private, policy (base64 JSON with conditions/expiration), X-Amz-Signature, X-Amz-Credential, X-Amz-Algorithm, X-Amz-Date, success_action_redirect=https://app.taxjar.com/csv_imports/upload_complete, and file content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[s3-intercept]]
- [[csv-upload]]
