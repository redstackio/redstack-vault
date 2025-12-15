---
tags:
  - clickjacking
  - html-creation
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.447Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: 1afe8674-c639-4876-a8df-af543b1a7f11
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-HTML-File-for-Clickjacking

## Summary

This procedure initiates a clickjacking attack by creating a basic HTML file that will host the malicious iframe and overlay elements targeting nextcloud.com.

## Description

In a clickjacking scenario, the attacker prepares a local HTML document to embed the vulnerable site (nextcloud.com) in an iframe. Due to the missing X-Frame-Options header, the site can be framed from any domain. This step focuses on setting up the file structure, which is then populated in subsequent steps. The target environment is any web browser, and the outcome is a ready-to-edit HTML file for the attack demonstration.

## Requirements

1. Access to a text editor (e.g., Notepad on Windows, TextEdit on macOS, or VS Code)
2. Local file system write permissions
3. Basic knowledge of HTML file creation

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with frame-ancestors directive to restrict framing
- Regularly audit HTTP headers for X-Frame-Options presence
- Monitor web server logs for unusual iframe embedding attempts

## Objectives

1. Establish the foundation for the clickjacking payload
2. Ensure the file is locally accessible for editing
3. Prepare for embedding the vulnerable site without errors

## Instructions

### Step 1: Open Text Editor and Create File

**Context**: Launch a text editor to generate the initial HTML document, which will act as the malicious page.

Save the file as "clickjack.html" with the following basic structure:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Demo</title>
</head>
<body>
    <!-- Payload will be inserted here -->
</body>
</html>
```

> This creates an empty HTML skeleton. Verify the file is saved correctly by reopening it in the editor.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web]]
