---
id: proc-inject-xss-payload
tags:
  - xss-injection
  - payload-modification
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-scheduled-post-with-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.193Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Website-Link

## Summary

This procedure modifies the 'website_link' parameter in a scheduled post creation request to inject a JavaScript payload, exploiting improper input validation in the Kit app on Shopify.

## Description

The vulnerability stems from the lack of strict URL validation in the 'website_link' field, allowing non-HTTP schemes like 'javascript:' or embedded HTML/JS. The payload is stored and rendered when the post is viewed, leading to execution on link click. This is a self-XSS, affecting only the injecting user.

## Requirements

1. Intercepted POST request from the previous procedure
2. Proxy tool for request editing (e.g., Burp Repeater)
3. Knowledge of XSS payloads that evade basic filters (e.g., no script tags if blocked)

## Defense

Defensive measures and detection strategies:

- Enforce strict URL validation (only allow http/https schemes)
- Sanitize and escape user inputs in link fields using libraries like DOMPurify
- Log and alert on suspicious link formats in API requests

## Objectives

1. Bypass filtration to store malicious JavaScript
2. Ensure the payload survives storage and rendering
3. Confirm injection without immediate execution

## Instructions

### Step 1: Edit Request in Proxy

**Context**: Locate the 'website_link' parameter in the multipart body and replace its value with an XSS payload.

Use the proxy's editor to modify the field, e.g., change to `javascript:alert(document.domain)`.

> Expected: Modified request ready for forwarding.

### Step 2: Send Modified Request

**Context**: Forward the altered request to the server to store the payload.

Execute [[commands/create-scheduled-post-with-xss]] or forward via proxy:

```bash
# Equivalent curl for demonstration (adapt with actual auth cookies)
curl -X POST 'https://kitcrm.com/pages/175422/manual_posts/31163' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundary' \
  -F 'website_link=javascript:alert("XSS")' \
  -F 'other_fields=...' # Include all original fields
```

> Expected: 200 OK response, post updated with injected link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-scheduled-post-with-xss]]

## Tools Used


## Tags

- [[xss-injection]]
- [[payload-bypass]]
