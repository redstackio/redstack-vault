---
id: proc-uuid-3
tags:
  - gatekeeper-bypass
  - quarantine-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:24:08.121Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Bypass-macOS-Gatekeeper-and-Quarantine-Checks

## Summary

This procedure exploits Slack's failure to apply the com.apple.quarantine extended attribute to downloaded files, allowing malicious executables like .terminal to run without macOS security prompts or scans.

## Description

macOS Gatekeeper and Quarantine protect against unsigned or downloaded executables by displaying warnings and blocking launches. However, Slack for macOS (direct download) downloads files without setting the quarantine xattr, treating them as local. When a .terminal file is opened, no checks occur, enabling silent execution. This affects environments with strict policies (e.g., 'App Store only'). The vulnerability is in Slack's download handler; expected outcome is unhindered file execution.

## Requirements

1. Slack version without quarantine support (e.g., direct download 3.3.3)
2. macOS with Gatekeeper enabled
3. Downloaded file must be .terminal or similar executable type

## Defense

Defensive measures and detection strategies:

- Update Slack to versions that apply quarantine attributes (if patched)
- Use xattr command to manually inspect files: xattr -l filename.terminal
- Deploy EDR tools to alert on missing quarantine flags on executables

## Objectives

1. Evade origin-based security checks for downloaded content
2. Prevent user warnings that could abort execution
3. Enable running in hardened Gatekeeper configurations

## Instructions

### Step 1: Verify Missing Quarantine Attribute

**Context**: Confirm the bypass condition post-download.

On the victim's system (or test), run:

```bash
xattr -l downloaded.terminal
```

> Expected: No com.apple.quarantine output, confirming bypass.

### Step 2: Attempt Launch Without Prompts

**Context**: Open the file to test evasion.

Double-click the file; observe no Gatekeeper dialog.

> Success if Terminal launches directly without 'Are you sure?' warning.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used

- [[commands/xattr-inspect-quarantine]]

## Tools Used


## Tags

- [[gatekeeper-bypass]]
- [[quarantine-bypass]]
