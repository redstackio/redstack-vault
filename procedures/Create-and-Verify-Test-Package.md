---
tags:
  - setup
  - web
  - file-upload
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
updated_at: '2025-12-14T17:31:30.786Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e0fc4ce2-dfa2-4aae-ae30-8def60a33415
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Verify-Test-Package

## Summary

This procedure sets up a test package on the ██████████ secure file sharing platform to familiarize with the upload and verification process, enabling subsequent interception of requests for IDOR exploitation.

## Description

In the context of testing the DoD's secure file sharing platform, this initial step involves uploading a benign file to create a package, verifying it via email, and accessing the status page. This establishes a controlled environment to observe normal request flows before modifying them for unauthorized access. The platform uses ASP.NET and requires email verification, but no authentication for initial uploads.

## Requirements

1. Web browser access to ████/Default.aspx
2. Valid email address for verification
3. Test file (any small document)

## Defense

Defensive measures and detection strategies:

- Monitor upload logs for anomalous file patterns or high-volume test uploads
- Implement rate limiting on package creation to prevent reconnaissance

## Objectives

1. Create a verifiable package to obtain a baseline PackageID
2. Confirm access to status page for request interception preparation
3. Validate email-based verification workflow

## Instructions

### Step 1: Upload Test File

**Context**: Initiate package creation to generate a PackageID for testing.

Visit ████/Default.aspx in a web browser. Select and upload a test file through the file upload interface.

> The upload process will generate an email with a verification link and initial password.

### Step 2: Verify Package via Email

**Context**: Confirm the package to activate it and enable recipient management.

Check your email for the verification message from the platform. Click the provided link to confirm the upload.

> Successful verification updates the package status to active.

### Step 3: Access Status Page

**Context**: Log in to view and prepare for recipient addition requests.

Use the password from the email to access ███/StatusLogIn.aspx?PackageID=x, where x is your test PackageID.

> The status page loads, showing package details and the 'Add New Recipient' section.

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

- [[setup]]
- [[web]]
- [[file-upload]]
