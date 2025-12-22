---
id: af783e34-9bb0-4336-a94e-21849bb173dd
name: Publishing Malicious Packages to Public NPM Registry
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:40.507Z'
updated_at: '2025-12-11T03:47:40.507Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Supply Chain Compromise]]'
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
tags:
  - supply-chain
  - npm
commands: []
platforms:
  - Node.js
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1195]]'
---

# Publishing Malicious Packages to Public NPM Registry

## Summary

This procedure covers creating and publishing malicious NPM packages with higher versions to the public registry to exploit dependency confusion.

## Description

The attacker creates packages with the same names as private modules but embeds malicious code and sets higher version numbers. These are then published to npmjs.com.

## Requirements

1. NPM account.
2. Malicious code ready (e.g., scripts for RCE).
3. Knowledge of target module versions.

## Defense

Defensive measures and detection strategies:

- Configure registries to prevent fallback to public.
- Monitor public registry for squatted package names.

## Objectives

1. Publish malicious packages.
2. Ensure higher versions than private ones.
3. Include executable malicious scripts.

## Instructions

### Step 1: Create Malicious Package

**Context**: Develop the package with malicious install scripts.

### Step 2: Publish to Registry

**Context**: Upload the package.

**Command** ([[commands/npm-publish-malicious]]):
```bash
npm publish
```

> Publishes the package to the public registry with a higher version.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used

- [[commands/npm-publish-malicious]]

## Tools Used

- #npm

## Tags

- [[Supply Chain Compromise]]
- #npm
