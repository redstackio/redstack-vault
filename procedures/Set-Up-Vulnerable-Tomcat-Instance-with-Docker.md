---
tags:
  - setup
  - docker
  - tomcat
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/docker-run-tomcat-vulnerable]]'
platforms:
  - Linux
  - Docker
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 61d685a2-0b1a-469b-8e3d-d43d7991863b
created_at: '2025-12-13T09:01:22.426Z'
updated_at: '2025-12-13T09:01:22.426Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set Up Vulnerable Tomcat Instance with Docker

## Summary

This procedure sets up a vulnerable Apache Tomcat instance using Docker to reproduce the HTTP Request Smuggling vulnerability for testing and exploitation purposes.

## Description

The procedure involves running a Docker container with Tomcat version 10.1.13, which is susceptible to request smuggling due to improper trailer header parsing. This setup allows for local reproduction of the vulnerability in a controlled environment, mapping host port 43022 to the container's port 8080.

## Requirements

1. Docker installed on a Linux host
2. Access to Docker Hub for pulling the tomcat:10.1.13 image
3. Local network access for port mapping

## Defense

Defensive measures and detection strategies:

- Use updated Tomcat versions that patch CVE-2023-45648
- Monitor Docker container deployments for vulnerable images

## Objectives

1. Deploy a vulnerable Tomcat server
2. Ensure the server is accessible for exploitation
3. Prepare environment for request smuggling tests

## Instructions

### Step 1: Launch Docker Container

**Context**: Run the Docker command to start the vulnerable Tomcat instance.

**Command** ([[commands/docker-run-tomcat-vulnerable]]):
```bash
docker run -d --name hrs_tomcat_11 -p 43022:8080 tomcat:10.1.13
```

> This command runs the container in detached mode, names it hrs_tomcat_11, and maps ports for access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/docker-run-tomcat-vulnerable]]

## Tools Used

- [[tools/Docker]]

## Tags

- [[setup]]
- [[tools/Docker]]
- [[tomcat]]
