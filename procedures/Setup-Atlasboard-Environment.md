---
tags:
  - setup
  - atlasboard
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/atlasboard]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-atlasboard]]'
  - '[[commands/atlasboard-new-dashboard]]'
  - '[[commands/cd-to-dashboard]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:30.383Z'
sub_techniques: []
id: 76da6f3e-ade1-4734-b3a5-4d7506236e90
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Atlasboard-Environment

## Summary

This procedure installs the Atlasboard framework and initializes a new dashboard project, providing the foundation for integrating vulnerable JIRA widgets and exploiting the XSS vulnerability.

## Description

Atlasboard is a Node.js-based dashboard framework that pulls data from tools like JIRA. This setup creates a local environment to host the dashboard, allowing subsequent integration of the atlasboard-atlassian-package which contains the unsanitized 'blockers' widget. The process requires Node.js and npm, and assumes local execution privileges. Expected outcome is a runnable dashboard skeleton ready for configuration.

## Requirements

1. Node.js (v8 or later) installed on the system
2. npm package manager access
3. Write permissions to the current directory for creating project folders
4. Internet access for downloading packages

## Defense

Defensive measures and detection strategies:

- Monitor npm global installations for unauthorized dashboard tools
- Restrict Node.js executions in production environments
- Use package managers with audit features to scan for known vulnerabilities

## Objectives

1. Establish a local Atlasboard instance for vulnerability testing
2. Prepare directory structure for package integration
3. Verify framework installation for dashboard hosting

## Instructions

### Step 1: Install Atlasboard Globally

**Context**: Install the Atlasboard CLI tool system-wide to enable dashboard creation commands.

**Command** ([[commands/npm-install-atlasboard]]):
```bash
npm install -g atlasboard
```

> This command downloads and installs the atlasboard package globally via npm. Expected output includes installation progress logs and a success message confirming the CLI is available.

### Step 2: Create New Dashboard Project

**Context**: Generate the initial project structure for a custom dashboard named 'mywallboard'.

**Command** ([[commands/atlasboard-new-dashboard]]):
```bash
atlasboard new mywallboard
```

> Runs the Atlasboard CLI to scaffold a new directory with configuration files like package.json and dashboard templates. Expected output is the creation of the 'mywallboard' folder with subdirectories.

### Step 3: Navigate to Project Directory

**Context**: Change into the new project folder to perform further setup steps.

**Command** ([[commands/cd-to-dashboard]]):
```bash
cd mywallboard/
```

> Standard shell navigation command. Expected output is the shell prompt updating to reflect the new working directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-atlasboard]]
- [[commands/atlasboard-new-dashboard]]
- [[commands/cd-to-dashboard]]

## Tools Used

- [[tools/npm]]
- [[tools/atlasboard]]

## Tags

- [[setup]]
- [[tools/atlasboard]]
- [[node.js]]
