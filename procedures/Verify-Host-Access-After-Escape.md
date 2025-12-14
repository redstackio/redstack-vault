---
id: proc-verify-host-access
tags:
  - post-escape-verification
  - host-compromise
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/read-system-issue-post-escape]]'
  - '[[commands/modify-dotfile-post-escape]]'
  - '[[commands/check-dotfile-modification]]'
verified: false
platforms:
  - Linux
  - Ubuntu
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:23:23.831Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Host-Access-After-Escape

## Summary

Confirm successful container escape by performing operations denied inside the snap, such as reading /etc/issue and modifying dotfiles, proving full host user access.

## Description

After X11 escape, the payload operates in host context, bypassing snap restrictions. This allows persistent changes like appending to .bashrc and accessing system files, demonstrating complete user-level compromise.

## Requirements

1. Successful X11 escape
2. Target files like /etc/issue and ~/.bashrc

## Defense

Defensive measures and detection strategies:

- Audit dotfile changes for unauthorized appends
- Monitor /etc reads from unexpected processes
- Implement file integrity monitoring on user configs

## Objectives

1. Validate host access
2. Confirm privilege escalation
3. Assess persistence potential

## Instructions

### Step 1: Read System Issue Post-Escape

**Context**: Test /etc access.

**Command** ([[commands/read-system-issue-post-escape]]):
```bash
cat /etc/issue
```

> Outputs 'Ubuntu 18.04.4 LTS \n \l'.

### Step 2: Modify Dotfile Post-Escape

**Context**: Test hidden file write.

**Command** ([[commands/modify-dotfile-post-escape]]):
```bash
echo 'echo PWNED' >> /home/itszn/.bashrc
```

> Appends successfully.

### Step 3: Check Modification

**Context**: Verify change.

**Command** ([[commands/check-dotfile-modification]]):
```bash
tail -n 1 /home/itszn/.bashrc
```

> Outputs 'echo PWNED'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/read-system-issue-post-escape]]
- [[commands/modify-dotfile-post-escape]]
- [[commands/check-dotfile-modification]]

## Tools Used


## Tags

- post-escape-verification
- host-compromise
