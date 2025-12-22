---
tags:
  - docker
  - reconnaissance
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/browse-docker-hub-tags]]'
platforms:
  - Cloud
  - Docker
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3f31d939-a5db-4167-b051-6cfe7802436d
created_at: '2025-12-14T17:31:42.966Z'
updated_at: '2025-12-14T17:31:42.966Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Browse-Docker-Hub-for-TaskCluster-Image-Tags

## Summary

This procedure involves scanning Docker Hub for available image tags in the TaskCluster repository to identify potential targets for secret extraction.

## Description

In the context of supply chain attacks, public container registries like Docker Hub can expose sensitive data in image metadata or tags. This step uses web browsing or API queries to enumerate tags for the taskcluster/taskcluster repository, focusing on older versions likely to contain unpatched vulnerabilities like hardcoded tokens.

## Requirements

1. Internet access to Docker Hub
2. Basic command-line tools like curl and jq for parsing
3. No authentication needed for public repos

## Defense

Defensive measures and detection strategies:

- Monitor Docker Hub for anomalous pulls or scans
- Use private repositories for sensitive images
- Implement image scanning tools like Trivy for secrets

## Objectives

1. Identify vulnerable image tags
2. Prepare for image pulling
3. Map the attack surface of public artifacts

## Instructions

### Step 1: Access Docker Hub Repository

**Context**: Navigate to the tags page to list available images.

**Command** ([[commands/browse-docker-hub-tags]]):
```bash
echo "Visit https://hub.docker.com/r/taskcluster/taskcluster/tags" && curl -s https://hub.docker.com/v2/repositories/taskcluster/taskcluster/tags/?page_size=100 | jq '.results[].name'
```

> This command outputs a list of tags. Manually visit the URL if curl is unavailable. Expected output includes tags like v15.0.0-20-g0eca18b7c.

### Step 2: Select Target Tags

**Context**: Choose tags based on version history, prioritizing older ones.

No specific command; review output and note tags such as c061025dc, ba7958766.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/browse-docker-hub-tags]]

## Tools Used

- [[tools/curl]]

## Tags

- docker-hub
- tag-enumeration
