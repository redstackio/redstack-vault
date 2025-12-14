---
id: proc-xss-identify-001
tags:
  - xss
  - reflected-xss
  - vulnerability-identification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.729Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Reflected XSS in Version Parameter

## Summary

This procedure involves testing the 'version' parameter in the verify.asp endpoint to detect if user input is reflected without sanitization, enabling cross-site scripting attacks.

## Description

In the context of the Acronis-managed website at http://www.grouplogic.com/files/glidownload/verify.asp, the 'version' parameter accepts user input that is directly echoed back into the HTML response. This lack of input validation allows attackers to inject HTML and JavaScript, leading to reflected XSS. The procedure requires only a web browser and focuses on confirming reflection by observing raw input in the page source.

## Requirements

1. Access to a web browser with developer tools
2. Knowledge of the target URL: http://www.grouplogic.com/files/glidownload/verify.asp
3. Basic understanding of URL parameters and HTML inspection

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and output encoding (e.g., HTML entity encoding) for all user inputs
- Use Content Security Policy (CSP) headers to restrict script execution
- Monitor web server logs for suspicious parameter values containing script tags

## Objectives

1. Confirm reflection of user input in the response
2. Identify potential for HTML/JavaScript injection
3. Validate the vulnerability for further exploitation

## Instructions

### Step 1: Access the Endpoint and Test Basic Reflection

**Context**: Load the endpoint with a simple parameter to check if input is echoed back unaltered.

Navigate to: http://www.grouplogic.com/files/glidownload/verify.asp?version=test

Inspect the page source (right-click > View Page Source) and search for "test". If it appears as plain text without encoding, reflection is confirmed.

> Expected output: The response includes something like "version=AC12test" directly in the HTML, indicating no sanitization.

### Step 2: Test for Special Character Handling

**Context**: Append special characters to probe for injection points.

Modify the URL to: http://www.grouplogic.com/files/glidownload/verify.asp?version=test%3Cscript%3Ealert(1)%3C/script%3E

Reload and check if the script tag is rendered or partially executed.

> Expected output: Special characters like < > are not escaped, allowing potential payload injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web-vulnerability]]
