---
tags:
  - backdoor
  - persistence
  - rce
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/pm2]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:23:42.026Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: c4f516cc-cfcf-4e5e-ac76-1d11210591b1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Registry Run Keys - Startup Folder]]'
---
# Demonstrate-Backdoor-Installation-in-Rocket-Chat-Bundle

## Summary

This procedure modifies the extracted Rocket.Chat bundle to inject a backdoor, simulating full RCE by altering npm install and pm2 startup processes for persistence.

## Description

Locally, the attacker recreates the installation: modifies package.json or scripts to execute malicious code during npm install, then configures pm2 ecosystem file for startup persistence. Targets Node.js environments on Linux. Requires the extracted bundle from prior steps. Expected outcomes: Backdoor activates on install, allowing ongoing access without user knowledge.

## Requirements

1. Extracted malicious tarball from previous procedure
2. Node.js and npm installed
3. PM2 for process management

## Defense

Defensive measures and detection strategies:

- Audit npm packages and scripts for malicious code
- Use npm audit and lockfiles for integrity
- Monitor pm2 startups for unauthorized processes

## Objectives

1. Inject backdoor into installation bundle
2. Achieve persistent execution
3. Demonstrate full compromise impact

## Instructions

### Step 1: Modify Bundle for Backdoor

**Context**: Alter extracted files to include malicious code in npm scripts.

Edit package.json to add a postinstall script executing a backdoor (e.g., reverse shell).

### Step 2: Simulate npm Install

**Context**: Run npm install to trigger the injected code.

```bash
cd bundle-directory
npm install
```

> Malicious script runs during postinstall, e.g., spawning a shell.

### Step 3: Configure PM2 for Persistence

**Context**: Modify ecosystem.config.js to execute backdoor on startup.

Add malicious command to PM2 config, then start:

```bash
pm2 start ecosystem.config.js
```

> PM2 launches with backdoor integrated; verify via pm2 logs showing execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell
- [[Registry Run Keys - Startup Folder]] Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/npm]]
- [[tools/pm2]]

## Tags

- backdoor
- persistence
- rce
