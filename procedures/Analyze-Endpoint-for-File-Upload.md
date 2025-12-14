---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Analyze-Endpoint-for-File-Upload
tags:
  - recon
  - web
  - endpoint-analysis
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:14.679Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Endpoint-for-File-Upload

## Summary

This procedure involves analyzing a web endpoint, specifically the .ashx handler on mobile.starbucks.com.sg, to determine if it enforces proper file type validation for uploads intended for images, revealing unrestricted upload capabilities.

## Description

In the context of the Starbucks mobile site, the .ashx endpoint processes file uploads but fails to validate file types, allowing arbitrary extensions. This analysis uses traffic interception to test upload behaviors, identifying the vulnerability that enables subsequent RCE. Prerequisites include access to a web proxy tool and the target URL.

## Requirements

1. Network access to mobile.starbucks.com.sg
2. Web proxy like Burp Suite for request interception
3. Sample image file for initial testing

## Defense

Defensive measures and detection strategies:

- Implement strict MIME type and extension validation on upload endpoints
- Use web application firewalls (WAF) to block suspicious file uploads
- Log and monitor upload requests for anomalous file types

## Objectives

1. Confirm endpoint accepts files without type restrictions
2. Document request/response patterns for exploitation
3. Identify potential upload directory for later access

## Instructions

### Step 1: Intercept Upload Requests

**Context**: Set up a proxy to capture legitimate upload traffic and analyze the endpoint behavior.

Configure [[tools/Burp-Suite]] as a proxy and browse the mobile site to trigger an image upload. Intercept the POST request to /upload.ashx.

> Inspect headers like Content-Type and form data to understand the upload mechanism.

### Step 2: Test File Type Validation

**Context**: Send various file types to check for restrictions.

Use Burp Repeater to modify the intercepted request: change the file extension from .jpg to .aspx and resend.

> Expected output: Server responds with 200 OK and no rejection, indicating unrestricted upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[web]]
