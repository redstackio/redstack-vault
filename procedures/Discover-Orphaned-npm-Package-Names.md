---
tags:
  - reconnaissance
  - npm
  - dependency-confusion
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:14.762Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7cca53dc-76f8-477e-8115-7853e52da015
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Orphaned-npm-Package-Names

## Summary

This procedure involves searching public sources for references to internal Node.js package names that are not published or protected on the public npm registry, identifying opportunities for dependency confusion attacks.

## Description

In scenarios like Uber's, internal libraries are referenced in code or configs without scoping (e.g., no @uber/ prefix) or private registry locks. Attackers scan GitHub repos, HackerOne reports, or public docs for such names. Once identified, verify they are unregistered on npmjs.com. This reconnaissance enables claiming them for malicious publishing, potentially leading to supply chain compromise.

## Requirements

1. Access to public search engines and GitHub
2. Knowledge of target's naming conventions (e.g., 'uber-*')
3. npm registry read access

## Defense

Defensive measures and detection strategies:

- Scope all internal packages (e.g., @company/)
- Enforce .npmrc with registry=private-url and audit=true
- Monitor npm registry for new claims on company-named packages

## Objectives

1. Identify exploitable orphaned dependencies
2. Gather intel on target's build process
3. Enable subsequent package claiming

## Instructions

### Step 1: Search Public Sources

**Context**: Use search engines to find leaked internal package references.

Search Google or GitHub for "uber internal npm package" or site:github.com "package.json" "uber-".

> Focus on error messages or configs revealing names like 'uber-build-tool'.

### Step 2: Verify on npm Registry

**Context**: Confirm the packages are unregistered.

Visit npmjs.com and search for each discovered name.

> Expected: No results or 'not found' page, indicating availability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[npm]]
