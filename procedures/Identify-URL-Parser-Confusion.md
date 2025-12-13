---
tags:
  - url-parsing
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c22a9d7f-d4d7-4f13-b662-0062f7337369
created_at: '2025-12-13T09:00:34.625Z'
updated_at: '2025-12-13T09:00:34.625Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify URL Parser Confusion

## Summary

This procedure identifies URL parser confusion with dot segments between frontend and backend servers.

## Description

Exploits disagreement on RFC 3986 section 5.2.4 where frontend normalizes /../ but backend does not, leading to cache mismatches. Used in web environments with CDNs.

## Requirements

1. Access to frontend and backend via proxies if possible.
2. Knowledge of URL normalization.
3. Testing URLs with dot segments.

## Defense

Defensive measures and detection strategies:

- Standardize URL parsing across layers.
- Reject requests with suspicious dot segments.

## Objectives

1. Confirm parser mismatch.
2. Enable cache poisoning vector.
3. Document RFC disagreement.

## Instructions

### Step 1: Test Normalization

**Context**: Send URLs with /../ to frontend and observe normalization.

> Request /Award/../Job/ and check effective path.

### Step 2: Compare Backend Behavior

**Context**: Bypass frontend if possible to test backend.

> Verify backend treats /../ as part of path.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[url-parsing]]
- [[web]]
