---
tags:
  - phishing
  - url-sharing
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-13T23:55:38.419Z'
sub_techniques: []
id: 6bc3f64d-6aed-4eb6-a039-e44ac843c56b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Share-Malicious-URL-with-Admin

## Summary

This procedure involves distributing the download URL of the uploaded malicious file to the workspace admin, tricking them into visiting it to trigger the XSS payload.

## Description

After uploading the file, the response provides a downloadUrl. Sharing this URL via workspace chat, email, or direct message lures the admin to view the 'image', which renders as HTML and executes JS in their authenticated session, enabling the privilege escalation.

## Requirements

1. Download URL from upload response
2. Access to communication channels in the workspace
3. Admin contact details

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious file shares
- Implement URL scanning for malicious content
- Use preview modes that don't execute JS for file views

## Objectives

1. Deliver the XSS vector to the victim
2. Ensure victim interaction with the malicious file
3. Set stage for JS execution in victim's context

## Instructions

### Step 1: Obtain and Prepare URL

**Context**: Extract the shareable URL from the upload output.

**Instructions**: The Python script prints the URL like https://dust.tt/api/.../downloadUrl?action=view. Copy this.

### Step 2: Distribute to Admin

**Context**: Send the URL to the admin account.

**Instructions**: Use the workspace interface, email, or any channel to share the URL, perhaps with a message like 'Check this uploaded image for the conversation.' Switch to admin account to receive and simulate visit.

**Expected Output**: Admin views the URL in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[Phishing]]
- [[url-sharing]]
