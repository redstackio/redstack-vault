---
tags:
  - web-access
  - upload-feature
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
updated_at: '2025-12-14T17:24:17.746Z'
sub_techniques: []
id: 62c71b79-86e4-416b-ae8f-a2cdc7d49225
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Semrush Report Constructor Logo Upload

## Summary

This procedure navigates to the Semrush report constructor page to access the vulnerable logo upload feature, setting the stage for exploiting ImageTragick.

## Description

The Semrush report constructor at https://www.semrush.com/my_reports/constructor includes a logo upload input that processes images with ImageMagick, which is vulnerable to ImageTragick if unpatched. This step requires a valid Semrush account for authenticated access. Successful navigation exposes the upload endpoint for subsequent payload delivery.

## Requirements

1. Valid Semrush account credentials
2. Web browser with internet access
3. No prior server access needed

## Defense

Defensive measures and detection strategies:

- Implement account access logging and monitor for unusual navigation to report features
- Use web application firewall (WAF) to inspect upload attempts

## Objectives

1. Gain access to the logo upload interface
2. Prepare for file upload exploitation
3. Confirm feature availability

## Instructions

### Step 1: Log In to Semrush

**Context**: Authenticate to access protected features.

Log in using your Semrush credentials at https://www.semrush.com.

### Step 2: Navigate to Report Constructor

**Context**: Locate the vulnerable upload endpoint.

Navigate to https://www.semrush.com/my_reports/constructor and identify the logo upload input field.

**Expected Output**: Upload form visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- upload-feature
