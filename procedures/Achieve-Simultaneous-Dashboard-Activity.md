---
tags:
  - dashboard-sabotage
  - reputation-damage
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.432Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 26f0d696-08ed-4e0e-bd1a-1184f2ba3770
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Achieve-Simultaneous-Dashboard-Activity

## Summary

This procedure finalizes the attack by observing how both parties' activities merge on the WakaTime dashboard, causing sabotage and metric corruption.

## Description

With parallel API keys active, submissions from both attacker and victim aggregate without isolation. The dashboard displays combined stats, leading to inaccurate rankings, reputation harm, and potential for further exploits like mass key theft via email enumeration.

## Requirements

1. Active sessions from both keys
2. Access to the shared dashboard
3. Ongoing activity from both sides

## Defense

Defensive measures and detection strategies:

- Isolate sessions by key or IP in aggregation logic
- Audit dashboard for duplicate source indicators
- Enable user reporting for suspicious stat changes

## Objectives

1. Merge activities to sabotage victim's profile
2. Expose impact on rankings and reputation
3. Validate the full chain's effectiveness

## Instructions

### Step 1: Submit Parallel Activities

**Context**: Ensure both keys are logging concurrently.

Attacker and victim both code simultaneously in their environments.

> API receives and stores data from multiple sources.

### Step 2: Review Aggregated Dashboard

**Context**: Inspect the unified view for anomalies.

Log in to https://waketime.com/dashboard and view stats.

> Mixed entries show, with totals reflecting both real and fake data.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dashboard-sabotage]]
- [[reputation-damage]]
