---
id: ae7491da-a6a0-483d-beb5-75198f5120d9
name: Register Packages on Public npm Registry
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:06.051Z'
updated_at: '2025-12-11T03:48:06.051Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Supply Chain Compromise]]'
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
tags:
  - dependency-confusion
  - npm
  - supply-chain
commands: []
platforms:
  - Node.js
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1195]]'
---

# Register Packages on Public npm Registry

## Summary

This procedure registers identified internal package names on the public npm registry, potentially with malicious code, to exploit dependency confusion.

## Description

After identifying vulnerable package names, the attacker creates and publishes packages to the public registry. These packages can include proof-of-concept tracking code or malicious payloads that execute upon installation, leading to RCE on target development systems. The target environment is Node.js-based development setups that default to public registries.

## Requirements

1. npm account on the public registry
2. List of identified package names
3. Optional: Malicious or tracking code to include in packages

## Defense

Defensive measures and detection strategies:

- Configure npm to use only internal registries
- Implement package allowlists and monitoring for public fetches

## Objectives

1. Publish packages successfully
2. Include mechanisms for tracking or exploitation
3. Enable observation of installations

## Instructions

### Step 1: Initialize Package

**Context**: Create a new npm package with the target name.

**Command** ([[commands/npm-init-package]]):
```bash
npm init -y
```

> This initializes a package.json file for the new package.

### Step 2: Publish Package

**Context**: Upload the package to the public registry.

**Command** ([[commands/npm-publish-package]]):
```bash
npm publish
```

> This publishes the package, making it available for automatic installation by vulnerable systems.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used

- [[commands/npm-init-package]]
- [[commands/npm-publish-package]]

## Tools Used

- #npm

## Tags

- #dependency-confusion
- [[Supply Chain Compromise]]
