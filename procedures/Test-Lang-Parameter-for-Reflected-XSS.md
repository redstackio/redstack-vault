---
id: proc-test-lang-xss
tags:
  - xss
  - reflected-xss
  - testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-test-lang]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:16.018Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Lang Parameter for Reflected XSS

## Summary

This procedure tests the 'lang' parameter for reflected XSS by injecting a JavaScript payload and checking if it is echoed without sanitization in the response.

## Description

Targeting the Glassdoor endpoint, inject a payload like <script>alert('XSS')</script> into the 'lang' parameter. If reflected unsanitized, it indicates a vulnerability allowing arbitrary script execution when a victim visits the crafted URL. This is typically done via HTTP requests or browser, with outcomes including payload visibility in page source.

## Requirements

1. Identified endpoint from prior recon
2. HTTP request tool
3. Basic payload knowledge

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs (e.g., HTML entity encoding)
- Validate parameter values against expected language codes
- Monitor for anomalous request payloads

## Objectives

1. Inject test payload into 'lang' parameter
2. Confirm lack of sanitization in response
3. Assess potential for script injection

## Instructions

### Step 1: Craft Malicious URL

**Context**: Build a URL with the XSS payload in the 'lang' parameter.

**Command** ([[commands/curl-xss-test-lang]]):
```bash
curl "https://help.glassdoor.com/gd_requestsubmitpage?lang=<script>alert('XSS')</script>"
```

> Inspect the response body for the raw payload.

### Step 2: Analyze Response

**Context**: Check if the payload is reflected without escaping.

Use grep or browser view source to search for the payload in the output.

> Expected: Payload appears as-is in HTML, not encoded.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test-lang]]

## Tools Used


## Tags

- [[xss]]
- [[testing]]
