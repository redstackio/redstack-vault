---
tags:
  - xss
  - url-modification
  - payload-injection
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
updated_at: '2025-12-14T03:46:38.108Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ccba3169-d438-42a4-ab6f-4c10e5f39d0d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Extract-and-Modify-Redirect-URL

## Summary

This procedure involves extracting the 'redirect_url' from the intercepted Imgur gifting request and injecting an XSS payload into its 'redirect' parameter to prepare for reflection and execution.

## Description

Following request interception, this step parses the JSON payload to isolate the 'redirect_url', which embeds a modifiable 'redirect' query parameter. The attacker replaces the benign redirect value with a javascript: URI containing malicious JavaScript, such as alert(document.cookie), exploiting the lack of sanitization. This targets the Imgur web platform in an authenticated session, leading to client-side code execution upon URL load. Prerequisites include the prior interception; outcomes enable payload delivery for cookie theft or further attacks.

## Requirements

1. Intercepted POST request details from previous procedure
2. Text editor or URL manipulation tool
3. Understanding of URL encoding and javascript: schemes

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all redirect parameters to block javascript: URIs
- Implement URL whitelisting for redirects
- Monitor for tampered URLs in logs or client-side

## Objectives

1. Extract vulnerable parameter from request
2. Inject XSS payload without breaking URL structure
3. Validate modified URL for immediate use

## Instructions

### Step 1: Extract redirect_url

**Context**: Locate and copy the parameter from the JSON body.

Manually inspect the request body and extract 'redirect_url': 'https://imgur.com/emerald/give-emerald?username=hermawanferdi&redirect=https://imgur.com/user/hermawanferdi'.

> Ensure the full URL is copied accurately.

### Step 2: Modify with XSS Payload

**Context**: Replace the redirect value to inject executable code.

Edit the URL to: 'https://imgur.com/emerald/give-emerald?username=hermawanferdi&redirect=javascript:alert(document.cookie)'.

> Test URL parsing in browser dev tools to confirm no errors.

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
- payload
- modification
