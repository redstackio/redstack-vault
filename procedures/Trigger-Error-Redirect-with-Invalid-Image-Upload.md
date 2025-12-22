---
tags:
  - xss
  - web-vulnerability
  - upload
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:15:31.527Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8c370f47-19a8-4dfc-9c99-fe72c897db86
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Error-Redirect-with-Invalid-Image-Upload

## Summary

This procedure simulates an invalid image upload on urbandictionary.com to trigger a redirect to the vulnerable /cloudinary_cors.html endpoint, setting the stage for XSS exploitation by reflecting an error message in the URL.

## Description

In the context of testing Urban Dictionary's definition upload feature, uploading a non-image file (e.g., a .txt file disguised as .jpg) causes the server to generate an error and redirect to a CORS handling page. The error parameter in this redirect is user-controlled and unsanitized, making it prone to injection attacks. This step requires no special privileges and can be performed by any site visitor attempting to add a definition.

## Requirements

1. Web browser access to urbandictionary.com
2. A non-image file to upload as an invalid image
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Validate file types and MIME types on upload
- Sanitize all reflected parameters in redirects
- Implement Content Security Policy (CSP) to block inline scripts

## Objectives

1. Provoke server-side error handling to expose the vulnerable endpoint
2. Capture the reflected error URL for further analysis
3. Establish initial access vector for XSS injection

## Instructions

### Step 1: Prepare Invalid Image File

**Context**: Create or select a file that will fail image validation, such as a text file renamed to end in .jpg.

No command required; manually prepare the file on your local system.

### Step 2: Attempt Upload on Urban Dictionary

**Context**: Navigate to the site and simulate a definition submission with the invalid attachment to trigger the error.

Use your browser to go to urbandictionary.com, start adding a new definition, attach the invalid file, and submit. The server will reject it and redirect.

**Expected Output**: Automatic redirect to http://www.urbandictionary.com/cloudinary_cors.html?error=Invalid+image+file.

### Step 3: Verify Redirect

**Context**: Confirm the error parameter is present and reflected.

Inspect the browser's address bar or network tab to see the full URL with the error query string.

**Expected Output**: URL contains unsanitized error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[upload]]
