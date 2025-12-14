---
id: proc-intercept-upload-964550
tags:
  - http-interception
  - mime-manipulation
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
updated_at: '2025-12-13T23:52:49.276Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Avatar-Upload-Request

## Summary

This procedure uses Burp Suite to intercept the avatar upload request to Shopify's accounts endpoint and modifies the Content-Type header to disguise the PNG as HTML, bypassing MIME validation.

## Description

During the upload process to /accounts/<ID>, the request is a multipart/form-data POST. Intercepting it allows changing the file part's Content-Type from image/png to text/html, causing the server to process metadata as HTML. This is key for stored XSS when combined with embedded payloads. Requires an authenticated session and Burp proxy setup.

## Requirements

1. Burp Suite running as proxy (e.g., port 8080)
2. Browser configured to use Burp proxy
3. Authenticated access to accounts.shopify.com

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type validation on server-side (e.g., ignore client-provided Content-Type, scan file content)
- Log and alert on mismatched MIME types in uploads
- Use WAF rules to block modified upload requests

## Objectives

1. Capture and edit the upload request headers
2. Change Content-Type to enable HTML parsing
3. Ensure request forwards without errors

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept traffic from the browser.

In Burp, enable Intercept in Proxy > Options, and point browser proxy to 127.0.0.1:8080.

### Step 2: Trigger and Intercept Request

**Context**: Initiate the avatar upload to capture the POST request.

Navigate to avatar upload in accounts.shopify.com, select the malicious PNG, and submit. In Burp Proxy > Intercept, the request will pause.

### Step 3: Modify Headers

**Context**: Edit the Content-Type for the file part to text/html.

In the intercepted request, locate the account[avatar] part and change Content-Type: image/png to Content-Type: text/html. Forward the request.

> Expected: Request proceeds; check Burp history for 200 OK response.

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

- web-proxy
- upload-bypass
