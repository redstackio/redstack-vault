---
id: proc-starbucks-trigger-xss
tags:
  - xss
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-access-content]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.739Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS via Uploaded Content

## Summary

This procedure accesses and renders the uploaded malicious content to execute stored XSS in the victim's browser context, exploiting unsanitized server-side rendering.

## Description

After uploading, the content is stored and displayed without escaping, allowing script execution. On the Starbucks site, viewing the uploaded file triggered the XSS payload. This can lead to session theft or phishing. Prerequisites: successful upload and knowledge of access path.

## Requirements

1. Uploaded file path or ID from previous step.
2. Victim access to the rendered content (e.g., via site page).
3. Browser for execution observation.

## Defense

Defensive measures and detection strategies:

- Sanitize all user-uploaded content before rendering (e.g., HTML entity encoding).
- Use Content Security Policy (CSP) to block inline scripts.
- Detect anomalous JavaScript execution via WAF logs.

## Objectives

1. Execute injected JavaScript in user sessions.
2. Demonstrate impact like alerts or data exfiltration.
3. Highlight persistence of the attack.

## Instructions

### Step 1: Access the Uploaded Content

**Context**: Visit or fetch the stored file to trigger rendering.

**Command** ([[commands/curl-access-content]]):
```bash
curl https://campaign.starbucks.com.sg/path/to/uploaded/test.html -v
```

> If rendered in browser, observe payload execution (e.g., alert). Curl shows raw content.

### Step 2: Verify Execution

**Context**: In a browser, load the page and check console for script run.

> Success: JavaScript executes, confirming stored XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-content]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
