---
tags:
  - setup
  - docker
  - tomcat
type: procedure
tools:
  - '[[tools/git]]'
  - '[[tools/cd]]'
  - '[[tools/docker-compose]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-repository]]'
  - '[[commands/cd-directory]]'
  - '[[commands/docker-compose-build]]'
  - '[[commands/docker-compose-up]]'
platforms:
  - Linux
  - Docker
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b7ceb90d-ee50-497a-83a3-6080228abff8
created_at: '2025-12-13T09:01:22.377Z'
updated_at: '2025-12-13T09:01:22.377Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Vulnerable Tomcat Environment

## Summary

This procedure sets up a vulnerable Apache Tomcat environment using Docker to reproduce the HTTP request smuggling vulnerability via oversized trailer headers.

## Description

The setup involves cloning a GitHub repository that contains Docker configurations for a vulnerable Tomcat server (version 9.0.82). This environment allows safe testing of the vulnerability without affecting production systems. The technical approach uses Docker Compose to build and run containers, exposing Tomcat on port 8082.

## Requirements

1. Git installed
2. Docker and Docker Compose installed
3. Access to GitHub for cloning
4. Linux-based system

## Defense

Defensive measures and detection strategies:

- Monitor Docker container logs for unusual activity
- Use network segmentation to isolate test environments
- Regularly update Tomcat to patched versions

## Objectives

1. Create a reproducible vulnerable environment
2. Ensure Tomcat is running and accessible
3. Prepare for payload crafting and exploitation

## Instructions

### Step 1: Clone Repository

**Context**: Obtain the setup files for the vulnerable Tomcat environment.

**Command** ([[commands/git-clone-repository]]):
```bash
git clone https://github.com/oss-aimoto/tomcat-trailer.git
```

> Clones the repository containing Docker files and scripts.

### Step 2: Change Directory

**Context**: Navigate into the cloned repository directory.

**Command** ([[commands/cd-directory]]):
```bash
cd tomcat-trailer
```

> Changes the working directory to access Docker Compose files.

### Step 3: Build Docker Images

**Context**: Build the necessary Docker images for Tomcat.

**Command** ([[commands/docker-compose-build]]):
```bash
docker-compose build
```

> Builds images based on docker-compose.yml.

### Step 4: Start Containers

**Context**: Run the Docker containers to start the vulnerable server.

**Command** ([[commands/docker-compose-up]]):
```bash
docker-compose up -d
```

> Starts containers in detached mode.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/git-clone-repository]]
- [[commands/cd-directory]]
- [[commands/docker-compose-build]]
- [[commands/docker-compose-up]]

## Tools Used

- [[tools/git]]
- [[tools/cd]]
- [[tools/docker-compose]]

## Tags

- [[setup]]
- [[docker]]
- [[tomcat]]
