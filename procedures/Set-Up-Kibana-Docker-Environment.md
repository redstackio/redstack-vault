---
tags:
  - kibana
  - docker
  - setup
type: procedure
tools:
  - '[[tools/headless_shell]]'
  - '[[tools/Metasploit]]'
  - '[[tools/Python-SimpleHTTPServer]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
  - Docker
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bb8071d4-3e96-46c8-8a48-2ed492689678
created_at: '2025-12-11T03:47:47.808Z'
updated_at: '2025-12-11T03:47:47.808Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Set Up Kibana Docker Environment

## Summary

This procedure sets up a Docker container running Kibana version 7.12.0 to access the vulnerable headless Chromium binary for testing and exploitation purposes.

## Description

By launching the Kibana Docker image in interactive mode, attackers can enter a bash shell and navigate to the directory containing the headless_shell binary. This environment simulates the target setup on Elastic Cloud, ECE, or ECK, allowing for local testing of the RCE vulnerability in the reporting feature.

## Requirements

1. Docker installed on the host machine
2. Network access to pull the Kibana image
3. Basic command-line knowledge

## Defense

Defensive measures and detection strategies:

- Monitor Docker container launches and image pulls for unauthorized Kibana instances
- Restrict access to Elastic repositories and implement image signing

## Objectives

1. Gain access to the headless Chromium binary
2. Prepare for exploit testing
3. Verify the vulnerable configuration

## Instructions

### Step 1: Launch Kibana Container

**Context**: Start the Docker container in interactive mode to enter a bash shell.

**Command** ([[commands/docker-run-kibana]]):
```bash
docker run --rm -it docker.elastic.co/kibana/kibana:7.12.0 bash
```

> This runs the Kibana 7.12.0 image, removes the container after exit, and provides an interactive terminal.

### Step 2: Navigate to Headless Shell Directory

**Context**: Change to the directory where the vulnerable headless_shell binary is located.

**Command** ([[commands/cd-to-headless-shell]]):
```bash
cd ./x-pack/plugins/reporting/chromium/headless_shell-linux_x64/
```

> This positions you to run the binary directly for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- None

## Commands Used

- [[commands/docker-run-kibana]]
- [[commands/cd-to-headless-shell]]

## Tools Used

- #docker

## Tags

- kibana
- docker
- setup
