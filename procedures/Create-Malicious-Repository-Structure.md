---
tags:
  - repository-setup
  - command-injection
type: procedure
tools:
  - '[[tools/tree]]'
  - '[[tools/git]]'
  - '[[tools/docker]]'
  - '[[tools/cat]]'
  - '[[tools/ssh]]'
  - '[[tools/whoami]]'
  - '[[tools/gitlab-rake]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/tree-display]]'
  - '[[commands/git-archive-injected]]'
  - '[[commands/docker-exec-bash]]'
  - '[[commands/cat-file]]'
  - '[[commands/ssh-connect]]'
  - '[[commands/whoami-user]]'
  - '[[commands/gitlab-rake-env]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: d40b69e0-b286-4dae-aabf-653c16d86b79
created_at: '2025-12-11T06:10:22.647Z'
updated_at: '2025-12-11T06:10:22.647Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Malicious Repository Structure

## Summary

This procedure involves creating a Git repository with a specially crafted directory structure that injects options into the git archive command, enabling arbitrary file overwrites on a vulnerable GitLab server.

## Description

The attack exploits unsanitized concatenation of the 'path' parameter in Gitaly's archive.go, allowing paths starting with '--output=' to redirect archive output to server files like authorized_keys, leading to RCE. This requires access to create repositories in GitLab 11.11.

## Requirements

1. Access to a GitLab instance for repository creation.
2. Attacker's SSH public key.
3. Local Git installation.

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs in git commands.
- Monitor for unusual repository paths or archive requests.

## Objectives

1. Prepare repository for command injection.
2. Include malicious path and SSH key.
3. Enable file overwrite trigger.

## Instructions

### Step 1: Set Up Directory Structure

**Context**: Create the directory path that injects '--output=' option.

Create a directory starting with '--output=/var/opt/gitlab/.ssh/authorized_keys/' and add 'id_ed25519.pub' containing the attacker's public key.

### Step 2: Visualize Structure

**Context**: Verify the malicious structure.

Execute [[commands/tree-display]] to display the directory tree:

```bash
tree
```

> Displays the tree showing the injected path and public key file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/tree-display]]

## Tools Used

- [[tools/tree]]

## Tags

- [[repository-setup]]
- [[command-injection]]
