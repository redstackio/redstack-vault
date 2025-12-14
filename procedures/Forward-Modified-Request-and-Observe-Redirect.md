---
id: proc-uuid-3
tags:
  - forward-request
  - redirect
  - '302'
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.683Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forward-Modified-Request-and-Observe-Redirect

## Summary

This procedure forwards the modified HTTP request to the server, observing the resulting redirect response that confirms the open redirect vulnerability.

## Description

After Host header manipulation, forwarding triggers the server's logic to issue a 302 redirect to the specified host. This demonstrates the lack of validation, allowing arbitrary external redirects on sites like www.localizestaging.com.

## Requirements

1. Modified request ready in Burp Suite
2. Server accessible and responsive
3. Ability to inspect HTTP responses

## Defense

Defensive measures and detection strategies:

- Implement redirect validation to internal/allowlisted URLs only
- Rate-limit or block requests with mismatched Host headers

## Objectives

1. Elicit the vulnerable redirect response
2. Capture the Location header for analysis
3. Validate exploit success before chaining

## Instructions

### Step 1: Forward in Burp

**Context**: Send the tampered request to the target server.

Click 'Forward' in Burp's Intercept tab to release the request.

### Step 2: Inspect Response

**Context**: Analyze the server's reply for redirect confirmation.

Switch to the Response tab; look for HTTP/1.1 302 Found and Location: http://evil.com/.

**Expected Output**: 302 response with redirect to attacker domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[forward-request]]
- [[redirect]]
- [[302]]
