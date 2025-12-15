---
tags:
  - installation
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-glance]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:16.689Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8dbb8efd-a92f-46bd-a4db-0bd20469d513
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-Glance-Module

## Summary

This procedure installs the Glance Node.js module, a static HTTP file server vulnerable to path traversal, using npm to set up the environment for exploitation testing.

## Description

The Glance module is installed locally via npm, placing it in the node_modules directory. This step is essential for local testing of the vulnerability where lack of path sanitization allows directory traversal. The target environment is a Node.js setup on Linux, with no prior access required beyond local execution privileges. Expected outcome is a successful installation enabling server startup in the next steps.

## Requirements

1. Node.js runtime installed (v8.9.4 LTS or later)
2. npm package manager available
3. Local directory for project setup

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit to detect known issues before installation
- Implement dependency pinning in package.json to avoid vulnerable versions

## Objectives

1. Prepare the vulnerable module for server execution
2. Verify installation integrity
3. Enable subsequent exploitation steps

## Instructions

### Step 1: Install Glance

**Context**: Use npm to fetch and install the Glance package from the registry, setting up the vulnerable component.

**Command** ([[commands/npm-install-glance]]):
```bash
npm install glance
```

> This command downloads and installs the Glance module, outputting logs like "added 1 package in X seconds". Successful execution confirms the module is ready in node_modules/glance.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-glance]]

## Tools Used

- [[tools/npm]]

## Tags

- installation
- node-js
