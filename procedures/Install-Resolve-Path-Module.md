---
id: 123e4567-e89b-12d3-a456-426614174002
name: Install-Resolve-Path-Module
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.857Z'
tactics: []
techniques: []
sub_techniques: []
tags:
  - setup
  - node-js
commands:
  - '[[commands/npm-install-resolve-path]]'
platforms:
  - Windows
  - Node.js
tools:
  - '[[tools/NPM]]'
validated: true
---

# Install-Resolve-Path-Module

## Summary

This procedure installs the vulnerable version of the resolve-path Node.js module using NPM, setting up the environment for reproducing the path traversal vulnerability.

## Description

To test the vulnerability, the specific vulnerable version (1.3.3) must be installed in a Node.js project. This involves initializing a new NPM project if needed and installing the module. The setup ensures compatibility with Node.js v8.9.4 on Windows.

## Requirements

1. Node.js v8.9.4 and NPM v5.6.0 installed
2. Windows environment
3. Project directory created

## Defense

Defensive measures and detection strategies:

- Avoid installing known vulnerable versions; use npm audit to check dependencies
- Pin versions in package.json to secure releases

## Objectives

1. Prepare the vulnerable module for testing
2. Ensure environment matches discovery conditions

## Instructions

### Step 1: Initialize Project

**Context**: Create a new Node.js project to host the module.

**Command**:
```bash
npm init -y
```

> This generates package.json.

### Step 2: Install Vulnerable Module

**Context**: Install resolve-path v1.3.3 specifically.

**Command** ([[commands/npm-install-resolve-path]]):
```bash
npm install resolve-path@1.3.3
```

> Installation completes with the module in node_modules/resolve-path.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used

- [[commands/npm-install-resolve-path]]

## Tools Used

- [[tools/NPM]]

## Tags

- setup
- node-js
