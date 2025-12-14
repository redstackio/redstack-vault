---
id: p-upload-svg-xss
tags:
  - stored-xss
  - svg-upload
  - nextcloud
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:13.199Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---
# Upload-Malicious-SVG-for-Stored-XSS

## Summary

This procedure leverages the unrestricted file upload in Nextcloud Contacts to store a malicious SVG file with embedded JavaScript, enabling persistent stored XSS attacks on users viewing the contact.

## Description

SVG files are accepted as images without sanitization of embedded scripts, allowing JavaScript payloads to be stored server-side. When rendered, the script executes in the viewer's browser. This targets authenticated users in the web app, with potential for data theft or further exploitation.

## Requirements

1. Active Nextcloud session with Contacts access
2. Malicious SVG file prepared (e.g., evilsvgfile.svg with <script>alert('XSS')</script>)
3. Basic knowledge of crafting SVG payloads

## Defense

Defensive measures and detection strategies:

- Sanitize SVG uploads by stripping or blocking script tags
- Use Content Security Policy (CSP) to restrict inline scripts
- Validate and parse file contents before storage

## Objectives

1. Store XSS payload via SVG upload
2. Persist the vulnerability in contact data
3. Enable execution on image interaction

## Instructions

### Step 1: Prepare Malicious SVG

**Context**: Create an SVG file containing executable JavaScript.

**Instructions**: Use a text editor to craft evilsvgfile.svg with content like: <svg><script>alert('XSS Triggered')</script></svg>.

> Save as .svg and ensure it's valid XML.

### Step 2: Upload to Contact Image

**Context**: Use the same upload mechanism as for images to store the payload.

**Instructions**: Edit a contact, open the image upload popup, select evilsvgfile.svg, and upload.

> The file is accepted and set as the contact image without script removal.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[nextcloud]]
