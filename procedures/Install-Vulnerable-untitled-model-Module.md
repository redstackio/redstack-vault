---
tags:
  - sqli
  - node.js
  - installation
type: procedure
tools:
  - '[[tools/yarn]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/yarn-add-untitled-model]]'
platforms:
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5dfca3e7-40f4-4178-a549-449f7062f72b
created_at: '2025-12-14T03:46:15.041Z'
updated_at: '2025-12-14T03:46:15.041Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-untitled-model-Module

## Summary

This procedure installs the vulnerable untitled-model Node.js module (version 1.0.5) into a project, setting the stage for SQL injection testing by including the package that directly concatenates user inputs into SQL queries.

## Description

The untitled-model module is a third-party npm package used for database modeling in Node.js applications. Due to its lack of input sanitization, it exposes SQL injection risks when used with untrusted data in functions like filter(). This procedure uses yarn to add it to a project, assuming a fresh Node.js setup. Prerequisites include Node.js installed and a project directory initialized with package.json.

## Requirements

1. Node.js runtime installed (version 8.12.0 or later)
2. Yarn package manager available
3. Write access to the project directory

## Defense

Defensive measures and detection strategies:

- Use parameterized queries or ORM libraries like Sequelize instead of raw concatenation
- Scan dependencies with tools like npm audit or Snyk for known vulnerabilities
- Monitor package installations in CI/CD pipelines

## Objectives

1. Integrate the vulnerable module for POC reproduction
2. Verify module availability for exploitation steps
3. Prepare environment without triggering production alerts

## Instructions

### Step 1: Add Module to Project

**Context**: Installs untitled-model from npm registry using yarn, updating dependencies.

**Command** ([[commands/yarn-add-untitled-model]]):
```bash
yarn add untitled-model
```

> This command fetches and installs version 1.0.5 (vulnerable), adding it to package.json. Expected output includes download progress and confirmation of addition to node_modules.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/yarn-add-untitled-model]]

## Tools Used

- [[tools/yarn]]

## Tags

- sqli
- node.js
