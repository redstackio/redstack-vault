---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - setup
  - docker
  - api
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.862Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Set-Up-TalentMAP-API-Environment

## Summary

This procedure builds and launches the TalentMAP API in a Docker container to create a local testing environment for IDOR exploitation, following instructions from a prior vulnerability report.

## Description

The TalentMAP API, built on Django and Python, is vulnerable to IDOR in its permission endpoint. Setting up the environment involves containerizing the application to isolate it and ensure reproducibility. This step is essential for controlled testing without affecting production systems. Prerequisites include Docker installed on the host machine and access to the build instructions from report #1809328.

## Requirements

1. Docker installed and running on the host
2. Access to source code or build artifacts for TalentMAP API
3. Basic familiarity with Docker commands

## Defense

Defensive measures and detection strategies:

- Monitor Docker image pulls and container startups for unauthorized environments
- Implement API gateway restrictions on local deployments
- Use container scanning tools to detect vulnerable images

## Objectives

1. Establish a running instance of the vulnerable API
2. Verify accessibility on localhost:8000
3. Prepare for database population

## Instructions

### Step 1: Build the Docker Image

**Context**: Use the provided build instructions to create the container image for the API.

No specific command; follow report #1809328 guidelines to docker build the image.

> This compiles the Django application into a runnable container. Expected output: Successful image build confirmation.

### Step 2: Run the Container

**Context**: Launch the container to expose the API service.

No specific command; docker run with port mapping to 8000.

> Starts the API server. Expected output: Container running, API responsive at http://localhost:8000.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- setup
- docker
- environment
