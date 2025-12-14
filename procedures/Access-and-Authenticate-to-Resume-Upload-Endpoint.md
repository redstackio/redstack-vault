---
id: proc-001
tags:
  - authentication
  - initial-access
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:22.969Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-and-Authenticate-to-Resume-Upload-Endpoint

## Summary

This procedure authenticates a user to the Starbucks job portal and navigates to the resume upload functionality, establishing a session necessary for exploiting the file upload vulnerability.

## Description

The attack begins with legitimate user authentication to ecjobs.starbucks.com.cn, followed by navigation to the resume or avatar upload section. This step ensures the attacker has a valid session cookie for subsequent intercepted requests. The target environment is a public-facing ASP.NET web application on Windows, where the upload endpoint lacks robust validation.

## Requirements

1. Valid login credentials for the job portal
2. Web browser or proxy tool like Burp Suite for session management
3. Network access to https://ecjobs.starbucks.com.cn

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for user logins
- Monitor for unusual session activity or rapid navigation to upload endpoints
- Rate-limit login attempts and upload submissions

## Objectives

1. Establish authenticated session
2. Reach the vulnerable upload endpoint
3. Prepare for request interception

## Instructions

### Step 1: Sign In to the Portal

**Context**: Use provided credentials to authenticate and gain access to user features.

No specific command; perform via web browser: Visit https://ecjobs.starbucks.com.cn, enter username and password, and submit the login form.

> Successful login redirects to the user dashboard with session cookies set (e.g., ASP.NET_SessionId).

### Step 2: Navigate to Resume Upload

**Context**: Direct to the section allowing file uploads for resumes or avatars.

No specific command; click through the UI to the resume management or profile update page containing the upload form.

> The upload endpoint is prepared, typically a POST to /recruitjob/upload or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication]]
- [[initial-access]]
