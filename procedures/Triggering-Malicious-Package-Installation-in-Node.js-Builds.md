---
id: 28025b26-6234-4c15-9ce2-112e089018c2
name: Triggering Malicious Package Installation in Node.js Builds
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:40.482Z'
updated_at: '2025-12-11T03:47:40.482Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Supply Chain Compromise]]'
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
tags:
  - dependency-confusion
  - installation
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

# Triggering Malicious Package Installation in Node.js Builds

## Summary

This procedure exploits the misconfiguration to cause the victim's build process to install the malicious package from the public registry.

## Description

Due to the fallback mechanism, higher versions from public are prioritized, leading to installation during project builds.

## Requirements

1. Victim's project dependent on the module.
2. Build process triggered (e.g., CI/CD).
3. Misconfigured registry.

## Defense

Defensive measures and detection strategies:

- Enforce private registry scoping.
- Audit dependencies during builds.

## Objectives

1. Ensure malicious package is pulled.
2. Confirm installation occurs.
3. Prepare for code execution.

## Instructions

### Step 1: Monitor for Build Triggers

**Context**: Wait for or induce a build that installs dependencies.

**Command** ([[commands/npm-install]]):
```bash
npm install
```

> This command, run in the victim's environment, installs the malicious version.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used

- [[commands/npm-install]]

## Tools Used

- #npm

## Tags

- #dependency-confusion
- [[Installation]]
