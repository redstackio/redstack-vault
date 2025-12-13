---
tags:
  - xss
  - file-upload
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c3e04c94-46d1-4b17-97c6-0922aaf1b076
created_at: '2025-12-13T09:00:33.873Z'
updated_at: '2025-12-13T09:00:33.873Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Bypass File Type Restrictions for Stored XSS via HTML Upload

## Summary

This procedure bypasses file type restrictions on the photo upload feature to upload HTML files containing malicious scripts, resulting in stored XSS that can spoof users or steal cookies.

## Description

The vulnerability exists in the upload endpoint where parameters can be modified to allow HTML files. By intercepting requests with Burp Suite, attackers change the allowed file types and extensions, enabling the upload of HTML with embedded JavaScript. The uploaded file is stored and can be accessed, executing the script in the context of the viewer.

## Requirements

1. Valid user account on https://ecjobs.starbucks.com.cn
2. Burp Suite for request interception
3. Network access to the target site

## Defense

Defensive measures and detection strategies:

- Implement strict file type validation and content-type checking on the server-side
- Use content security policy (CSP) to prevent XSS execution
- Monitor upload requests for unusual parameter modifications

## Objectives

1. Upload malicious HTML for stored XSS
2. Enable cookie theft or user spoofing
3. Confirm execution via access to uploaded file

## Instructions

### Step 1: Navigate to Upload Page

**Context**: Log in and access the personal information settings to initiate photo upload.

Access https://ecjobs.starbucks.com.cn and navigate to the upload feature.

> This sets up the initial request for interception.

### Step 2: Intercept and Modify Upload Request

**Context**: Use Burp Suite to capture and alter the request to bypass restrictions.

Intercept the HTTPS upload request with [[tools/Burp-Suite]]. Add 'html;' to 'allow_file_type_list' or delete it, and change filename suffix to '.html'.

> The modified request allows HTML upload, leading to stored XSS when accessed.

### Step 3: Access Uploaded File

**Context**: Verify the upload by visiting the file URL.

Visit the URL like https://ecjobs.starbucks.com.cn/retail/tempfiles/temp_uploaded_641dee35-5a62-478e-90d7-f5558a78c60e.html.

> Scripts in the HTML execute, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- file-upload
- bypass
