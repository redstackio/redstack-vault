---
tags:
  - npm
  - supply-chain
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-npm-git-publish]]'
platforms:
  - Linux
  - Node.js
techniques:
  - '[[Compromise Hardware Supply Chain]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d47cac84-2411-4c23-b520-20229a43f8cb
created_at: '2025-12-14T17:23:20.107Z'
updated_at: '2025-12-14T17:23:20.107Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Compromise Hardware Supply Chain]]'
---
# Install-Vulnerable-npm-git-publish-Module

## Summary

This procedure installs the vulnerable npm-git-publish module version 0.2.4-beta from the public npm registry, enabling the subsequent RCE exploitation through its insecure command handling.

## Description

As part of a supply chain attack vector, installing unvetted dependencies like npm-git-publish exposes developers to RCE risks. The module's publish function formats the remote URL into a shell command without escaping, allowing injection. This procedure uses npm to fetch the specific vulnerable version, assuming public registry access. It targets Node.js project directories on Linux, where the module will be placed in node_modules for require() access. Post-install, the environment is ready for PoC execution, but in real scenarios, this could occur via malicious package suggestions or dependency confusion.

## Requirements

1. Node.js and npm installed on the system
2. Internet access to npm registry
3. Write permissions in the project directory
4. No prior installation of npm-git-publish to ensure vulnerable version

## Defense

Defensive measures and detection strategies:

- Run `npm audit` regularly to detect known vulnerabilities in dependencies
- Pin versions to secure releases and avoid betas (e.g., specify ^0.3.0 if patched)
- Use .npmrc to lock registry to verified sources and enable lockfiles
- Implement software bill of materials (SBOM) scanning with tools like Dependency-Track

## Objectives

1. Download and install the exact vulnerable module version
2. Set up the node_modules environment for exploitation
3. Confirm installation without triggering security warnings

## Instructions

### Step 1: Install the Module

**Context**: Use npm to install npm-git-publish, pulling the beta version with the RCE flaw.

**Command** ([[commands/npm-install-npm-git-publish]]):
```bash
npm i npm-git-publish
```

> The `i` flag installs the package; by default, it fetches the latest, but context specifies 0.2.4-beta. Expected output includes logs like "added 1 package" and version details. Verify with `npm ls npm-git-publish` to confirm 0.2.4-beta.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Compromise Hardware Supply Chain]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-npm-git-publish]]

## Tools Used

- [[tools/npm]]

## Tags

- [[tools/npm]]
- [[supply-chain]]
- [[installation]]
