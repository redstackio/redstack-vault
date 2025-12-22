---
id: 1a9cf9ad-29d9-40d3-bbd4-5fbe3c0ae8f4
name: Identify Internal npm Package Names
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:06.053Z'
updated_at: '2025-12-11T03:48:06.053Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Supply Chain Compromise]]'
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
tags:
  - dependency-confusion
  - reconnaissance
  - npm
commands: []
platforms:
  - Node.js
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1195]]'
---

# Identify Internal npm Package Names

## Summary

This procedure involves analyzing target configurations or projects to identify internal npm package names that are not registered on the public registry, setting the stage for dependency confusion attacks.

## Description

In this attack scenario, the attacker examines development projects, such as those on GitHub or leaked sources, to find references to internal packages. These packages default to the public NPM registry if not found internally, allowing an attacker to register them publicly. The expected outcome is a list of exploitable package names that could lead to malicious code installation on target systems.

## Requirements

1. Access to public code repositories or leaked configurations
2. Basic knowledge of npm package naming conventions
3. Tools for searching and analyzing code (e.g., grep or code review tools)

## Defense

Defensive measures and detection strategies:

- Use scoped packages and internal registries exclusively
- Monitor for unexpected package installations from public sources

## Objectives

1. Compile a list of unregistered internal package names
2. Verify they are fetchable from public registry
3. Prepare for registration in subsequent steps

## Instructions

### Step 1: Analyze Configurations

**Context**: Search through available project files or configurations to find references to internal packages.

Review package.json files or build scripts for dependencies that start with specific prefixes (e.g., @company/internal-package) and check if they exist on the public npm registry using npm search or manual checks.

### Step 2: Verify Absence on Public Registry

**Context**: Confirm the packages are not already registered publicly.

Visit npmjs.com or use npm commands to search for the package names and ensure they return no results.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used



## Tools Used

- #npm

## Tags

- #dependency-confusion
- [[Reconnaissance]]
