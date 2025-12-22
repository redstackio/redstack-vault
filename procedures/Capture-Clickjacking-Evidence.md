---
tags:
  - clickjacking
  - evidence
  - screenshot
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
updated_at: '2025-12-14T17:28:12.555Z'
sub_techniques: []
id: 78b3abf0-38d0-47db-b8c3-cb5b77c4881b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Capture-Clickjacking-Evidence

## Summary

This procedure documents the clickjacking vulnerability by capturing screenshots of the loaded PoC, providing visual proof of the embedded iframe and overlaid elements for reporting or analysis.

## Description

Evidence capture is essential for vulnerability disclosure, showing the target site framed with deceptive overlays. Use built-in browser tools or OS screenshot utilities to record the setup. This follows validation and requires no additional setup beyond the PoC; outcomes include images highlighting the attack vector, such as positioned overlays over login areas on sifchain.finance.

## Requirements

1. Screenshot tool (e.g., browser's built-in capture, Snipping Tool on Windows, Command+Shift+4 on macOS)
2. Loaded PoC in browser from previous steps
3. Image viewer or editor for annotation

## Defense

Defensive measures and detection strategies:

- Regularly audit HTTP headers with tools like curl or browser inspectors
- Log and alert on anomalous embedding attempts via server access logs
- Use vulnerability scanners (e.g., Nuclei) with clickjacking templates for automated detection
- Train developers on secure header implementation best practices

## Objectives

1. Visually document the successful iframe embedding
2. Highlight overlay positions for impact demonstration
3. Prepare evidence for vulnerability reports

## Instructions

### Step 1: Prepare PoC for Capture

**Context**: Ensure the PoC is loaded and overlays are visible to capture the full attack setup.

Navigate to the PoC in the browser and resize the window to show the embedded site clearly. Use developer tools to inspect and adjust overlay positions if needed.

> Verify no frame errors in console; the site should appear framed with transparent elements overlaid.

### Step 2: Take and Annotate Screenshot

**Context**: Capture the screen and add annotations to emphasize the vulnerability.

Use your OS screenshot tool to capture the browser window, focusing on the iframe and overlays. Annotate with arrows pointing to the embedded site and fake elements.

> Save as PNG or JPG (e.g., clickjack-evidence.png). The image should clearly show sifchain.finance loaded in the iframe with potential click-trick areas marked.

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
- [[evidence]]
- [[screenshot]]
