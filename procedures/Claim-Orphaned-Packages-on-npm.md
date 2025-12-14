---
tags:
  - npm
  - supply-chain
  - dependency-confusion
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
updated_at: '2025-12-14T17:24:14.754Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 0b874a25-2a47-4a4a-af12-15e9df4e7ec4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Compromise Software Dependencies and Development Tools]]'
---
# Claim-Orphaned-Packages-on-npm

## Summary

This procedure registers ownership of unused package names on the public npm registry, positioning the attacker to publish malicious versions that can be pulled by misconfigured internal builds.

## Description

After discovering orphaned names, create an npm account and claim them via the registry website or CLI. This exploits the lack of scoping in the target's package.json, where npm install falls back to public registry. In Uber's case, this allowed control over internal library names, enabling RCE during builds.

## Requirements

1. Valid npm account (free signup)
2. List of target package names
3. Internet access to npmjs.com

## Defense

Defensive measures and detection strategies:

- Pre-claim all potential internal package names
- Use scoped packages and private registries exclusively
- Set up alerts for npm publications matching company patterns

## Objectives

1. Gain control over supply chain entry points
2. Prepare for malicious code deployment
3. Disrupt target's dependency resolution

## Instructions

### Step 1: Create npm Account

**Context**: Ensure authenticated access for registration.

Visit npmjs.com and sign up or log in.

> Expected: Account dashboard accessible.

### Step 2: Register Packages

**Context**: Claim each orphaned name.

On the npm site, search for the package name and select 'Initialize new package' or use the web form to create it.

> Repeat for all names; success confirmed by ownership in profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Compromise Software Dependencies and Development Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[supply-chain]]
- [[npm]]
