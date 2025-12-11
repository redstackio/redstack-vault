---
tags:
  - ssrf
  - file-read
  - email-chaining
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Linux
  - Cloud (GCP)
techniques:
  - '[[Data from Local System]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 3e484303-72b2-432e-abde-75fbc68c844b
created_at: '2025-12-11T03:47:56.714Z'
updated_at: '2025-12-11T03:47:56.714Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1005]]'
  - '[[T1190]]'
---
# Chain XSS to File Read and SSRF via Email

## Summary

This procedure chains the stored XSS with GitLab's email notifications to inject stylesheet links, enabling arbitrary file reads and SSRF through premailer-rails processing.

## Description

Email notifications process markdown with premailer-rails, which loads injected <link> tags, allowing local file reads via path traversal or SSRF to internal services like GCP metadata, potentially leaking credentials.

## Requirements

1. Triggered XSS in an issue
2. Email notifications enabled
3. Knowledge of target internal paths/endpoints

## Defense

Defensive measures and detection strategies:

- Disable or sandbox email CSS inlining
- Block file:// and internal URL loads in premailer-rails

## Objectives

1. Inject <link> tags via XSS
2. Trigger file read or SSRF in email processing
3. Exfiltrate sensitive data

## Instructions

### Step 1: Prepare Injection for Email

**Context**: Use XSS to inject <link rel='stylesheet' href='file:///etc/passwd'> or similar for file read.

Modify the markdown payload to include stylesheet links targeting local files or internal URLs.

### Step 2: Trigger Email Notification

**Context**: Cause an email to be sent, processing the injected tags.

Comment or update the issue to generate a notification email.

### Step 3: Observe Leakage

**Context**: Check for leaked data in email or server responses.

Monitor for file contents (e.g., /etc/passwd) or internal responses (e.g., metadata) in the processed email.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- ssrf
- file-read
- email-chaining
