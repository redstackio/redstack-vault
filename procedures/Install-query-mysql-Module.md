---
id: proc-001
tags:
  - sqli
  - node.js
  - setup
type: procedure
tools:
  - '[[tools/NPM-Package-Manager]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-query-mysql]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:15.096Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-query-mysql-Module

## Summary

This procedure installs the vulnerable 'query-mysql' Node.js module (v0.0.2) using npm, setting up the environment for demonstrating SQL injection in its query construction functions.

## Description

The query-mysql module builds SQL queries via string concatenation without input sanitization, particularly in fetchById. This procedure prepares a local Node.js project to exploit this by installing the module and configuring a basic app. It assumes a fresh Node.js environment and targets local development setups simulating third-party module usage in web apps.

## Requirements

1. Node.js v8.9.3 or later installed
2. npm 5.5.1 or compatible
3. Local project directory initialized with package.json

## Defense

Defensive measures and detection strategies:

- Use audited dependencies; avoid unmaintained modules like query-mysql
- Scan for known vulns with npm audit or Snyk
- Monitor for anomalous npm installs in CI/CD pipelines

## Objectives

1. Add vulnerable module to project dependencies
2. Verify installation for exploitation readiness
3. Prepare for database integration testing

## Instructions

### Step 1: Initialize Project if Needed

**Context**: Ensure a Node.js project exists to install dependencies.

**Command** ([[commands/npm-init-project]]):
```bash
npm init -y
```

> Initializes package.json; expected output: package.json created.

### Step 2: Install Module

**Context**: Download and install query-mysql from npm.

**Command** ([[commands/npm-install-query-mysql]]):
```bash
npm install query-mysql
```

> Installs v0.0.2 (vulnerable version); expected output: added to node_modules and package.json.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-query-mysql]]

## Tools Used

- [[tools/NPM-Package-Manager]]

## Tags

- sqli
- node.js
- setup
