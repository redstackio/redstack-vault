---
id: 5f1e4f0e-bc04-4487-8579-0ffb1cf5ba39
name: Executing Arbitrary Code via Malicious NPM Package
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:40.451Z'
updated_at: '2025-12-11T03:47:40.451Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
sub_techniques: []
tags:
  - rce
  - execution
commands: []
platforms:
  - Node.js
tools: []
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---

# Executing Arbitrary Code via Malicious NPM Package

## Summary

This procedure involves the execution of malicious scripts embedded in the installed NPM package, leading to arbitrary code execution on the host.

## Description

Upon installation, the package's scripts run automatically, executing attacker-controlled code on the affected systems.

## Requirements

1. Malicious package installed.
2. Installation scripts enabled.
3. Host permissions for code execution.

## Defense

Defensive measures and detection strategies:

- Scan packages for malicious code.
- Run builds in isolated environments.

## Objectives

1. Achieve code execution.
2. Perform post-exploitation actions.
3. Maintain access if needed.

## Instructions

### Step 1: Code Execution During Install

**Context**: The malicious script runs automatically.

No direct command; execution is triggered by installation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

## Commands Used

## Tools Used

- #npm

## Tags

- #rce
- [[Execution]]
