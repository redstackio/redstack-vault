---
tags:
  - setup
  - pm2
  - npm
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/pm2]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-i-pm2]]'
  - '[[commands/pm2-start]]'
verified: false
platforms:
  - Node.js
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:28:20.457Z'
sub_techniques: []
id: a0a44ecd-7090-4019-8e80-a94ca2848bd5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Install-and-Verify-PM2

## Summary

This procedure installs the PM2 Node.js process manager locally using npm and verifies its functionality by starting the daemon, setting up the environment for subsequent command injection exploitation.

## Description

PM2 is a production process manager for Node.js applications. In vulnerable versions like 3.5.1, it suffers from command injection in the install function. This setup step reproduces the environment by installing PM2 in a local project directory and creating a symlink to its executable. Verification ensures the daemon runs correctly before exploitation. Prerequisites include Node.js (v10.13.0+) and npm installed on a Unix-like system (macOS/Linux). Expected outcome: Functional PM2 ready for CLI/API interaction.

## Requirements

1. Node.js runtime installed (version 10+)
2. npm package manager access
3. Local project directory with write permissions
4. Unix shell environment (macOS or Linux)

## Defense

Defensive measures and detection strategies:

- Use package managers with input validation and avoid shell: true in spawn calls
- Monitor npm install processes for anomalous command executions via process auditing tools like auditd
- Employ application-level input sanitization for module names in process managers

## Objectives

1. Install PM2 to replicate the vulnerable setup
2. Verify PM2 daemon startup without errors
3. Prepare for command injection testing

## Instructions

### Step 1: Install PM2

**Context**: Installs PM2 locally in the project directory to enable access to the vulnerable install function.

**Command** ([[commands/npm-i-pm2]]):
```bash
npm i pm2
```

> This command fetches and installs PM2 version 3.5.1 (vulnerable), outputting installation logs and a success message. Create a symlink to ./node_modules/.bin/pm2 if needed for global-like access.

### Step 2: Verify PM2 Installation

**Context**: Starts the PM2 daemon to confirm correct installation and functionality.

**Command** ([[commands/pm2-start]]):
```bash
./pm2 start
```

> Starts the PM2 process manager, displaying a status table. If no apps are running, it shows an empty table or warns about missing ecosystem.config.js; success indicates the daemon is ready.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/npm-i-pm2]]
- [[commands/pm2-start]]

## Tools Used

- [[tools/npm]]
- [[tools/pm2]]

## Tags

- setup
- pm2
- npm
