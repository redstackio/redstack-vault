---
tags:
  - web-cache-poisoning
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 3aa92153-6a07-4eee-bd5d-276b02e3b8f7
created_at: '2025-12-13T09:00:34.208Z'
updated_at: '2025-12-13T09:00:34.208Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Distribute Poisoned Response

## Summary

This procedure involves normal users accessing the poisoned page, receiving the cached malicious response, which results in broken functionality and denial of service.

## Description

Once the cache is poisoned, any user visiting the affected endpoint like /zh-cn/careers/ will get the altered page, potentially including injected XSS or failed resource loads, amplifying the attack's impact without further attacker interaction.

## Requirements

1. Cache already poisoned
2. Users accessing the site normally
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Regular cache flushing
- Anomaly detection in user access patterns

## Objectives

1. Achieve widespread DoS
2. Distribute potential attacks like XSS
3. Maximize impact

## Instructions

### Step 1: User Access

**Context**: Normal browsing to the poisoned URL.

No specific command; users visit https://www.acronis.com/zh-cn/careers/ and receive the poisoned cache.

> Results in broken page for users.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- web-cache-poisoning
- dos
