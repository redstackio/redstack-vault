---
tags:
  - upload-bypass
  - xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e8a390ed-36d2-416b-b8c3-846d3c3292af
created_at: '2025-12-11T03:47:56.727Z'
updated_at: '2025-12-11T03:47:56.727Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Upload Malicious Design with Filename Injection

## Summary

This procedure bypasses GitLab's filename sanitization by modifying the Content-Disposition header during design upload, injecting quotes and attributes for later XSS exploitation.

## Description

GitLab uses CarrierWave for file uploads, but the filename*=ASCII-8BIT'' syntax allows bypassing sanitization, enabling special characters like quotes in filenames. This sets up attribute injection in markdown links.

## Requirements

1. Intercepting proxy like [[tools/Burp-Suite]]
2. Existing GitLab issue for upload
3. File to upload (e.g., .png)

## Defense

Defensive measures and detection strategies:

- Strengthen filename validation in upload endpoints
- Monitor for anomalous Content-Disposition headers

## Objectives

1. Upload design with injected filename
2. Enable attribute breakout for XSS
3. Confirm upload via page refresh

## Instructions

### Step 1: Set Up Proxy

**Context**: Configure Burp Suite to intercept upload requests.

Launch [[tools/Burp-Suite]] and set it as the browser proxy.

### Step 2: Initiate Upload and Modify Request

**Context**: Upload a design and edit the header in the intercepted request.

Attempt upload, intercept in Burp, change header to: Content-Disposition: form-data; name="1"; filename*=ASCII-8BIT''bbb%22class%3D%22gfm%22a%3D%27.png.

### Step 3: Refresh and Verify

**Context**: Reload the page to confirm the crafted filename.

Refresh the issue page to see the design named bbb"class="gfm"a='.png.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- upload-bypass
- xss
