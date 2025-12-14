---
tags:
  - docker
  - inspection
  - secrets
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/docker-inspect-image-file]]'
platforms:
  - Docker
  - Linux
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials In Files]]'
id: bbdeb50b-8d60-4694-98cc-99fc603f4f5b
created_at: '2025-12-14T17:31:42.945Z'
updated_at: '2025-12-14T17:31:42.945Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
---
# Inspect-Docker-Images-for-Hardcoded-Secrets

## Summary

This procedure examines the filesystem of Docker images to locate and extract hardcoded authentication tokens or other secrets.

## Description

Container images often bundle dependencies like npm packages that may contain test credentials. In this case, the sentry-api package's test.js file includes a live token, allowing attackers to search specific paths for sensitive data.

## Requirements

1. Pulled Docker images available
2. Docker runtime
3. Basic grep knowledge

## Defense

Defensive measures and detection strategies:

- Use secret scanning in CI/CD pipelines (e.g., GitGuardian)
- Remove test files from production builds
- Sign and verify images

## Objectives

1. Locate the token in node_modules
2. Extract the secret value
3. Assess exposure risk

## Instructions

### Step 1: Run Container and Extract File

**Context**: Mount or run the image to access internal files without full execution.

**Command** ([[commands/docker-inspect-image-file]]):
```bash
docker run --rm -it taskcluster/taskcluster:v15.0.0-20-g0eca18b7c cat /app/node_modules/sentry-api/test.js | grep -i token
```

> Outputs the line with the token: 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9. Repeat for other tags.

### Step 2: Save Extracted Secret

**Context**: Store the token for later use.

**Command**:
```bash
echo "5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9" > sentry_token.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used

- [[commands/docker-inspect-image-file]]

## Tools Used

- [[tools/Docker]]

## Tags

- file-inspection
- credential-theft
