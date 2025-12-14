---
tags:
  - docker
  - rails
  - execution
type: procedure
tools:
  - '[[tools/Docker]]'
  - '[[tools/Rails]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/docker-run-railspoc]]'
  - '[[commands/rails-server-production]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:16.346Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9bf5baa0-6465-45eb-a358-bab2f7f72a4f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Run-Vulnerable-Rails-Application-in-Docker

## Summary

This procedure starts the vulnerable Rails application inside a Docker container in production mode, mapping ports for local access to test exploitation.

## Description

The container runs the Rails server bound to all interfaces on port 3000, exposed via host port 8888. This simulates a deployable web app where sanitize configs allow the XSS bypass. Interactive mode allows monitoring logs during exploitation.

## Requirements

1. Built Docker image local/railspoc:latest
2. Host port 8888 free
3. Docker daemon running

## Defense

Defensive measures and detection strategies:

- Run containers with non-root users
- Use network isolation (e.g., no port exposure)
- Log container starts and monitor for vulnerable images

## Objectives

1. Launch container with port mapping
2. Start Rails server in production
3. Verify app accessibility

## Instructions

### Step 1: Run Docker Container

**Context**: Start the container interactively with port binding.

**Command** ([[commands/docker-run-railspoc]]):
```bash
docker run -it --rm -p 127.0.0.1:8888:3000 local/railspoc:latest
```

> Maps ports; expected: Container ID and startup.

### Step 2: Server Startup Inside Container

**Context**: The entrypoint runs the server.

**Command** ([[commands/rails-server-production]]):
```bash
./bin/rails server -b 0.0.0.0 -e production
```

> Binds to 0.0.0.0; expected: Server logs showing listening on 3000.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/docker-run-railspoc]]
- [[commands/rails-server-production]]

## Tools Used

- [[tools/Docker]]
- [[tools/Rails]]

## Tags

- docker
- execution
