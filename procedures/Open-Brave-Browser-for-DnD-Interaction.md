---
id: proc-open-brave-dnd-001
name: Open-Brave-Browser-for-DnD-Interaction
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.785Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploitation for Client Execution]]'
tags:
  - browser-setup
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
  - '[[Exploitation for Client Execution]]'
---

# Open-Brave-Browser-for-DnD-Interaction

## Summary

This procedure launches the Brave browser and loads a benign page to create an active tab ready for drag-and-drop interaction, setting the stage for the shortcut file exploit.

## Description

Brave (0.24.0) must be running with a loaded page for DnD to trigger navigation. This step ensures the browser is in a state where Chromium-level handling of .webloc files can bypass restrictions. No special flags needed; expected outcome is a responsive tab for subsequent DnD.

## Requirements

1. Brave 0.24.0 installed on macOS
2. MITM server running from prior procedure

## Defense

Defensive measures and detection strategies:

- Disable or sandbox browser processes with AppArmor/SELinux
- Monitor for unusual browser launches via process auditing

## Objectives

1. Establish browser session for user interaction
2. Prepare tab for DnD vulnerability trigger

## Instructions

### Step 1: Launch Brave

**Context**: Open the browser application.

Launch via command line or GUI:
```bash
open -a "Brave Browser"
```

> Expected output: Browser window opens.

### Step 2: Load Benign Page

**Context**: Navigate to a standard site to activate the tab.

In address bar: `https://www.google.com`

> Expected output: Page loads without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- browser-setup
