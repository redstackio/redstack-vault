---
id: proc-uber-upload-001
tags:
  - file-upload
  - xss-injection
  - uber-eats
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
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:49.540Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-HTML-or-SVG-File

## Summary

This procedure exploits the unrestricted file upload in Uber Eats menu addition by submitting an HTML or SVG file containing JavaScript, enabling stored XSS.

## Description

The upload endpoint in the onboarding menu feature does not validate file types or content, accepting HTML/SVG files. These are stored and later served inline, allowing embedded scripts to execute when viewed. A simple payload like `<script>alert('XSS')</script>` demonstrates the issue, but real attacks could steal sessions.

## Requirements

1. Access to menu addition upload form
2. Prepared malicious file (e.g., test.html with XSS payload)
3. Browser developer tools for inspection if needed

## Defense

Defensive measures and detection strategies:

- Enforce file type whitelisting (e.g., only JPG, PNG)
- Scan uploads for executable content like <script> tags
- Serve uploaded files with Content-Disposition: attachment to prevent inline rendering

## Objectives

1. Inject malicious JavaScript via file upload
2. Store the payload on the server without detection
3. Enable execution upon file access

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create a file with embedded XSS payload.

Use a text editor to make test.html: `<!DOCTYPE html><html><body><script>alert('XSS')</script></body></html>`. Save as .html or embed in .svg.

### Step 2: Submit Upload

**Context**: Use the form to bypass restrictions.

In the menu addition interface, select the file upload option and choose the prepared file. Submit without any type checks blocking it.

> Upload succeeds, and the file is stored, often with a URL for later access.

### Step 3: Confirm Storage

**Context**: Verify the file is persisted.

Check the menu preview or file list for the uploaded item; it should appear without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[xss-injection]]
- [[uber-eats]]
