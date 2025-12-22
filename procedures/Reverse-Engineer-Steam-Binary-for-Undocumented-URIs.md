---
tags:
  - reverse-engineering
  - uri
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
  - '[[tools/React-Developer-Tools]]'
  - '[[tools/Binary-Grep]]'
  - '[[tools/Vim]]'
  - '[[tools/Remote-Chrome-Console]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/steam-open-game]]'
  - '[[commands/steam-open-console]]'
  - '[[commands/window-top-postmessage]]'
  - '[[commands/open-steam-uri]]'
  - '[[commands/object-keys-window]]'
  - '[[commands/steam-openexternalforpid-jarfile]]'
  - '[[commands/steam-openexternalforpid-file]]'
  - '[[commands/custom-protocol-txt]]'
  - '[[commands/custom-protocol-calculator]]'
  - '[[commands/custom-protocol-jarfile-traversal]]'
  - '[[commands/custom-protocol-jarfile-path]]'
platforms:
  - Windows
techniques:
  - '[[User Execution]]'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: efed3d77-500e-4728-bb89-250dd82dc128
created_at: '2025-12-11T06:10:18.132Z'
updated_at: '2025-12-11T06:10:18.132Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1204]]'
---
# Reverse Engineer Steam Binary for Undocumented URIs

## Summary

This procedure reverse-engineers the Steam binary to discover undocumented URIs like openexternalforpid for process execution.

## Description

By searching binary strings, attackers find hidden URI handlers that can be abused for RCE when combined with custom protocols.

## Requirements

1. Steam binary file
2. Binary analysis tools

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove undocumented URIs
- Monitor Steam console for unusual invocations

## Objectives

1. Find new URI patterns
2. Test with parameters
3. Confirm execution capabilities

## Instructions

### Step 1: Search Binary

**Context**: Grep for known URIs.

Use [[tools/Binary-Grep]] to search Steam.exe for 'steam://'.

> Expected: Discovery of openexternalforpid format.

### Step 2: Test Discovered URIs

**Context**: Validate with parameters.

Test [[commands/steam-openexternalforpid-jarfile]]: steam://openexternalforpid/10400/jarfile:something

```bash
steam://openexternalforpid/10400/jarfile:something
```

Test [[commands/steam-openexternalforpid-file]]: steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe

```bash
steam://openexternalforpid/10400/file:///C:/Windows/cmd.exe
```

> Expected: Process launch attempts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[User Execution]]

### Sub-Techniques



## Commands Used

- [[commands/steam-openexternalforpid-jarfile]]
- [[commands/steam-openexternalforpid-file]]

## Tools Used

- [[tools/Binary-Grep]]
- [[tools/Vim]]

## Tags

- [[reverse-engineering]]
- [[commands/open-steam-uri]]
