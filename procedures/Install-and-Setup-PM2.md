---
id: uuid-install-setup
tags:
  - setup
  - pm2
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/pm2]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-pm2]]'
  - '[[commands/ln-symlink-pm2]]'
  - '[[commands/pm2-start]]'
verified: false
platforms:
  - Node.js
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:28:20.580Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Install-and-Setup-PM2

## Summary

This procedure installs the vulnerable PM2 version 3.5.1 using npm, creates a convenient symlink to the executable, and verifies the installation by starting the PM2 daemon. It sets up the environment for subsequent command injection exploits in the PM2 process manager.

## Description

PM2 is a production process manager for Node.js applications. In this vulnerable setup (version 3.5.1), the installation prepares the ground for exploiting command injection in the pm2.install() function. The procedure assumes local shell access on a Node.js environment running on macOS or Linux. Expected outcomes include a functional PM2 daemon ready for API interactions and CLI commands, with no processes running initially.

## Requirements

1. Node.js runtime (version 10.13.0 or later)
2. npm package manager access
3. Local shell (bash) on macOS or Linux
4. Internet access for npm install

## Defense

Defensive measures and detection strategies:

- Use package managers with vulnerability scanning (e.g., npm audit) to detect outdated PM2 versions
- Run process managers like PM2 in isolated containers or with least privileges
- Monitor for unexpected npm installations via endpoint detection tools

## Objectives

1. Install vulnerable PM2 to enable exploitation
2. Verify PM2 functionality without errors
3. Prepare symlink for easy CLI access

## Instructions

### Step 1: Install PM2 Module

**Context**: Install the PM2 module locally via npm to add it to the project's node_modules.

**Command** ([[commands/npm-install-pm2]]):
```bash
npm i pm2
```

> This command fetches and installs PM2 version 3.5.1 (vulnerable). Expected output includes installation logs and creation of the node_modules/pm2 directory.

### Step 2: Create Symlink to PM2 Executable

**Context**: Create a symbolic link in the current directory for convenient access to the PM2 binary without full paths.

**Command** ([[commands/ln-symlink-pm2]]):
```bash
ln -s ./node_modules/pm2/bin/pm2 pm2
```

> This links the PM2 binary to 'pm2' in the current dir. Expected output: Symlink created, verifiable with 'ls -l pm2' showing the link to node_modules.

### Step 3: Start PM2 Daemon

**Context**: Initialize the PM2 daemon to ensure it runs correctly and check for basic functionality.

**Command** ([[commands/pm2-start]]):
```bash
./pm2 start
```

> Starts PM2, which looks for ecosystem.config.js (none present). Expected output: Error about missing config and an empty process table, confirming PM2 is operational.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-pm2]]
- [[commands/ln-symlink-pm2]]
- [[commands/pm2-start]]

## Tools Used

- [[tools/npm]]
- [[tools/pm2]]

## Tags

- setup
- pm2
- node.js
