---
id: proc-uuid-2
name: Craft-CSRF-Proof-of-Concept-for-File-Upload
tags:
  - csrf
  - poc
  - file-upload
  - web
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
updated_at: '2025-12-14T17:27:23.052Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-CSRF-Proof-of-Concept-for-File-Upload

## Summary

This procedure creates a malicious HTML file that exploits a CSRF vulnerability to automatically upload a file to a target web endpoint without user interaction.

## Description

Targeting the Topcoder wiki's doattachfile.action endpoint, the PoC uses an auto-submitting HTML form to perform a multipart POST request. When loaded by an authenticated user, it attaches an arbitrary file (e.g., csrf.txt) to a specified wiki page. This demonstrates how lack of CSRF protections allows cross-site actions on behalf of users.

## Requirements

1. Text editor for HTML/JavaScript
2. Sample file to upload (e.g., a text file)
3. Knowledge of the vulnerable endpoint and parameters from reconnaissance

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens in file upload forms
- Validate request origins and referer headers
- Log and alert on uploads from non-wiki origins

## Objectives

1. Build a functional auto-submit form for file upload
2. Ensure compatibility with authenticated sessions
3. Test for silent execution without alerts

## Instructions

### Step 1: Create the HTML Structure

**Context**: Set up the form with target endpoint and parameters.

Write an HTML file with a <form> tag: action="https://apps.topcoder.com/wiki/pages/doattachfile.action", method="POST", enctype="multipart/form-data". Include hidden input for pageId (e.g., <input type="hidden" name="pageId" value="165871793">) and a file input <input type="file" name="file" value="path/to/csrf.txt">

**Expected Output**: Basic form skeleton ready for auto-submit.

### Step 2: Add Auto-Submit JavaScript

**Context**: Trigger form submission on page load to bypass user consent.

Add <script>document.getElementById('csrfForm').submit();</script> after the form, with id="csrfForm" on the form tag. Ensure the file input references the actual file path.

**Expected Output**: HTML that submits immediately upon loading.

### Step 3: Local Validation

**Context**: Test the PoC in a controlled environment.

Open the HTML in a browser while authenticated to the wiki (use incognito if needed). Check network tab for the POST request and wiki for the uploaded file.

**Expected Output**: File attached without manual input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf-poc]]
- [[JavaScript]]
