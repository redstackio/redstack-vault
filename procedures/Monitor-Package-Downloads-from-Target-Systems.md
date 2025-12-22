---
id: e9319005-36e5-4310-bde8-d35e6034e0d5
name: Monitor Package Downloads from Target Systems
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:06.049Z'
updated_at: '2025-12-11T03:48:06.049Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Supply Chain Compromise]]'
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
tags:
  - dependency-confusion
  - monitoring
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
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1195]]'
---

# Monitor Package Downloads from Target Systems

## Summary

This procedure involves observing downloads and installations of the registered packages from the target's systems to confirm exploitation.

## Description

Once packages are registered, the attacker monitors download logs or uses embedded tracking (e.g., beacons in the package code) to detect installations from the target's IP ranges or systems. This confirms the dependency confusion and potential RCE if malicious code was included. The target is development environments fetching packages automatically.

## Requirements

1. Access to npm package analytics or custom tracking server
2. Published packages with tracking mechanisms
3. Knowledge of target's IP ranges for correlation

## Defense

Defensive measures and detection strategies:

- Regularly audit package installations and sources
- Use network monitoring to detect unexpected outbound connections to public registries

## Objectives

1. Confirm downloads from target systems
2. Log installation details
3. Assess impact of any executed code

## Instructions

### Step 1: Check npm Logs

**Context**: Review public npm download statistics for the packages.

Access the npm package page or use API to fetch download logs and look for patterns matching the target's known activity.

### Step 2: Monitor Custom Tracking

**Context**: If included, monitor callbacks from the package code.

Set up a server to receive beacons or logs from the package's post-install scripts, confirming executions on target systems.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used



## Tools Used

- #npm

## Tags

- #dependency-confusion
- #monitoring
