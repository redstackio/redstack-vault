---
id: proc-dnd-shortcut-brave-001
name: Drag-and-Drop-Malicious-Shortcut-to-Brave
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.771Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
tags:
  - dnd-exploit
  - uxss
platforms:
  - macOS
  - Browser
tools: []
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Client Execution]]'
---

# Drag-and-Drop-Malicious-Shortcut-to-Brave

## Summary

This procedure crafts and drags a .webloc shortcut file pointing to a chrome://brave URL (e.g., chrome://brave/etc/passwd) onto a Brave tab, bypassing origin validation and loading MITM-injected malicious HTML in the privileged context.

## Description

The vulnerability stems from Chromium handling DnD of shortcuts at a low level, allowing blocked URLs without checks. The .webloc XML points to the malicious URL; upon DnD, it navigates to chrome://brave, intercepted by MITM to serve exploit HTML. This achieves UXSS for local file access. Prerequisites: Crafted file and running browser/MITM.

## Requirements

1. Crafted .webloc file (XML with <string>chrome://brave/etc/passwd</string>)
2. Active Brave tab and MITM server

## Defense

Defensive measures and detection strategies:

- Patch Brave/Chromium to validate DnD URLs
- Disable DnD in browser policies or extensions
- Monitor file creation of .webloc/.desktop files

## Objectives

1. Trigger navigation to privileged origin
2. Load malicious content via MITM
3. Enable subsequent exploitation

## Instructions

### Step 1: Create Shortcut File

**Context**: Generate .webloc with malicious URL.

Manual creation or script:
```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>URL</key><string>chrome://brave/etc/passwd</string></dict></plist>' > exploit.webloc
```

> Expected output: File created.

### Step 2: Perform DnD

**Context**: Drag file to browser tab.

Drag exploit.webloc from Finder to Brave tab.

> Expected output: Navigation occurs, MITM injects HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dnd-exploit
- uxss
