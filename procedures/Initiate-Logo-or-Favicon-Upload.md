---
id: proc-uuid-2
tags:
  - nextcloud
  - file-upload
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.878Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Logo-or-Favicon-Upload

## Summary

This procedure triggers the file upload mechanism in Nextcloud's theming settings, generating a POST request that can be intercepted for parameter manipulation.

## Description

Once in the theming interface, selecting and uploading an image file for the logo or favicon sends a multipart/form-data POST request to the server. The request includes a 'key' parameter that determines the stored filename. This step is crucial as it initiates the vulnerable endpoint without modification yet, allowing for proxy interception in the next phase. It targets PHP-based Nextcloud installations and assumes no prior proxy interference.

## Requirements

1. Access to theming settings page
2. A valid image file (e.g., logo.png or favicon.ico)
3. Browser proxy set to Burp Suite

## Defense

Defensive measures and detection strategies:

- Validate file types and sizes on the client and server side
- Log all upload attempts with file metadata
- Use intrusion detection to flag frequent theming changes by admins

## Objectives

1. Generate the upload POST request
2. Include a sample file to test the endpoint
3. Ensure request is ready for interception

## Instructions

### Step 1: Select Upload Type

**Context**: Choose between logo or favicon to target the appropriate upload field.

No specific command; in the web interface, locate the 'Upload logo' or 'Upload favicon' button.

> Click the button to open the file selection dialog.

### Step 2: Upload Image File

**Context**: Submit a test image to trigger the request.

No specific command; select an image file (e.g., test.png) and click upload.

> The browser sends a POST to /settings/admin/theming with multipart data including the file and 'key' parameter. If proxied, the request halts at Burp.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[nextcloud]]
- [[file-upload]]
- [[web]]
