---
id: proc-demonstrate-restrictions
tags:
  - container-confinement
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/attempt-dotfile-modification]]'
  - '[[commands/attempt-system-file-read]]'
verified: false
platforms:
  - Linux
  - Ubuntu
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:23.837Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Demonstrate-Snap-Container-Restrictions

## Summary

Post-RCE, test the snap confinement boundaries by attempting operations like dotfile modification and system file reads, which fail due to AppArmor restrictions, confirming the scoped impact.

## Description

Snap uses strict confinement, limiting access to non-hidden home files only. Attempts to touch dotfiles (.bashrc) or /etc/issue result in permission denied, highlighting why escape is necessary for full compromise. This step validates the environment and payload scope.

## Requirements

1. RCE achieved inside snap
2. Standard user home and /etc paths

## Defense

Defensive measures and detection strategies:

- Enable strict snap confinement for all apps
- Log AppArmor denials for unusual access patterns
- Review snap plugs for over-permissions like X11

## Objectives

1. Identify confinement limits
2. Confirm RCE is container-bound
3. Prepare rationale for escape

## Instructions

### Step 1: Attempt Dotfile Modification

**Context**: Test write to hidden file.

**Command** ([[commands/attempt-dotfile-modification]]):
```bash
echo 'echo PWNED' >> /home/itszn/.bashrc
```

> Fails with 'Permission denied'.

### Step 2: Attempt System File Read

**Context**: Test access outside home.

**Command** ([[commands/attempt-system-file-read]]):
```bash
cat /etc/issue
```

> Fails with 'Permission denied'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/attempt-dotfile-modification]]
- [[commands/attempt-system-file-read]]

## Tools Used


## Tags

- container-confinement
- discovery
