---
tags:
  - rce
  - npm
  - execution
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
  - '[[JavaScript]]'
  - '[[Compromise Software Dependencies and Development Tools]]'
updated_at: '2025-12-14T17:24:14.740Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7bda79d7-4e25-44eb-84fa-3e7655a096dc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Compromise Software Dependencies and Development Tools]]'
---
# Demonstrate-RCE-via-npm-Installation

## Summary

This procedure simulates the target's npm install process to show how the malicious package is pulled from the public registry and executes, proving RCE on build servers.

## Description

Replicate the target's package.json dependencies, run npm install without private registry config, and observe the fallback to public npm. The malicious postinstall or module code runs, demonstrating compromise. In Uber's scenario, this bypassed internal controls for build server access.

## Requirements

1. Malicious packages published
2. Sample package.json from target's public sources
3. Node.js environment for simulation

## Defense

Defensive measures and detection strategies:

- Configure .npmrc with `registry=https://private.npmjs.company.com`
- Use lockfiles and CI/CD scans for unexpected packages
- Log and alert on npm installs from public sources

## Objectives

1. Validate supply chain exploit
2. Show execution impact
3. Highlight internal system risks

## Instructions

### Step 1: Setup Test Environment

**Context**: Mimic target's config.

Create a test package.json with dependency on the orphaned name (e.g., "uber-internal-lib": "^1.0.0").

> Ensure no .npmrc overrides to private registry.

### Step 2: Run Installation

**Context**: Trigger the pull and execution.

Execute `npm install` in the test directory.

> Expected: Package downloaded from public npm, malicious code runs (e.g., command output or file creation).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Compromise Software Dependencies and Development Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[node-js]]
