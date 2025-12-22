---
id: proc-hangersteak-install-001
tags:
  - directory-traversal
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-hangersteak]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:05.554Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-Hangersteak-Module

## Summary

This procedure installs the vulnerable hangersteak Node.js module (v0.2.4) from the npm registry to set up an environment for reproducing the directory traversal vulnerability.

## Description

The hangersteak module is a static file server for Node.js that fails to sanitize paths, allowing traversal attacks. Installing it via npm prepares the local environment. This step requires Node.js and npm to be pre-installed on a Linux or compatible system. Once installed, the module can be required in scripts to create vulnerable servers. Expected outcomes include a successful package download without version specification, defaulting to the latest (vulnerable) version.

## Requirements

1. Node.js runtime installed (v10+ recommended)
2. npm package manager available
3. Internet access to npm registry
4. Local directory for project setup

## Defense

Defensive measures and detection strategies:

- Audit dependencies with tools like npm audit to identify vulnerable packages
- Pin versions to non-vulnerable releases (e.g., avoid 0.2.4)
- Monitor npm install logs for suspicious package names

## Objectives

1. Download and install hangersteak for server setup
2. Verify module availability for scripting
3. Prepare environment for vulnerability reproduction

## Instructions

### Step 1: Install the Module

**Context**: Use npm to fetch the hangersteak package, which will install version 0.2.4 if not specified.

**Command** ([[commands/npm-install-hangersteak]]):
```bash
npm install hangersteak
```

> This command resolves the package from the npm registry, creates a node_modules directory, and outputs installation progress. Expected output includes lines like "added 1 package" and confirmation of hangersteak@0.2.4.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-hangersteak]]

## Tools Used

- [[tools/npm]]

## Tags

- [[directory-traversal]]
- [[node-js]]
