---
id: 559a9d09-bd93-44bc-94a3-5ad60ac10639
name: Reconnaissance of Private NPM Module Names
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:40.582Z'
updated_at: '2025-12-11T03:47:40.582Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Supply Chain Compromise]]'
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
tags:
  - recon
  - dependency-confusion
commands: []
platforms:
  - Node.js
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1195]]'
---

# Reconnaissance of Private NPM Module Names

## Summary

This procedure involves identifying the names of internal private NPM modules used by the target organization, which is crucial for setting up a dependency confusion attack.

## Description

Discovery of private module names can be achieved through various reconnaissance methods such as analyzing public repositories, leaked information, or error messages. This step lays the foundation for publishing malicious packages with matching names but higher versions.

## Requirements

1. Access to public sources for reconnaissance.
2. Tools for information gathering (e.g., search engines, GitHub dorks).
3. Basic knowledge of NPM ecosystem.

## Defense

Defensive measures and detection strategies:

- Monitor for leaked module names in public sources.
- Use scoped packages to prevent confusion.

## Objectives

1. Obtain list of private module names.
2. Verify their usage in target's projects.
3. Prepare for malicious package creation.

## Instructions

### Step 1: Gather Information

**Context**: Search for potential leaks or references to private module names.

Use manual reconnaissance techniques, such as searching GitHub or public docs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used

## Tools Used

## Tags

- #recon
- #dependency-confusion
