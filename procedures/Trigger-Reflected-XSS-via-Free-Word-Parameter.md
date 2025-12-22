---
id: proc-starbucks-xss-trigger
tags:
  - xss
  - reflected-xss
  - injection
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:06.204Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Reflected-XSS-via-Free-Word-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in the Starbucks Japan store search page by injecting a JavaScript payload via the 'free_word' parameter, allowing arbitrary code execution in the victim's browser.

## Description

The store search endpoint at https://www.starbucks.co.jp/store/search/ fails to sanitize user input in the 'free_word' query parameter, reflecting it directly into the HTML response. An attacker crafts a URL with an encoded <script> tag that breaks out of any attributes and executes JavaScript, such as an alert. This can be used as a proof-of-concept or foundation for more severe attacks like data theft. The target environment is a public-facing web application; no authentication is required, but the victim must visit the malicious link.

## Requirements

1. Web browser like Firefox for testing
2. Direct internet access to https://www.starbucks.co.jp/store/search/
3. URL encoding knowledge for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding (e.g., HTML entity encoding) on all user inputs
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in logs or WAF alerts for injection patterns

## Objectives

1. Confirm XSS vulnerability by executing a benign script
2. Demonstrate potential for arbitrary JavaScript in victim context
3. Lay groundwork for data exfiltration

## Instructions

### Step 1: Craft and Navigate to Payload URL

**Context**: Encode a simple script payload to inject into the 'free_word' parameter, breaking out of HTML context to execute JavaScript.

**Command** (Direct URL Navigation):

No shell command; use browser to visit:

```url
https://www.starbucks.co.jp/store/search/?free_word=%22%3E%3Cscript%3Ealert()%3C/script%3E%3E
```

> This URL decodes to free_word="><script>alert()</script>">, injecting the script tag. Expected output: Alert dialog pops up in the browser, proving execution.

### Step 2: Verify Reflection in Page Source

**Context**: Inspect the page to confirm the payload is reflected unsanitized.

**Instructions**: Right-click and view page source in Firefox; search for 'alert()' to see the injected script.

> Expected output: Raw <script>alert()</script> visible in HTML, without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Initial Access]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[reflected-xss]]
