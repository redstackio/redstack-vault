---
id: proc-email-xss-slack
tags:
  - xss
  - stored-xss
type: procedure
tools:
  - '[[tools/Email-Client-macOS]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:15.142Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Upload-HTML-via-Email-for-Stored-XSS

## Summary

This alternative procedure uploads unfiltered HTML/JS via email to Slack's integration, storing it as executable text/html on files.slack.com for stored XSS.

## Description

Slack's email integration stores plaintext emails without filtering, allowing HTML/JS payloads. Accessing via 'open original' or url_private executes on the trusted domain, enabling phishing or RCE hosting without external servers.

## Requirements

1. Slack workspace with email integration enabled.
2. Email client for sending plaintext with HTML.
3. Access to uploaded file URL.

## Defense

Defensive measures and detection strategies:

- Filter HTML in email uploads; force text/plain or add security headers.
- Block direct HTML execution on file views.
- Scan uploads for JS payloads.

## Objectives

1. Store executable HTML on trusted domain.
2. Enable phishing or payload delivery.
3. Bypass external hosting needs.

## Instructions

### Step 1: Prepare and Send Email

**Context**: Craft email with malicious HTML.

Use [[tools/Email-Client-macOS]] in plaintext mode (CMD+SHIFT+T on macOS) to send to Slack's custom email address with <script>alert('XSS')</script> or full payload.

> Email uploads to files.slack.com as text/html.

### Step 2: Access and Execute

**Context**: Retrieve and trigger XSS.

Use /api/files.info url_private or 'open original' to load the file.

> HTML executes in browser on *.slack.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Email-Client-macOS]]

## Tags

- xss
- stored-xss
