---
tags:
  - xss
  - file-upload
  - gitlab
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ae2188a2-ab71-487a-9576-94a0cbd4ca26
created_at: '2025-12-14T00:11:16.702Z'
updated_at: '2025-12-14T00:11:16.702Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload Malicious Design in GitLab

## Summary

This procedure involves creating a GitLab project and uploading a design file with a malicious filename to bypass sanitization and enable attribute injection for XSS.

## Description

The attack targets GitLab's Design Management feature by intercepting the upload request and modifying the Content-Disposition header to include special characters like quotes, which are not properly validated in the DesignReferenceFilter. This sets up for later markdown injection. Prerequisites include a GitLab account and proxy tool setup.

## Requirements

1. Valid GitLab account with project creation access
2. Burp Suite or similar proxy for request interception
3. Access to GitLab web interface

## Defense

Defensive measures and detection strategies:

- Implement stricter filename validation in CarrierWave and regex patterns
- Monitor for unusual Content-Disposition headers in uploads

## Objectives

1. Upload design with injected filename
2. Confirm persistence in issue designs
3. Prepare for XSS injection

## Instructions

### Step 1: Create Project and Issue

**Context**: Set up the environment for design upload.

Access GitLab and create a new project, then create an issue within it.

> This establishes the base for uploading designs.

### Step 2: Set Up Proxy and Upload Design

**Context**: Intercept and modify the upload request.

Use [[tools/Burp-Suite]] to intercept the design upload request. Modify the header to: 'Content-Disposition: form-data; name="1"; filename*=ASCII-8BIT''bbb%22class%3D%22gfm%22a%3D%27.png'.

> This injects special characters bypassing Workhorse sanitization.

### Step 3: Confirm Upload

**Context**: Verify the malicious design is stored.

Refresh the page to see the design with the injected filename.

> Expected: Design listed with filename containing quotes and classes.

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

- xss
- file-upload
- gitlab
