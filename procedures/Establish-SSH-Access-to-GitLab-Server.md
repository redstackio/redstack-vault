---
tags:
  - ssh
  - rce
  - shell-access
type: procedure
tools:
  - '[[tools/ssh]]'
  - '[[tools/gitlab-rake]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/gitlab-rake-env-info]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Remote Management]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:27.985Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5b1d75b2-fc11-45bf-b881-5eae4382dd16
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Remote Management]]'
  - '[[Unix Shell]]'
---
# Establish-SSH-Access-to-GitLab-Server

## Summary

This procedure leverages the injected SSH public key to gain remote shell access to the GitLab server as the 'git' user, confirming RCE and allowing further commands like environment reconnaissance.

## Description

After successful key injection via path traversal, the attacker connects to the GitLab server over SSH using the 'git' username and target IP. Authentication succeeds via the modified authorized_keys file. Once in, GitLab-specific rake tasks can be run to verify the environment and setup.

## Requirements

1. Injected SSH public key in server's /home/git/.ssh/authorized_keys
2. SSH client configured with corresponding private key
3. Network access to target SSH port 22
4. Local private key matching the uploaded public key

## Defense

Defensive measures and detection strategies:

- Monitor SSH authorized_keys modifications
- Use key-based auth with strict host key checking
- Log and alert on new SSH logins as 'git' user
- Disable SSH for 'git' user if possible

## Objectives

1. Authenticate and gain shell as 'git'
2. Execute commands to confirm control
3. Gather environment details for persistence

## Instructions

### Step 1: Initiate SSH Connection

**Context**: Connect to the server using the injected key for shell access.

**Command** ([[commands/ssh-gitlab-access]]):
```bash
ssh git@10.26.0.5
```

> This establishes an SSH session as 'git' user to the target IP, authenticating with the private key. Expected: shell prompt without password prompt.

**Success Indicators**:
- Login successful
- Prompt shows 'git@hostname'

### Step 2: Verify Access with Rake Task

**Context**: Run a GitLab rake task to output environment info, confirming RCE.

**Command** ([[commands/gitlab-rake-env-info]]):
```bash
gitlab-rake gitlab:env:info
```

> This displays system and GitLab details like versions. Expected: output with Ruby 2.6.3, GitLab 12.4.2-ee, etc.

**Success Indicators**:
- Detailed env info printed
- No permission errors

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Remote Management]]
- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/ssh-gitlab-access]]
- [[commands/gitlab-rake-env-info]]

## Tools Used

- [[tools/ssh]]
- [[tools/gitlab-rake]]

## Tags

- [[tools/ssh]]
- [[rce]]
