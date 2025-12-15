---
tags:
  - csrf
  - exploit
  - upload
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.901Z'
sub_techniques: []
id: c6d8aae6-3554-4820-b9fd-52c26c5bcaaf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-Profile-Picture-Upload

## Summary

This procedure demonstrates the CSRF exploit by loading malicious HTML pages in a victim's browser, resulting in unauthorized profile picture changes.

## Description

In the TopCoder wiki scenario, the victim visits the attacker's hosted HTML pages while logged in, triggering automatic POST requests to upload and save a malicious image. This impacts privacy and enables social engineering. Prerequisites: Victim's authenticated session and delivery mechanism (e.g., email link). Outcomes: Profile integrity compromised without user awareness.

## Requirements

1. Hosted HTML files (csrf_upload.html and csrf_save.html)
2. Victim logged into TopCoder
3. Delivery vector (e.g., phishing site)

## Defense

Defensive measures and detection strategies:

- Double-submit CSRF cookies
- Content Security Policy to block inline scripts
- User education on suspicious links

## Objectives

1. Upload arbitrary image via CSRF
2. Save changes to victim's profile
3. Verify impact through observation

## Instructions

### Step 1: Deliver and Load Upload Page

**Context**: Trick victim into loading the upload HTML.

Send a link to csrf_upload.html (e.g., via email). When visited, the page auto-submits the form to https://apps.topcoder.com/wiki/users/editmyprofilepicture.action.

> Expected: Image uploads temporarily; check network tab for 200 OK response.

### Step 2: Load Save Page

**Context**: Immediately follow with save action.

Redirect or link to csrf_save.html, which submits to doeditmyprofilepicture.action.

> Expected: Profile picture updates; verify by viewing victim's profile.

### Step 3: Validate Exploitation

**Context**: Confirm the attack success.

Record a video or screenshot showing the profile change before/after page loads.

> Success: Malicious image set as profile picture.

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
- [[exploit]]
- [[upload]]
