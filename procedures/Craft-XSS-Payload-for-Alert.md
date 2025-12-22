---
tags:
  - xss
  - javascript
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/open-xss-alert-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 898f647a-97ef-47cc-8bcb-cb16311735ac
created_at: '2025-12-13T23:56:20.471Z'
updated_at: '2025-12-13T23:56:20.471Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for Alert

## Summary

This procedure crafts a proof-of-concept URL to exploit XSS in Swagger-UI by injecting a base64-encoded payload via configUrl, resulting in a simple JavaScript alert.

## Description

The configUrl parameter accepts data: URLs without proper validation, allowing base64-encoded HTML/JS to be loaded and executed. This can demonstrate arbitrary JS execution in the application's context.

## Requirements

1. Access to the vulnerable endpoint
2. Browser for testing
3. Knowledge of base64 encoding for payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and validate configUrl inputs
- Monitor for data: URL usage in parameters

## Objectives

1. Confirm XSS vulnerability
2. Execute simple JS payload
3. Validate injection point

## Instructions

### Step 1: Craft and Open URL

**Context**: Construct the malicious URL and test in browser.

Execute [[commands/open-xss-alert-url]] to open:

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-alert-payload'
```

> Replace with actual base64 payload that injects <script>alert('XSS')</script> via YAML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/open-xss-alert-url]]

## Tools Used

- [[Browser]]

## Tags

- [[xss]]
- [[JavaScript]]
