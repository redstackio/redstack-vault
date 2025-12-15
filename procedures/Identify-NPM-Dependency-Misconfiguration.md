---
tags:
  - reconnaissance
  - dependency-confusion
  - npm
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:18.348Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0933b22d-d666-453d-a23b-fba5f70a6980
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify NPM Dependency Misconfiguration

## Summary

This procedure involves reconnaissance to identify internal package names in a target's Node.js projects that do not exist on the public NPM registry, exploiting misconfigurations where builds default to public sources.

## Description

In dependency confusion attacks, attackers search for scoped or unscoped package names used internally but absent publicly. This is common in organizations with private registries like Verdaccio or Nexus, but default NPM configs pull from public.npmjs.com if internal fails. The procedure targets development pipelines, using public info like GitHub repos, job descriptions, or error logs to guess names. Expected outcome: A list of hijackable packages leading to supply chain compromise.

## Requirements

1. Access to public repositories or documentation of the target organization
2. NPM CLI installed for searching
3. Basic knowledge of Node.js package naming conventions (e.g., @org/internal-lib)

## Defense

Defensive measures and detection strategies:

- Enforce strict registry configuration in package.json or .npmrc (registry=internal-url)
- Use tools like npm audit or Snyk to scan for unexpected dependencies
- Monitor public NPM publishes for organization-scoped names

## Objectives

1. Discover candidate package names for confusion
2. Validate absence on public registry
3. Prepare for malicious publishing

## Instructions

### Step 1: Gather Potential Package Names

**Context**: Review public sources to identify likely internal package names.

Search GitHub for the target's repositories mentioning NPM dependencies:

Browse https://github.com/search?q=org:paypal+npm+package&type=code and note names like "@paypal/internal-auth".

**Expected Output**: List of guessed names (e.g., internal-auth, company-utils).

### Step 2: Verify Public Absence

**Context**: Confirm the packages do not exist publicly to ensure hijackability.

Use NPM search or view on npmjs.com:

```bash
npm info @paypal/internal-auth
```

If it returns "package not found", it's a candidate.

**Expected Output**: Error or no results for the package.

### Step 3: Document Misconfiguration Evidence

**Context**: Correlate with known pipeline behaviors.

Check public CI logs or docs for default registry usage.

**Expected Output**: Notes on potential impact (e.g., dev builds affected).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[npm]]
- [[supply-chain]]
