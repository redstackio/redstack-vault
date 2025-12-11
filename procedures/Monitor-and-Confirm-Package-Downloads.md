---
tags:
  - dependency-confusion
  - monitoring
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-search]]'
  - '[[commands/npm-init]]'
  - '[[commands/npm-publish-package]]'
  - '[[commands/npm-install-observe]]'
platforms:
  - Web
  - Cloud
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 87b669d0-be02-4762-947a-b71c62d6ae24
created_at: '2025-12-11T06:10:40.149Z'
updated_at: '2025-12-11T06:10:40.149Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Monitor and Confirm Package Downloads

## Summary

This procedure focuses on observing and confirming that the published packages are downloaded by the target's systems, validating the dependency confusion vulnerability.

## Description

By embedding logging or using NPM analytics, attackers monitor installations, confirming that internal systems are pulling the public packages, potentially executing malicious code.

## Requirements

1. Published packages with monitoring capabilities.
2. Access to logging or analytics tools.
3. Knowledge of target IP ranges for confirmation.

## Defense

Defensive measures and detection strategies:

- Audit dependency installations regularly.
- Use network monitoring for unexpected registry accesses.

## Objectives

1. Capture download events.
2. Confirm target system involvement.
3. Assess potential for RCE.

## Instructions

### Step 1: Simulate and Observe Installation

**Context**: Test and monitor verbose installations.

**Command** ([[commands/npm-install-observe]]):
```bash
npm install package-name --loglevel=verbose
```

> Logs detailed installation info; in real scenarios, use package-embedded beacons.

### Step 2: Check Analytics

**Context**: Review NPM dashboard for download stats.

Monitor for IPs matching target's known ranges.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

## Commands Used

- [[commands/npm-install-observe]]

## Tools Used

- [[tools/npm]]

## Tags

- [[dependency-confusion]]
- [[monitoring]]
