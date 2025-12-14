---
id: proc-access-malicious-html-brave-dos
tags:
  - dos
  - browser
  - html
  - delivery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:26:30.442Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Access-Malicious-HTML-for-Brave-DoS

## Summary

This procedure involves delivering a malicious HTML file to the target user, which contains JavaScript code for triggering a DoS in Brave browser. It relies on social engineering or direct access to load the file.

## Description

The attack begins by hosting an HTML file on a web server (e.g., http://www.tiks.host-ed.me/pop up dos.html) or providing it as an attachment. When opened in Brave browser (version 0.11.6), the file executes JavaScript that sets up recursive popups. This step focuses on the initial access vector, exploiting user interaction to load the content. Expected outcome is the page rendering and script initialization without immediate detection.

## Requirements

1. Access to a web server or file sharing method to host/deliver the HTML
2. Target using Brave browser on Linux or Windows
3. No special privileges; user must voluntarily open the file or visit the URL

## Defense

Defensive measures and detection strategies:

- Educate users on avoiding suspicious links or attachments
- Browser extensions like popup blockers or script filters
- Monitor for unusual web traffic to unknown hosts

## Objectives

1. Load the malicious HTML into the victim's Brave browser
2. Initiate JavaScript execution for subsequent DoS
3. Achieve initial access without authentication

## Instructions

### Step 1: Prepare and Host the Malicious HTML

**Context**: Create or obtain the HTML file with embedded JavaScript for popup recursion and make it accessible.

No command required; manually save or upload the file to a server.

> The file should include <script> tags with location.reload() logic. Expected output: File hosted at a URL like http://example.com/pop up dos.html.

### Step 2: Direct Target to Access the Content

**Context**: Trick the user into visiting the URL or opening the file in Brave.

No command; use phishing email or direct link.

> Upon opening, the page loads. Expected output: Browser navigates to the page and begins script execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- browser
- html
