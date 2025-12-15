---
id: proc-test-xss-935503-2
tags:
  - xss
  - payload-testing
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:09.658Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test XSS with Simple Payload

## Summary

This procedure tests the XSS vulnerability using a basic script injection to confirm arbitrary JavaScript execution on the vulnerable thank-you page.

## Description

By injecting a payload like '<script>alert(1)</script>' into the email parameter, the procedure verifies if the script executes, popping an alert. This is done via URL manipulation, targeting the lack of input sanitization. Success indicates the site is vulnerable to reflected XSS.

## Requirements

1. Vulnerable endpoint identified
2. Web browser
3. URL encoding knowledge for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with libraries like OWASP ESAPI
- Deploy WAF to block common XSS payloads
- Log and alert on script tag injections

## Objectives

1. Execute simple JavaScript to confirm XSS
2. Validate payload delivery and execution
3. Prepare for advanced exploitation

## Instructions

### Step 1: Craft Test URL

**Context**: Encode and inject the payload into the email parameter to bypass basic filters.

**Command** (Manual URL Construction):

https://cz.acronis.com/dekujeme-za-odber-novinek-produktu-disk-director/?user=OK&oktosend=&email=tester@gmail.comaxsar%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3eqw87f

> The payload closes any open script or tag and injects alert(1). Load the URL.

### Step 2: Verify Execution

**Context**: Check for successful script run.

**Command** (Browser Interaction):

Load page and observe for alert dialog.

> Expected: Alert box with '1' appears, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- testing
