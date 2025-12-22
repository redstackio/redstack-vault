---
tags:
  - web
  - upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:25.270Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7aeb0a00-1d99-4433-836c-fb101250d781
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Header-Image-Upload-Function

## Summary

This procedure involves navigating to the header image upload endpoint in the Booth.pm design edit page to initiate the file upload process, setting the stage for subsequent exploitation.

## Description

In the context of the Booth.pm application, the header image upload is handled at https://manage.booth.pm/design/edit. Attackers with authenticated access can reach this page to select and submit files. This step ensures the target endpoint is accessible and the upload form is functional, which is a prerequisite for manipulating requests in later steps. The expected outcome is readiness to submit a crafted file without immediate blocks.

## Requirements

1. Valid authenticated session to Booth.pm management panel
2. Web browser or HTTP client like curl
3. Network connectivity to https://manage.booth.pm

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on upload endpoints
- Require CAPTCHA or additional auth for design edits
- Monitor access logs for unusual navigation patterns to edit pages

## Objectives

1. Gain access to the vulnerable upload interface
2. Verify the endpoint is reachable and functional
3. Prepare for header manipulation in the upload request

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the application and reach the design edit page to expose the upload function.

**Command** ([[commands/curl-upload-access]]):
```bash
curl -X GET https://manage.booth.pm/design/edit -H "Cookie: session=your_session_cookie" -v
```

> This command fetches the edit page using your session cookie. Expected output includes HTML with the upload form; check for status 200 and presence of file input elements.

### Step 2: Inspect Upload Form

**Context**: Use browser dev tools to identify the upload form action and fields.

**Instructions**: Open the page in a browser, inspect the <form> element for enctype and action URL. Note the file input name, typically 'header_image'.

> No command needed; manual inspection confirms the form supports multipart uploads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-access]]

## Tools Used


## Tags

- [[web]]
- [[upload]]
