---
id: proc-003
tags:
  - poc
  - csrf
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.164Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# PoC-Generation-for-CSRF-using-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept a legitimate admin request and generate a malicious HTML form that exploits the CSRF vulnerability in express-cart's admin endpoints.

## Description

By capturing POST parameters from actions like discount creation (/admin/settings/discount/create), an auto-submitting form is crafted to forge requests. The root cause is the lack of CSRF tokens, allowing external sites to submit data if the victim is authenticated.

## Requirements

1. Burp Suite installed and running
2. Browser proxy configured to Burp (e.g., 127.0.0.1:8080)
3. Authenticated admin session

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Monitor for anomalous POST requests from external referers
- Use Content Security Policy to restrict form submissions

## Objectives

1. Intercept and extract request parameters
2. Build a functional CSRF PoC HTML
3. Test PoC in isolation

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Perform an admin action while proxied through Burp to capture data.

**Command** (Burp Usage):
In Burp Proxy, enable interception. In browser, submit a discount creation form.

> Burp captures the POST to /admin/settings/discount/create with params like code, type, value, start, end. Expected output: Request details in Burp Repeater.

### Step 2: Craft PoC HTML

**Context**: Create an HTML file mimicking the form.

**Command** (Manual HTML Creation):
Use a text editor to write the form.

> Include hidden inputs for captured params and JavaScript to auto-submit. Expected output: Valid HTML file that posts to target endpoint.

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

- poc
- csrf
- burp-suite
