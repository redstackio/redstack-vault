---
tags:
  - rce
  - npm
  - malware
  - dependency-confusion
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:14.746Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: aad57f62-3354-44bf-b04a-5515ecd8606e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
  - '[[JavaScript]]'
---
# Publish-Malicious-Code-to-Claimed-Packages

## Summary

This procedure involves creating and publishing Node.js packages with malicious code to claimed names, designed to execute during installation in the target's build process, achieving RCE.

## Description

Build a package mimicking the internal library, embedding code in postinstall scripts or main module to run commands (e.g., curl to attacker server or system probes). Publish via npm, exploiting the target's fallback to public registry. Uber's proof-of-concept showed this leading to build server compromise.

## Requirements

1. Owned package names on npm
2. Node.js and npm installed locally
3. Basic JavaScript knowledge for payload

## Defense

Defensive measures and detection strategies:

- Pin dependencies with exact versions in package-lock.json
- Use npm audit and Snyk for supply chain scanning
- Restrict builds to verified registries

## Objectives

1. Deploy executable malicious payload
2. Mimic legitimate internal functionality
3. Trigger RCE on installation

## Instructions

### Step 1: Create Malicious Package

**Context**: Develop the package structure with payload.

Create directory, package.json with name matching orphaned (e.g., "uber-internal-lib": "1.0.0"), and index.js or scripts/postinstall.js with exec('whoami') or similar.

> Test locally with npm pack to ensure no errors.

### Step 2: Publish to npm

**Context**: Upload the package to public registry.

Run `npm publish` from the package directory after login.

> Expected: Success message; verify on npmjs.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Compromise Software Dependencies and Development Tools]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[JavaScript]]
