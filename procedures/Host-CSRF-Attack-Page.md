---
tags:
  - csrf
  - hosting
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:57.376Z'
sub_techniques: []
id: 63bbf640-1156-4c9d-8d6a-a62602ce7b76
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-CSRF-Attack-Page

## Summary

This procedure involves saving and uploading the prepared HTML file to an attacker-controlled server, making the CSRF payload publicly accessible via a URL for distribution to victims.

## Description

Hosting ensures the malicious page can be delivered cross-origin, exploiting the browser's same-origin policy relaxation for user-initiated actions like clicks. For Lichess, this allows the GET request to be sent from the attacker's domain while using the victim's authenticated session cookies.

## Requirements

1. Access to a web hosting service (free options like GitHub Pages or Netlify)
2. The prepared HTML file from prior procedure
3. Basic file upload knowledge

## Defense

Defensive measures and detection strategies:

- Educate users on phishing links
- Implement referrer checks or strict CSP
- Log and alert on unusual external referrers to sensitive endpoints

## Objectives

1. Deploy the HTML to a public endpoint
2. Obtain a shareable URL
3. Verify accessibility without restrictions

## Instructions

### Step 1: Save the File

**Context**: Prepare the file for upload by naming it appropriately.

Save the HTML as attack.html or csrf.html on your local machine.

### Step 2: Upload to Hosting Service

**Context**: Use a hosting platform to serve the static file.

For example, on GitHub Pages:
1. Create a new repository.
2. Upload the HTML file to the root.
3. Enable Pages in settings.
4. Access via https://username.github.io/repo/csrf.html.

Test by visiting the URL in an incognito browser; confirm the page loads and link is present.

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
- [[hosting]]
