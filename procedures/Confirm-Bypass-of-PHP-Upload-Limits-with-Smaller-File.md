---
id: proc-uuid-3
tags:
  - php
  - bypass
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.120Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Confirm Bypass of PHP Upload Limits with Smaller File

## Summary

This procedure uses a moderately oversized file (e.g., 8.20 MB JPEG) to verify that PHP's upload_max_filesize (2M) is not enforced, confirming application-level bypass of configuration limits.

## Description

By uploading a file larger than the php.ini limit but smaller than extreme sizes, this step isolates whether the issue is in PHP config enforcement or app logic, showing no errors and successful processing.

## Requirements

1. Test file of 8.20 MB (e.g., JPEG image)
2. Browser access to upload form
3. Knowledge of target's php.ini settings (e.g., upload_max_filesize=2M)

## Defense

Defensive measures and detection strategies:

- Validate file sizes in application code before PHP handling
- Audit php.ini enforcement in upload handlers
- Alert on uploads exceeding configured limits

## Objectives

1. Validate PHP limit non-enforcement
2. Ensure consistent bypass behavior
3. Build evidence for DoS potential

## Instructions

### Step 1: Select and Upload File

**Context**: Submit the oversized JPEG to test limit adherence.

In browser, navigate to upload page, select 8.20 MB JPEG, and submit.

> Expected: Upload completes without errors, despite exceeding 2M limit.

### Step 2: Check for Errors

**Context**: Confirm no rejection messages.

Review page response; no warnings should appear.

> Success: File accepted, proving bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[php]]
- [[bypass]]
- [[file-upload]]
