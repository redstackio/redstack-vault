---
id: proc-crowdsignal-quiz-setup-001
tags:
  - xss
  - quiz-creation
  - photo-upload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:55.463Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Crowdsignal-Quiz-and-Upload-Image

## Summary

This procedure sets up a new quiz on Crowdsignal and uploads an image to prepare the environment for exploiting the stored XSS vulnerability in the media_code parameter during the save process.

## Description

In the context of testing for stored XSS in Crowdsignal's Photo Insert App, this step involves navigating to the dashboard, creating a quiz, adding a multiple-choice element, and uploading a benign image. This action generates the save request containing the vulnerable media_code parameter, which can later be intercepted and modified. The target environment is the web-based quiz editor at https://app.crowdsignal.com, requiring an authenticated user session. Expected outcomes include a quiz ready for payload injection, with no execution at this stage.

## Requirements

1. Authenticated access to https://app.crowdsignal.com/dashboard
2. A test image file for upload
3. Web browser with proxy support for subsequent interception

## Defense

Defensive measures and detection strategies:

- Implement client-side input validation on upload forms
- Monitor for unusual image upload patterns in quiz creation logs
- Use Content Security Policy (CSP) to restrict inline script execution

## Objectives

1. Establish the quiz creation context to access the vulnerable save endpoint
2. Trigger the image upload to populate the media_code parameter
3. Prepare for request interception without alerting defenses

## Instructions

### Step 1: Access Dashboard and Create Quiz

**Context**: Log in and initiate a new quiz to enter the editor where elements can be added.

No command required; use the web interface:

- Navigate to https://app.crowdsignal.com/dashboard
- Select "Create a New > Quiz"

> This opens the quiz editor. Expected output: Blank quiz canvas ready for elements.

### Step 2: Add Multiple Choice and Upload Image

**Context**: Add a question type that supports images and perform the upload to generate the save request payload.

No command required; use the web interface:

- In the quiz editor, add "Multiple Choice" to the page
- Click the image button in the element
- Select and upload a photo file
- Click "Upload"

> Expected output: Image appears in the element, and the media_code (photo ID) is set for the impending save request.

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

- [[xss]]
- [[quiz-creation]]
