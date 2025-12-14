---
tags:
  - burp
  - intercept
  - http
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.240Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f9d0c992-3828-4f6f-b7e0-31d52b36b5b5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Upload-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture the HTTP POST request generated during a profile image upload, allowing inspection of parameters like 'personId' for subsequent manipulation in the IDOR exploit.

## Description

Burp Suite acts as a man-in-the-middle proxy to intercept traffic from the browser to the server. In this DoD web app scenario, triggering an image upload sends a request containing the 'personId', which can be examined for IDOR flaws. Prerequisites include proxy configuration; outcomes include a paused request ready for editing.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Authenticated session from previous access

## Defense

Defensive measures and detection strategies:

- Use HTTPS with certificate pinning to detect proxy interception
- Log and alert on proxy-like traffic anomalies or unusual request timings

## Objectives

1. Capture the upload request
2. Identify vulnerable parameters
3. Prepare for parameter tampering

## Instructions

### Step 1: Configure Proxy and Trigger Upload

**Context**: Set up interception and perform the upload to capture the request.

In Burp Suite, enable Intercept in the Proxy tab. Then, in the browser, select and upload an image.

> The request will pause in Burp. Expected output: HTTP POST request displayed, including multipart/form-data with 'personId'.

### Step 2: Inspect Request

**Context**: Review the captured request for key parameters.

Examine the request body in Burp's Inspector.

> Look for 'personId={your_id}'. Expected output: Confirmation of parameter presence and value.

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

- [[burp]]
- [[intercept]]
- [[http]]
