---
tags:
  - gitlab
  - file-overwrite
  - repo-creation
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 442084af-50a5-4d69-a594-1b8f0eb85160
created_at: '2025-12-11T03:47:40.208Z'
updated_at: '2025-12-11T03:47:40.208Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Malicious Git Repository for File Overwrite

## Summary

This procedure involves creating a Git repository with a specially crafted directory structure that starts with '--output=' to exploit a command injection vulnerability in GitLab's git archive feature, enabling arbitrary file overwrites.

## Description

The attack targets self-hosted GitLab instances by crafting a repository path that is misinterpreted as command-line options in Gitaly, allowing overwrite of sensitive files like authorized_keys for RCE. Prerequisites include access to create repositories in GitLab and an SSH public key.

## Requirements

1. Git installed (version 2.21.0 or compatible)
2. Access to a GitLab instance
3. SSH key pair generated

## Defense

Defensive measures and detection strategies:

- Patch GitLab to versions without this vulnerability
- Monitor for unusual repository paths starting with '--'

## Objectives

1. Prepare exploit repository for file overwrite
2. Include attacker's SSH public key
3. Enable subsequent archive trigger

## Instructions

### Step 1: Set Up Directory Structure

**Context**: Create the exploit directory and add the public key file.

Initialize a Git repo and create directory '--output=/var/opt/gitlab/.ssh/authorized_keys/' with 'id_ed25519.pub' inside.

### Step 2: Verify Structure

**Context**: Confirm the crafted structure.

Execute [[commands/tree-display]]:

```bash
tree
```

> Displays the directory tree showing the exploit path and public key file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/tree-display]]

## Tools Used

- #git

## Tags

- #gitlab-rake
- #file-overwrite
