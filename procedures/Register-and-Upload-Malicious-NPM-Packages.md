---
tags:
  - dependency-confusion
  - supply-chain
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-search]]'
  - '[[commands/npm-init]]'
  - '[[commands/npm-publish-package]]'
  - '[[commands/npm-install-observe]]'
platforms:
  - Web
  - Cloud
techniques:
  - '[[Supply Chain Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
id: 4d0e69e3-aaf2-40fa-b567-35c44b4ff640
created_at: '2025-12-11T06:10:40.152Z'
updated_at: '2025-12-11T06:10:40.152Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1195]]'
---
# Register and Upload Malicious NPM Packages

## Summary

This procedure covers creating and publishing NPM packages using unregistered internal names, potentially embedding malicious code for dependency confusion exploitation.

## Description

Attackers register the identified names on the public NPM registry, uploading packages that could include backdoors or monitoring code, exploiting misconfigurations where internal systems fetch from public sources.

## Requirements

1. NPM account with publishing rights.
2. Package code ready, including any malicious payloads.
3. Target package names from reconnaissance.

## Defense

Defensive measures and detection strategies:

- Configure npm to use private registries exclusively.
- Implement package allowlisting.

## Objectives

1. Claim the package name publicly.
2. Upload package with potential malicious content.
3. Enable automatic installation by vulnerable systems.

## Instructions

### Step 1: Initialize Package

**Context**: Set up a new package directory.

**Command** ([[commands/npm-init]]):
```bash
npm init -y
```

> Initializes package.json with defaults.

### Step 2: Publish Package

**Context**: Upload to public registry.

**Command** ([[commands/npm-publish-package]]):
```bash
npm publish
```

> Publishes the package; include malicious index.js if desired.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used

- [[commands/npm-init]]
- [[commands/npm-publish-package]]

## Tools Used

- [[tools/npm]]

## Tags

- [[dependency-confusion]]
- [[supply-chain]]
