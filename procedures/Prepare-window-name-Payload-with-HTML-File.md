---
id: proc-window-name-payload-001
tags:
  - xss
  - payload
  - html
  - window-name
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.342Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-window-name-Payload-with-HTML-File

## Summary

This procedure creates an external HTML file that sets the window.name property to a JavaScript payload, which is then evaluated by the injected SVG onload in the Vimeo thumbnail, enabling XSS without direct script injection.

## Description

The payload leverages the window.name property, which persists across iframe loads, to store executable JS like 'prompt(document.domain,document.cookie)'. The HTML file embeds the Vimeo player iframe, setting the name before loading, so when the video ends and the thumbnail renders the unescaped username, the SVG triggers eval(name), executing the payload. This bypasses typical XSS filters by using an indirect vector.

## Requirements

1. Text editor (e.g., Notepad, VS Code).
2. Attacker's Vimeo video URL.
3. Web browser for testing.

## Defense

Defensive measures and detection strategies:

- Escape or strip SVG/HTML from usernames.
- Disable or sanitize window.name usage in iframes.
- Implement strict CSP to block eval() and prompts.
- Log and alert on cross-origin iframe loads with suspicious names.

## Objectives

1. Store JS payload in window.name for indirect execution.
2. Embed Vimeo player to simulate victim view.
3. Trigger payload via thumbnail without interaction.

## Instructions

### Step 1: Create HTML File Structure

**Context**: Build the base HTML to set window.name.

Open a text editor and start with: `<html><body><script>window.name = 'prompt(document.domain,document.cookie)';</script>`.

### Step 2: Embed Iframe for Player

**Context**: Add iframe to load the malicious video player.

Append: `<iframe src="https://player.vimeo.com/video/YOUR_VIDEO_ID" width="640" height="360" allowfullscreen></iframe>`. Replace YOUR_VIDEO_ID with the actual ID.

### Step 3: Save and Test

**Context**: Save as 'name_xss_iframe.html' and open in browser.

Verify window.name is set and iframe loads without errors.

**Expected Output**: Payload set; iframe displays video.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload]]
