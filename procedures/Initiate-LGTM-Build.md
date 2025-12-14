---
id: proc-initiate-lgtm-build
tags:
  - lgtm
  - build
  - rce
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:57.741Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---
# Initiate-LGTM-Build

## Summary

This procedure triggers the LGTM build process on a configured GitHub repository, executing the RCE payload in the .lgtm.yml to establish the reverse shell.

## Description

LGTM integrates with GitHub to run automated builds in a sandboxed Docker container. Adding the repo to LGTM starts the analysis, running the YAML steps and connecting the reverse shell to the attacker's listener after initialization.

## Requirements

1. GitHub repo with .lgtm.yml committed
2. LGTM account or public repo access
3. Active netcat listener

## Defense

Defensive measures and detection strategies:

- Review build logs for anomalous commands
- Limit YAML execution to trusted patterns
- Isolate build environments with no outbound access

## Objectives

1. Execute RCE payload in sandbox
2. Confirm reverse shell connection
3. Gain foothold for further exploitation

## Instructions

### Step 1: Add Project to LGTM

**Context**: Integrate the repository to start the build process.

No command; navigate to LGTM dashboard, search for the GitHub repo, and enable analysis.

> The build triggers automatically, running .lgtm.yml steps. Monitor netcat for connection (may take 1-5 minutes).

### Step 2: Verify Connection

**Context**: Confirm shell access in listener.

No command; interact with the shell prompt in netcat.

> Expected: Full shell access to container, e.g., run 'whoami' to verify.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- lgtm
- build

---
