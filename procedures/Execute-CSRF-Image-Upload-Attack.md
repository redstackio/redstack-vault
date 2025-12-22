---
id: proc-003
tags:
  - csrf
  - exploit
  - upload
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
updated_at: '2025-12-14T17:27:42.381Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-Image-Upload-Attack

## Summary

This procedure triggers the CSRF attack by having the victim load and submit the malicious HTML form while authenticated, resulting in an unauthorized image upload to their photo set.

## Description

With the victim logged into Chaturbate, opening the PoC HTML in the same browser session allows the form to submit cross-origin to the upload endpoint. Since no CSRF token is required or validated, the server processes the request as legitimate, adding the image to the specified set.

## Requirements

1. Victim authenticated in browser
2. Modified PoC HTML file
3. Delivery method (e.g., email link to local file or hosted page)

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all POST requests
- Use Content-Security-Policy to block inline scripts/forms
- Alert on uploads from non-standard referers

## Objectives

1. Forge and submit the upload request
2. Bypass authentication checks via session cookie
3. Inject payload without victim awareness

## Instructions

### Step 1: Deliver PoC to Victim

**Context**: Ensure the victim loads the HTML while logged in.

Send the `poc.html` via phishing or host it on a malicious site, tricking the victim to open it.

**Expected Output**: File loaded in victim's browser.

### Step 2: Trigger Form Submission

**Context**: Initiate the cross-site request.

Instruct or auto-trigger the "Submit request" button, which posts the form to Chaturbate's endpoint.

**Expected Output**: Server accepts the upload (200 OK response).

### Step 3: Monitor for Errors

**Context**: Confirm no CSRF rejection.

Check browser console for any failures; success means silent upload.

**Expected Output**: No errors, image queued for addition.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[upload]]
