---
tags:
  - file-upload
  - xss
  - stored-xss
  - sharepoint
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9d398142-7d72-44c1-bc66-91c321644a2a
created_at: '2025-12-13T23:56:19.967Z'
updated_at: '2025-12-13T23:56:19.967Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---
# Create-Blog-Post-and-Upload-Malicious-File

## Summary

This procedure demonstrates creating a blog post on a SharePoint site and uploading a malicious HTML or SVG file containing JavaScript to exploit stored XSS, embedding the payload for execution when viewed.

## Description

Targeted at SharePoint blog features, this involves navigating to the user's personal blog, initiating a post, and using the body insert functionality to upload files without proper sanitization. The root cause is the lack of validation for embedded scripts in HTML/SVG, allowing storage and rendering of malicious content. Prerequisites include an authenticated session; outcomes include the payload being stored and ready for triggering, potentially affecting all viewers.

## Requirements

1. Authenticated user account with blog access
2. Malicious file prepared (e.g., mygf.html with <script>alert('XSS')</script> or SVG with javascript:alert('XSS'))
3. Web browser for interactions

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all uploaded files, stripping executable scripts from HTML/SVG
- Use content security policy (CSP) to block inline JavaScript
- Scan uploads for known XSS patterns and quarantine suspicious files

## Objectives

1. Embed JavaScript payload in a stored blog post
2. Bypass file upload filters to store malicious content
3. Set up conditions for XSS execution on preview or view

## Instructions

### Step 1: Navigate to Personal Blog and Start Post

**Context**: Access the blog creation interface to prepare for file insertion.

Log in and go to https://██████████/Profiles/My/#Your Username#/Blog/default.aspx, then click the 'Create a Post' button.

> This opens the post editor, where the body textarea is available for content addition.

### Step 2: Insert and Upload Malicious File

**Context**: Use the upload feature to embed the payload into the post body.

Click on the 'Body' textarea, then the 'Insert' button, followed by 'Upload File'. Select the malicious file (e.g., mygf.html or evilsvgfile.svg containing <script>alert('XSS')</script>).

> The file uploads and embeds as an object or link in the post, storing the payload server-side.

### Step 3: Confirm Upload

**Context**: Finalize the embedding to ensure the file is processed.

Click 'Ok' and wait for the upload to complete and the file to appear embedded in the editor.

> No errors indicate successful storage; the post now contains the exploitable content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[xss]]
- [[stored-xss]]
- [[Sharepoint]]
