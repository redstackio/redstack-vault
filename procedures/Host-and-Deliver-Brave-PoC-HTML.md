---
id: proc-uuid-1
tags:
  - poc-delivery
  - social-engineering
  - brave-browser
type: procedure
tools:
  - '[[tools/Generic-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Microsoft Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:23:31.277Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Host-and-Deliver-Brave-PoC-HTML

## Summary

This procedure involves hosting a malicious HTML PoC file on a web server and delivering it to the target via social engineering, instructing them to save and open it locally in Brave browser to initiate the scheme bypass attack.

## Description

The PoC HTML contains JavaScript that opens a popup with an anchor tag pointing to 'chrome://brave'. When opened locally, it tricks the user into interacting with the UI to bypass restrictions. This targets Brave on Windows, relying on user download and local file opening. Prerequisites include a web server for hosting and target susceptibility to instructions.

## Requirements

1. Access to a web server for hosting the HTML file
2. Social engineering channel (e.g., email, chat) to instruct target
3. Target running Brave browser on Windows with local file execution enabled

## Defense

Defensive measures and detection strategies:

- Educate users on risks of opening unknown HTML files
- Browser sandboxing and local file policies to block malicious popups
- Network monitoring for suspicious HTML downloads from unknown sources

## Objectives

1. Deliver PoC to target and ensure local opening
2. Trigger initial UI interaction for scheme bypass setup
3. Position for subsequent exploitation steps

## Instructions

### Step 1: Create and Host PoC HTML

**Context**: Prepare the malicious HTML file with popup logic and upload to server.

**Instructions**: Create braveRCE.html with content including <script> to open window with <a href="chrome://brave"> link </a>. Use [[tools/Generic-Web-Server]] to serve it.

No specific command; manual file creation and upload.

> Expected: File accessible via URL, e.g., http://attacker.com/braveRCE.html.

### Step 2: Instruct Target to Download and Open

**Context**: Use social engineering to get target to save and launch the file in Brave.

**Instructions**: Send link with instructions: "Download this HTML and open in Brave from your desktop."

> Expected: Target confirms opening; popup appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Generic-Web-Server]]

## Tags

- [[poc-delivery]]
- [[social-engineering]]
