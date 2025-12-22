---
tags:
  - dependency-confusion
  - recon
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
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
id: c9c1dd7f-c9c1-417c-b581-3bc5baefbaaf
created_at: '2025-12-11T06:10:40.155Z'
updated_at: '2025-12-11T06:10:40.155Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1195]]'
---
# Identify Unregistered Internal NPM Packages

## Summary

This procedure involves analyzing target development projects to discover internal NPM package names that are not registered on the public registry, setting the stage for dependency confusion attacks.

## Description

In dependency confusion scenarios, attackers identify package names used internally but not reserved publicly. By searching public sources or leaks, attackers can find these names and prepare to claim them, leading to unintended installations from the public registry.

## Requirements

1. Access to public code repositories or leaks containing package.json files.
2. NPM CLI installed.
3. Basic knowledge of Node.js ecosystems.

## Defense

Defensive measures and detection strategies:

- Use scoped packages and internal registries.
- Monitor for unexpected package downloads.

## Objectives

1. Compile a list of unregistered internal packages.
2. Verify they default to public registry.
3. Prepare for registration in attack chain.

## Instructions

### Step 1: Search for Package Names

**Context**: Query the public NPM registry to check for existing registrations.

**Command** ([[commands/npm-search]]):
```bash
npm search suspected-internal-package
```

> This command returns search results; if no package is found, it's unregistered.

### Step 2: Analyze Sources

**Context**: Review public GitHub repos or leaks for package.json references.

Manually inspect or script the extraction of dependency names not prefixed with scopes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used

- [[commands/npm-search]]

## Tools Used

- [[tools/npm]]

## Tags

- [[dependency-confusion]]
- [[recon]]
