---
tags:
  - setup
  - node-js
  - npm
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-global-http-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:49.814Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d40cded4-f125-44b1-a331-2ad49af24c72
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-http-server-Module

## Summary

This procedure installs the vulnerable http_server Node.js module globally using npm, enabling the creation of a static HTTP server that exposes directory listings without filename sanitization, setting the stage for stored XSS exploitation.

## Description

The http_server module is a simple Node.js package for serving static files and directories over HTTP. In this attack scenario, it is installed to simulate a misconfigured server where attackers can upload or create files with malicious names. The target environment is a local Node.js setup, with expected outcomes including the availability of the http_server command for launching the vulnerable service on port 8888. Prerequisites include Node.js and npm installed on the system.

## Requirements

1. Node.js runtime (version compatible with the module, e.g., 8+)
2. npm package manager
3. Internet access to the npm registry
4. Terminal access on Linux/macOS or Command Prompt/PowerShell on Windows

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for third-party modules in production environments
- Use package vulnerability scanners like npm audit to detect known issues
- Restrict global installations with npm policies or use yarn for better security

## Objectives

1. Prepare the environment by installing the http_server module
2. Enable server startup for directory serving
3. Verify module availability without errors

## Instructions

### Step 1: Install Globally

**Context**: Use npm to fetch and install the http_server package from the registry, making it executable system-wide.

**Command** ([[commands/npm-install-global-http-server]]):
```bash
npm install -g http_server
```

> This command downloads the package and installs it globally. Expected output includes progress messages and a final confirmation like "added X packages".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-global-http-server]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- installation
