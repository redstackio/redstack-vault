---
tags:
  - burp-suite
  - http-intercept
  - mime-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:59.813Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: eb243460-b142-430c-9030-fb7bad353b97
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Upload-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture and alter the Content-Type header of Reddit's image upload request, changing it from image/png to image/svg+xml to disguise the upcoming corrupted file.

## Description

Targeting Reddit's media upload endpoint, this step intercepts the POST request for the second image. The modification exploits the lack of server-side content validation, allowing a mismatched MIME type to pass. This leads to improper processing and storage of a 'None' URL. Requires Burp Suite running as a proxy; expected outcome is a modified request ready for content replacement, without immediate detection.

## Requirements

1. Burp Suite Professional or Community edition installed and running
2. Browser proxy configured (e.g., FoxyProxy extension pointing to 127.0.0.1:8080)
3. Ongoing media post session from prior procedure
4. Knowledge of HTTP headers and request structure

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type validation on server-side using libraries like file-type.js
- Log and alert on proxy-detected MIME changes in upload traffic
- Use WAF rules to block anomalous Content-Type switches in file uploads

## Objectives

1. Capture the upload request without disrupting the session
2. Modify the MIME type to enable SVG processing path
3. Prepare for content injection while maintaining request integrity

## Instructions

### Step 1: Configure and Intercept

**Context**: Set up interception to capture the second image upload.

No command; Burp UI:

- In Burp, go to Proxy > Intercept tab and ensure 'Intercept is on'.
- Trigger the second PNG upload in Reddit UI.

> Expected: Request appears in Burp with headers like Content-Type: image/png.

### Step 2: Locate and Edit Content-Type

**Context**: Identify the MIME header for modification.

No command; edit in Burp:

- In the intercepted request, find the 'Content-Type: image/png' header.
- Right-click and select 'Edit header' or manually change to 'Content-Type: image/svg+xml'.

> Expected: Header updated; request body still contains PNG binary.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- burp-suite
- http-intercept
- mime-modification
