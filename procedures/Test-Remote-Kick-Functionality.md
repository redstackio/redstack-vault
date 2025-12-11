---
tags:
  - kick
  - testing
type: procedure
tools:
  - '[[tools/grep]]'
  - '[[tools/SourceMod]]'
  - '[[tools/Metamod]]'
  - '[[tools/CS:GO-Dedicated-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/disconnect-html-test]]'
  - '[[commands/kickid-test]]'
  - '[[commands/sm-kick-test]]'
  - '[[commands/sm-testkick-rce]]'
platforms:
  - Windows
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c5bb66a3-6473-4d18-a358-487a0f7eec9b
created_at: '2025-12-11T06:10:15.656Z'
updated_at: '2025-12-11T06:10:15.656Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Test Remote Kick Functionality

## Summary

This procedure tests kick commands on a dedicated CS:GO server to deliver custom messages remotely.

## Description

Starting with native kickid and moving to SourceMod's sm_kick, overcome character limits using KickClient() for unrestricted payload delivery.

## Requirements

1. Dedicated CS:GO server
2. SourceMod and Metamod installed
3. Admin access to server

## Defense

Defensive measures and detection strategies:

- Monitor server plugins
- Restrict kick message lengths

## Objectives

1. Test kick with payloads
2. Bypass character limits
3. Confirm remote delivery

## Instructions

### Step 1: Test Native Kick

**Context**: Attempt basic kick.

Execute [[commands/kickid-test]]:

```bash
kickid <player_id>
```

### Step 2: Test SourceMod Kick

**Context**: Use plugin for custom message.

Execute [[commands/sm-kick-test]]:

```bash
sm_kick <player> "message"
```

> Switch to KickClient() if limited.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/kickid-test]]
- [[commands/sm-kick-test]]

## Tools Used

- [[tools/SourceMod]]
- [[tools/Metamod]]

## Tags

- kick
- testing
