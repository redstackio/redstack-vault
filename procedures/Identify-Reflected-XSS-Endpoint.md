---
id: proc-uuid-1-1149144
tags:
  - xss
  - recon
  - web-vuln
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
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
updated_at: '2025-12-14T17:28:12.531Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Reflected-XSS-Endpoint

## Summary

This procedure involves reconnaissance to identify web endpoints vulnerable to reflected XSS by testing URL parameters that fetch and render external content without proper sanitization, allowing arbitrary JavaScript injection.

## Description

In this attack scenario, the target is a web application endpoint that accepts a 'url' parameter, fetches content from it using XMLHttpRequest, and renders the response inline without escaping HTML or JavaScript. This leads to reflected XSS when the path or query includes malicious payloads. The procedure requires proxying traffic to inspect parameters and testing with benign URLs to confirm behavior. Prerequisites include access to a web proxy and knowledge of the target's API endpoints.

## Requirements

1. Web proxy tool like Burp Suite for intercepting and modifying requests
2. Knowledge of the target's authenticated endpoints
3. Attacker-controlled domain for testing fetches (optional for initial ID)

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts
- Sanitize and escape all user-supplied content before rendering
- Use HTTPOnly and Secure flags on session cookies to mitigate theft

## Objectives

1. Locate endpoints accepting unsanitized URL parameters
2. Confirm server fetches and renders external content
3. Prepare for payload injection

## Instructions

### Step 1: Intercept and Inspect Requests

**Context**: Use a proxy to capture traffic and identify parameters that trigger content fetching.

No specific command; configure [[tools/Burp-Suite-Professional]] to proxy browser traffic to the target site https://█████/████.

Observe GET requests with 'url' parameter and note if responses include fetched content.

### Step 2: Test with Benign URL

**Context**: Supply a safe external URL to verify rendering without sanitization.

Send a request to https://█████/████&url=http://example.com using the proxy.

**Expected Output**: Response body includes raw HTML from example.com, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[xss]]
- [[recon]]
