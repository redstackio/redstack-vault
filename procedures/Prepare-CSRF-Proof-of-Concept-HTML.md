---
id: proc-002
tags:
  - csrf
  - poc
  - html
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:42.384Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-CSRF-Proof-of-Concept-HTML

## Summary

This procedure involves downloading and modifying a simple HTML file to create a CSRF PoC that forges an image upload request to Chaturbate's unprotected endpoint, targeting a specific photo set ID.

## Description

The PoC exploits the absence of CSRF tokens by using a standard HTML form that submits a POST request with an image file (e.g., blank white PNG) to the upload handler. The form must mimic the legitimate upload parameters, including the set ID, to append the image without victim interaction beyond loading the page.

## Requirements

1. Base PoC HTML file from the report
2. Text editor (e.g., Notepad++ or VS Code)
3. Known photo set ID from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy and CSRF token validation
- Scan for and block cross-origin form submissions
- Log all upload attempts with origin headers

## Objectives

1. Customize the PoC to target the victim's set
2. Ensure the form uploads a detectable payload (e.g., blank image)
3. Test locally for syntax validity

## Instructions

### Step 1: Obtain Base PoC File

**Context**: Acquire the template HTML for the CSRF form.

Download the `poc.html` file containing the basic form structure for Chaturbate upload.

**Expected Output**: HTML file saved locally.

### Step 2: Edit Set ID Parameter

**Context**: Update the form to reference the specific target set.

Open the file in a text editor and replace the placeholder (e.g., 4771110) in the form's hidden input or action URL with the actual set ID.

**Expected Output**: Form now targets `https://chaturbate.com/photo_videos/photoset/detail/[username]/[actual_set_id]/`.

### Step 3: Verify PoC Structure

**Context**: Ensure the form includes necessary fields like image file and submit button.

Review the HTML for POST method, enctype="multipart/form-data", and a blank image attachment.

**Expected Output**: Valid HTML ready for browser execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[poc]]
- [[html]]
