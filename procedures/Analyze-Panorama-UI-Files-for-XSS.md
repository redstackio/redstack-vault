---
id: proc-csgo-ui-analysis-001
tags:
  - recon
  - xss
  - csgo
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Windows
  - Game
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:14.883Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze Panorama UI Files for XSS

## Summary

This procedure involves extracting and statically analyzing CS:GO's Panorama UI files to identify vulnerabilities like unsanitized HTML parsing, enabling the discovery of XSS entry points in popups.

## Description

In the CS:GO installation, the Panorama UI framework uses XML layout files bundled in code.pbin. By unzipping this archive and searching for attributes like html='true', attackers can pinpoint components that parse raw HTML without sanitization, such as the disconnect/kick popup in popup_generic.xml. This sets the stage for injecting payloads that execute JavaScript in the client's browser context, potentially calling Steam APIs for RCE.

## Requirements

1. Local CS:GO installation (Steamapps\common\Counter-Strike Global Offensive\csgo\panorama\code.pbin)
2. Unzipping tool (e.g., 7-Zip)
3. Grep or text search capability

## Defense

Defensive measures and detection strategies:

- Valve to sanitize all UI inputs
- Monitor for unusual file extractions in game directories
- Client-side input validation updates

## Objectives

1. Identify vulnerable UI components
2. Confirm raw HTML parsing risks
3. Prepare for payload testing

## Instructions

### Step 1: Extract Panorama Files

**Context**: Unpack the bundled UI code to access XML layouts.

No specific command; use file explorer or 7-Zip to unzip steamapps\common\Counter-Strike Global Offensive\csgo\panorama\code.pbin into a directory.

> Expected output: Extracted XML files including layout\popups\popup_generic.xml.

### Step 2: Search for Vulnerable Attributes

**Context**: Scan files for html='true' to find parsing points.

Use grep in the extracted directory:

```bash
grep -r "html='true'" .
```

> This reveals Label tags in popup_generic.xml that enable unsanitized HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- xss
- csgo
