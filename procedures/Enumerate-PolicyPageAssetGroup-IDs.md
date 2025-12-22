---
tags:
  - enumeration
  - idor
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/graphql-query-asset-group-name]]'
  - '[[commands/graphql-query-asset-group-details]]'
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 633fd087-ae37-487e-a670-631843e3b312
created_at: '2025-12-11T03:48:05.935Z'
updated_at: '2025-12-11T03:48:05.935Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1213]]'
---
# Enumerate PolicyPageAssetGroup IDs

## Summary

This procedure involves guessing or enumerating numerical IDs for PolicyPageAssetGroups, which are used as the first part of the Global ID in HackerOne's GraphQL queries.

## Description

By trying sequential numerical values (e.g., 1 to 5000), attackers can identify valid PolicyPageAssetGroup IDs to combine with program IDs. This is a brute-force approach without specific tools, relying on trial and error in subsequent queries.

## Requirements

1. Knowledge of potential ID ranges from similar systems
2. Patience for manual enumeration
3. Integration with GID construction steps

## Defense

Defensive measures and detection strategies:

- Use non-sequential or obfuscated IDs
- Monitor for high volumes of failed queries

## Objectives

1. Discover valid asset group IDs
2. Enable GID construction for exploitation
3. Support information disclosure attacks

## Instructions

### Step 1: Guess Numerical IDs

**Context**: Manually enumerate possible IDs by testing values in GID formats during queries.

> Try values like 3981 and increment/decrement to find valid ones; no specific command, but integrate with query steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #enumeration
- #idor
