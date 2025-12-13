---
tags:
  - setup
  - docker
  - poc
type: procedure
tools:
  - '[[tools/docker]]'
  - '[[tools/docker-compose]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/docker-compose-up-build]]'
platforms:
  - Linux
  - Node.js
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f6ae56ad-7462-4446-9189-5124bf787d7a
created_at: '2025-12-13T09:01:17.118Z'
updated_at: '2025-12-13T09:01:17.118Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
---
# Set Up PoC Environment for Node.js and ATS

## Summary

This procedure sets up a proof-of-concept environment using Docker to run a vulnerable Node.js server and ATS proxy for demonstrating HTTP Request Smuggling.

## Description

The setup involves unzipping a PoC archive and launching Docker containers that include a Node.js 16.3.0 server with llhttp parser and an ATS 9.0.0 proxy. This creates a local environment where the parsing mismatch can be exploited, with the server on port 8081 and proxy on 8080.

## Requirements

1. Docker and docker-compose installed on Linux host
2. poc.zip file available
3. Sudo access for docker-compose

## Defense

Defensive measures and detection strategies:

- Monitor Docker container logs for unusual startups
- Restrict Docker access to authorized users

## Objectives

1. Establish vulnerable environment
2. Ensure services are running on correct ports
3. Prepare for further testing and exploitation

## Instructions

### Step 1: Unzip and Start Containers

**Context**: Unzip the PoC files and build/start the Docker environment.

**Command** ([[commands/docker-compose-up-build]]):
```bash
sudo docker-compose up --build
```

> This command builds and starts the containers, setting up Node.js on 8081 and ATS on 8080.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques



### Sub-Techniques



## Commands Used

- [[commands/docker-compose-up-build]]

## Tools Used

- [[tools/docker]]
- [[tools/docker-compose]]

## Tags

- [[setup]]
- [[tools/docker]]
- [[poc]]
