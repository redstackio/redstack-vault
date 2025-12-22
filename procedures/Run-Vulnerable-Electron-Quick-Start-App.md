---
id: proc-001
tags:
  - electron
  - setup
  - vulnerable-app
type: procedure
tools:
  - '[[tools/Electron]]'
  - '[[tools/electron-quick-start]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Desktop
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:29:36.009Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Run-Vulnerable-Electron-Quick-Start-App

## Summary

This procedure sets up and runs the electron-quick-start sample application using a vulnerable version of Electron, creating an environment where the renderer process can exploit the Web Bluetooth API without proper permission checks.

## Description

The electron-quick-start app provides a minimal Electron application with a renderer process loading a basic HTML page. By using Electron versions prior to the patches (e.g., before 17.0.0-alpha.6), the default configuration fails to enforce Bluetooth permission prompts, allowing subsequent JavaScript execution to access system Bluetooth resources. This is typically run on a local desktop machine with Bluetooth enabled and nearby devices available. Prerequisites include Node.js and Git for cloning the repository.

## Requirements

1. Node.js installed (v12 or later)
2. Git for repository cloning
3. Vulnerable Electron version specified in package.json (e.g., ^13.6.5 or earlier unpatched stable)
4. Local Bluetooth adapter enabled with discoverable devices nearby

## Defense

Defensive measures and detection strategies:

- Update Electron to patched versions (17.0.0-alpha.6+, 16.0.6+, etc.) to enforce permission checks
- Implement custom event handlers for navigator.bluetooth in Electron apps to require user consent
- Monitor renderer process for unauthorized JavaScript execution via developer tools
- Disable Web Bluetooth API in Electron via contextBridge or session permissions

## Objectives

1. Launch a renderer process vulnerable to Bluetooth API bypass
2. Verify the app runs without custom security configurations
3. Prepare for exploitation by confirming Bluetooth API availability

## Instructions

### Step 1: Clone and Prepare the Repository

**Context**: Download the sample app and configure it with a vulnerable Electron version.

**Instructions**: Use Git to clone the repository and edit package.json to pin a vulnerable Electron version.

```bash
git clone https://github.com/electron/electron-quick-start
cd electron-quick-start
npm install electron@^13.6.5 --save-dev
```

> This clones the repo, navigates to it, and installs a vulnerable Electron version. Expected output: Dependencies installed, no errors.

### Step 2: Run the Application

**Context**: Start the Electron app to load the renderer process.

**Instructions**: Execute the start script to launch the app.

```bash
npm start
```

> This runs the app using electron . command implicitly. Expected output: A new window opens displaying the quick-start HTML page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Electron]]
- [[tools/electron-quick-start]]

## Tags

- electron
- setup
- vulnerable-app
