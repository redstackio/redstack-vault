---
tags:
  - clickjacking
  - screenshot
  - evidence
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
updated_at: '2025-12-14T17:28:04.332Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7a0eb458-6531-4342-bde6-3fdc785c1d48
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Capture-Clickjacking-Demonstration-Screenshot

## Summary

This procedure captures a screenshot to visually prove a clickjacking vulnerability, showing the target page embedded in an iframe with overlaid malicious UI elements, useful for vulnerability reporting or documentation.

## Description

After creating a clickjacking PoC, this step documents the exploit by screenshotting the browser view where the iframed content (e.g., Yelp homepage) is overlaid with fake buttons. This confirms the lack of protections and highlights potential impacts like unintended user actions on profile deletions. It applies to web environments and requires no advanced tools, focusing on evidence collection for low-risk demonstrations.

## Requirements

1. Loaded clickjacking PoC in a web browser
2. Built-in screenshot capability (e.g., OS print screen)
3. Image viewer or editor to save the capture

## Defense

Defensive measures and detection strategies:

- Use browser developer tools to inspect for unexpected iframes
- Deploy client-side protections like NoScript extensions
- Log and alert on anomalous embedding attempts in server access logs

## Objectives

1. Visually capture the iframe overlay setup
2. Provide evidence of successful embedding
3. Support vulnerability validation and reporting

## Instructions

### Step 1: Prepare the PoC View

**Context**: Adjust the PoC to clearly show the vulnerability for capture.

In the browser with `clickjack.html` open, modify the iframe style inline (via developer tools) to set opacity to 0.3 for visibility, and ensure the fake button aligns over a target element like a search or profile button on Yelp.

> This makes the overlay evident in the screenshot without fully hiding the content.

### Step 2: Take and Save the Screenshot

**Context**: Capture the full browser window or relevant section.

Use your system's screenshot tool: On Windows, press Win+Shift+S; on macOS, Command+Shift+4. Select the area showing the iframed Yelp page and overlay, then save as `yelp_clickjacking.png`.

> Expected output: A clear image file demonstrating the embedded content and malicious overlay, ready for attachment in reports.

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
- [[documentation]]
