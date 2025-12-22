---
tags:
  - web-cache-poisoning
  - http
  - dos
  - automation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7c08b73d-9ef7-4a67-bf53-e98318f19f3c
created_at: '2025-12-13T09:00:34.355Z'
updated_at: '2025-12-13T09:00:34.355Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Extend and Automate DoS Attack

## Summary

This procedure targets multiple pages and automates repeated poisoning requests to maintain DoS beyond the initial cache duration.

## Description

By poisoning additional pages like https://www.██████████/█████ and scripting repeated attacks, the DoS can be prolonged indefinitely, turning a temporary issue into a sustained disruption.

## Requirements

1. List of additional target pages
2. Scripting capability for automation (e.g., bash script with curl)
3. Confirmed vulnerability on target

## Defense

Defensive measures and detection strategies:

- Rate-limit requests from single IPs
- Implement cache invalidation timers
- Detect automated request patterns

## Objectives

1. Expand DoS to multiple pages
2. Achieve persistent disruption
3. Maximize impact through automation

## Instructions

### Step 1: Target Additional Pages

**Context**: Repeat poisoning on new paths.

> Send malformed requests to additional URLs to poison their caches.

### Step 2: Automate Repetition

**Context**: Script repeated attacks to refresh poisoning.

> Create a loop script to send poisoning requests periodically before cache expiration.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[web-cache-poisoning]]
- [[dos]]
- [[automation]]
