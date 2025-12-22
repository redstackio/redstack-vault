---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - recon
  - web
  - aws
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.211Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Missing CSRF Protection on S3 Upload Endpoint

## Summary

This procedure involves inspecting a web application's file upload functionality integrated with AWS S3 to detect the absence of Cross-Site Request Forgery (CSRF) token validation, allowing potential unauthorized uploads from external sites.

## Description

In the context of Udemy's staging environment, the file upload feature for course assets lacked CSRF protection, enabling attackers to forge requests from malicious webpages. This procedure outlines how to identify such vulnerabilities by analyzing network traffic and testing cross-origin requests. Prerequisites include access to the target web app and basic knowledge of web security testing. Expected outcomes include confirmation of the vulnerability, paving the way for exploitation demonstrations.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools) for network inspection
2. Access to the target web application (e.g., Udemy staging upload feature)
3. Ability to craft simple HTTP requests for testing

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing endpoints, validated server-side
- Use Content Security Policy (CSP) headers to restrict cross-origin form submissions
- Monitor S3 bucket logs for anomalous uploads from unexpected referers

## Objectives

1. Confirm absence of CSRF protection on the S3 upload endpoint
2. Document the endpoint URL and request format for exploitation
3. Assess potential impact on staging storage and processing

## Instructions

### Step 1: Inspect Legitimate Upload Request

**Context**: Perform a normal file upload on the target site to capture the request details and check for CSRF tokens.

Navigate to the upload feature in the web app, select a test file, and submit. Open browser developer tools (F12), go to the Network tab, and filter for the upload POST request. Examine headers and form data for any CSRF-related fields (e.g., _token, csrf_token).

**Expected Output**: Request details showing no CSRF token present, e.g., POST to /upload-s3-staging with multipart/form-data but missing token fields.

### Step 2: Test Cross-Origin Request

**Context**: Simulate a cross-origin request to verify if the endpoint accepts uploads without origin checks.

Use a tool like curl or a simple HTML form on a different domain to send a POST request to the identified endpoint with a test file. Check the response for success (e.g., 200 OK) without authentication or token requirements.

For example, craft a basic test:

```html
<form action="https://staging.udemy.com/upload-s3" method="POST" enctype="multipart/form-data">
  <input type="file" name="file" value="test.txt">
  <input type="submit">
</form>
```

Host this on an external site and attempt submission.

**Expected Output**: Successful upload response, confirming the vulnerability.

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
- [[s3]]
- [[aws]]
- [[web]]
