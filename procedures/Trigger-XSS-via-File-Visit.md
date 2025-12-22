---
tags:
  - xss
  - trigger
  - execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Apache
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 735093f8-4740-46a8-8deb-71674a311dcd
created_at: '2025-12-13T23:56:03.272Z'
updated_at: '2025-12-13T23:56:03.272Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-File-Visit

## Summary

This procedure visits the URL of the uploaded file with a numeric name, causing Apache to serve it as text/HTML and execute the embedded JavaScript payload for XSS.

## Description

Due to the filename '-1', Apache's content negotiation serves the file as HTML instead of image, parsing and running scripts. This can escalate to admin actions like user creation via crafted payloads, targeting visiting administrators.

## Requirements

1. Uploaded file with numeric name
2. Admin-level access to view files
3. Knowledge of target URL structure

## Defense

Defensive measures and detection strategies:

- Configure Apache to force MIME types for uploads directory
- Monitor access to upload paths for suspicious views
- Implement Content-Security-Policy to block inline scripts

## Objectives

1. Force HTML rendering of uploaded file
2. Execute JavaScript payload
3. Achieve session compromise or escalation

## Instructions

### Step 1: Construct URL

**Context**: Build the direct link to the file.

Determine path: `/wp-content/uploads/YYYY/MM/-1` (replace with actual year/month).

### Step 2: Visit as Admin

**Context**: Trigger execution in admin context.

Log in as admin and navigate to the URL. Observe payload execution (e.g., alert or iframe action).

### Step 3: Validate Impact

**Context**: Confirm exploitation success.

Check for effects like new user in admin or network requests from payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[Execution]]
