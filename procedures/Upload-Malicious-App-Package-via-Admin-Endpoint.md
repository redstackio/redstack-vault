---
id: proc-uuid-2
tags:
  - file-upload
  - broken-access-control
  - rocket-chat
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
updated_at: '2025-12-14T17:29:09.746Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-App-Package-via-Admin-Endpoint

## Summary

This procedure exploits the lack of privilege checks on the Rocket.Chat admin app installation endpoint to upload an arbitrary app package as a non-admin user enabling installation of potentially malicious applications.

## Description

Rocket.Chat's `/admin/app/install` endpoint allows file uploads without verifying user roles allowing non-admins to install apps. The attacker prepares a ZIP package with a custom app.json defining the app ID and uploads it via the web form. Prerequisites include a valid non-admin session and the outcome is the app being installed with a user-controlled ID ready for activation.

## Requirements

1. Authenticated non-admin session from prior login
2. Malicious app package ZIP file with app.json containing controlled ID
3. Web browser with developer tools or HTTP client for upload

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks requiring admin roles for app uploads
- Validate uploaded files for malicious content and signatures
- Log and alert on app installation attempts from non-admin users

## Objectives

1. Upload arbitrary app package without authorization
2. Install the app with a predictable ID
3. Set up for subsequent activation

## Instructions

### Step 1: Prepare App Package

**Context**: Create or obtain a ZIP file containing the malicious app with app.json defining the app ID.

**Command** (Manual Preparation):

Ensure the ZIP includes `app.json` with fields like `id: "malicious-app"`.

> Expected output: Valid ZIP ready for upload.

### Step 2: Access and Submit Upload Form

**Context**: Navigate to the vulnerable endpoint and perform the upload.

**Command** (Browser Action):

Go to `http://<rocket-chat-url>/admin/app/install` and select the ZIP file in the upload form then submit.

> Expected output: Success message or response with installed app details including ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- broken-access-control
- rocket-chat
