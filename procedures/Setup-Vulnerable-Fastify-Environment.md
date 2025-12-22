---
tags:
  - setup
  - poc
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-fastify-poc]]'
  - '[[commands/npm-install-fastify-deps]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.793Z'
sub_techniques: []
id: c04d0fbd-4fde-4926-93fd-2076a8b504cf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Vulnerable-Fastify-Environment

## Summary

This procedure sets up a local development environment for demonstrating the RCE vulnerability in Fastify with @fastify/view and EJS by creating a project directory and installing required dependencies.

## Description

In a Node.js environment, create a dedicated directory for the proof-of-concept (PoC) and use npm to install Fastify, the @fastify/view plugin, and the EJS template engine. This prepares the groundwork for building and running the vulnerable server, allowing subsequent steps to focus on code creation and exploitation. The setup assumes a standard Node.js installation and targets local execution for testing.

## Requirements

1. Node.js and npm installed on the system
2. Write permissions in the current directory
3. Internet access for package downloads

## Defense

Defensive measures and detection strategies:

- Use package managers with audit features (e.g., npm audit) to scan for known vulnerabilities in dependencies
- Implement containerization or virtual environments to isolate PoC setups from production systems

## Objectives

1. Establish a clean project space for the vulnerable application
2. Install exact dependencies matching the vulnerable configuration
3. Verify readiness for server creation

## Instructions

### Step 1: Create Project Directory

**Context**: Initialize the PoC directory to organize files and dependencies.

**Command** ([[commands/mkdir-fastify-poc]]):
```bash
mkdir fastify-rce-poc && cd fastify-rce-poc
```

> This command creates the directory and changes into it, setting up the working environment. Expected output: New directory created and current working directory changed to fastify-rce-poc.

### Step 2: Install Dependencies

**Context**: Fetch and install the required Node.js packages for the Fastify server.

**Command** ([[commands/npm-install-fastify-deps]]):
```bash
npm install fastify @fastify/view ejs
```

> Installs Fastify framework, view plugin, and EJS engine. Expected output: Packages installed in node_modules, with package.json updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/mkdir-fastify-poc]]
- [[commands/npm-install-fastify-deps]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- poc
- node.js
