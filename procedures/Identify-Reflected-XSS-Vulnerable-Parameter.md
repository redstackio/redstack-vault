---
tags:
  - xss
  - reflected-xss
  - web-testing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-reflect-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:02.400Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 772239f3-5717-406c-89ad-a9e81ca8d9af
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Reflected-XSS-Vulnerable-Parameter

## Summary

This procedure involves testing a web endpoint's URL parameters to identify reflection of user input without sanitization, confirming a potential reflected XSS vulnerability. It is primarily used in web application security assessments to map attack surfaces on public-facing systems like government websites.

## Description

In a reflected XSS attack, user-supplied input via URL parameters is echoed back in the server's response without proper encoding, allowing attackers to inject and execute malicious JavaScript when a victim visits the crafted URL. This procedure focuses on the discovery phase: systematically testing parameters for reflection. For the DoD system, the ██████= parameter in ███████████?████████= was found to reflect input directly. Prerequisites include access to the target URL and basic web debugging tools. Expected outcomes: confirmation of unsanitized reflection, enabling escalation to payload injection.

## Requirements

1. Network access to the target web endpoint (e.g., https://█████?██████=)
2. Browser with developer tools or curl for sending requests
3. Knowledge of common XSS test strings (e.g., '<script>alert(1)</script>')

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) for all user inputs in responses
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor access logs for suspicious parameter values containing script tags

## Objectives

1. Confirm parameter reflection without sanitization
2. Document the vulnerable endpoint for reporting
3. Assess potential impact on user sessions

## Instructions

### Step 1: Test Parameter Reflection

**Context**: Send a simple non-malicious string to the parameter and inspect the response for direct reflection.

**Command** ([[commands/curl-reflect-test]]):
```bash
curl -s "https://█████?██████=test123" | grep -i "test123"
```

> This command fetches the page and searches for the test string in the output. If 'test123' appears unencoded in the HTML, reflection is confirmed.

### Step 2: Inspect Response Source

**Context**: Use browser tools to view the full HTML source and verify if the input is placed in a script-executable context (e.g., inside HTML tags).

No specific command; manually visit the URL in a browser, right-click > View Page Source, and search for the test input.

> Look for the input appearing as raw text within <body> or attribute values, indicating XSS potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-reflect-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[web-vulnerability]]
