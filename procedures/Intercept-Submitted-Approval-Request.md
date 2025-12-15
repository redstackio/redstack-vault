---
tags:
  - intercept
  - proxy
  - http-request
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:36.274Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 82ad1a37-c5aa-4dc0-8e50-00aca1341dd1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Submitted-Approval-Request

## Summary

Intercept the POST request from the approval form submission using a proxy tool to examine and prepare the request for modification.

## Description

After submitting the form, the request targets the WordPress REST API endpoint /wp-json/brc/v1/approval-requests via POST with multipart/form-data including the g-recaptcha-response. Interception allows inspection of headers, body, and token without altering the flow initially. This is crucial for identifying the exact payload structure in a PHP/WordPress environment.

## Requirements

1. Proxy tool like Burp Suite installed and configured as browser proxy
2. HTTPS interception enabled (install CA certificate)
3. Prior completion of form filling

## Defense

Defensive measures and detection strategies:

- Use HTTPS with HSTS to complicate proxy interception
- Log all API requests with user agents and IPs
- Detect proxy-like user agents or unusual traffic patterns

## Objectives

1. Capture complete request details
2. Verify valid token presence
3. Prepare for payload preservation in tampering

## Instructions

### Step 1: Configure Proxy Interception

**Context**: Set up the proxy to catch the submission.

In Burp Suite, enable Intercept in Proxy > Intercept tab and configure browser to use 127.0.0.1:8080 as proxy.

> Expected output: Proxy ready, no traffic until submission.

### Step 2: Submit Form and Capture Request

**Context**: Trigger the request and halt it for inspection.

Submit the form; Burp will pause the request.

Inspect: Method POST, URL /wp-json/brc/v1/approval-requests, body with fields and g-recaptcha-response.

> Expected output: Full request visible, including token (long string from Google).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
