---
id: proc-trigger-xss-vulnerable-swagger-ui
tags:
  - xss-trigger
  - swagger-ui
  - payload-execution
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.377Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Vulnerable-Swagger-UI

## Summary

This procedure loads the malicious Swagger specification into the vulnerable UI on the target page, causing the injected JavaScript to execute and potentially steal user data.

## Description

The Zomato developers documentation at https://developers.zomato.com/documentation uses an old Swagger UI that parses external JSON specs without sanitizing fields like property names. By directing it to the hosted malicious spec, the payload reflects and runs in the browser, allowing cookie theft or further attacks.

## Requirements

1. Access to the target URL: https://developers.zomato.com/documentation
2. Hosted malicious JSON endpoint URL
3. Victim browser context (e.g., logged-in user session)

## Defense

Defensive measures and detection strategies:

- Patch Swagger UI to latest version
- Disable external spec loading or whitelist domains
- Monitor browser console for script execution errors

## Objectives

1. Direct Swagger UI to load the malicious spec
2. Observe payload execution (e.g., alert or data exfil)
3. Collect stolen data like cookies

## Instructions

### Step 1: Access Target Page

**Context**: Navigate to the vulnerable documentation.

Open https://developers.zomato.com/documentation in a browser.

### Step 2: Configure Spec URL

**Context**: Point Swagger UI to the malicious endpoint.

In the Swagger UI interface, enter the hosted JSON URL (e.g., http://attacker.com/swagger.json) into the spec loading field and submit.

### Step 3: Observe Execution

**Context**: Verify the XSS triggers during rendering.

The UI parses the JSON; watch for the alert('document.cookie') or network requests to attacker servers if exfiltrating data.

> Impact includes stealing session tokens for account compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[payload-execution]]
