---
tags:
  - xss
  - stored-xss
type: procedure
tools:
  - '[[tools/Browser-Chrome]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
id: b3600eb8-5da0-46b6-886b-b246db28ff1e
created_at: '2025-12-14T17:26:49.110Z'
updated_at: '2025-12-14T17:26:49.110Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-phpBB-Forum

## Summary

This procedure triggers the Stored XSS by viewing pages where the malicious emoji is displayed, such as posts, comments, or admin sections, executing the injected payload.

## Description

Once imported, the unsanitized SMILEY_IMG with XSS (e.g., onmouseover=alert()) appears in forum content. Any user viewing affected pages triggers the script, enabling defacement, cookie theft, or malware distribution. Impact is persistent and affects all users.

## Requirements

1. Successful import of malicious emoji
2. Access to forum pages (as any user)
3. Browser for viewing

## Defense

Defensive measures and detection strategies:

- Output-encode all user-controlled content, including emojis
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for unusual JavaScript execution in forum logs

## Objectives

1. Execute XSS payload on page load/interaction
2. Demonstrate impact like alerts or theft
3. Affect multiple users persistently

## Instructions

### Step 1: View Affected Content

**Context**: Navigate to pages using the malicious emoji.

**Command** (Manual via Browser):

Use [[tools/Browser-Chrome]] to visit a post or admin page with the emoji.

> Expected output: Payload triggers, e.g., alert() on mouseover.

### Step 2: Verify Execution

**Context**: Confirm XSS fires and potential actions.

**Command** (Manual):

Interact with emoji (hover) and check console/network for theft.

> Expected output: Script execution, possible cookie exfil.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Chrome]]

## Tags

- [[xss]]
- [[stored-xss]]
