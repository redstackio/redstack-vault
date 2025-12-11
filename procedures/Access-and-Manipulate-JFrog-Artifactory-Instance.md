---
tags:
  - supply-chain
  - artifact-manipulation
type: procedure
tools:
  - '[[tools/Git]]'
  - '[[tools/Grep]]'
  - '[[tools/Curl]]'
  - '[[tools/JFrog-CLI]]'
tactics:
  - '[[Persistence]]'
  - '[[Discovery]]'
commands: []
platforms:
  - JFrog Artifactory
techniques:
  - '[[Supply Chain Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Compromise Software Supply Chain]]'
id: 3fcbfdc4-e50a-412d-b75d-adf95519841b
created_at: '2025-12-11T03:47:56.550Z'
updated_at: '2025-12-11T03:47:56.550Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1195]]'
---
# Access and Manipulate JFrog Artifactory Instance

## Summary

This procedure uses validated credentials to access internal artifacts in JFrog Artifactory and demonstrate push capabilities, highlighting risks of supply chain compromise.

## Description

With authenticated access, browse and download internal libraries, then test uploading updates to existing artifacts. This can lead to injecting malicious code into production pipelines. The target is a web-based Artifactory service.

## Requirements

1. Validated Artifactory credentials
2. JFrog CLI installed and configured
3. Test file for upload demonstration

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) in Artifactory
- Monitor for unauthorized uploads or accesses in logs
- Use immutable repositories for critical artifacts

## Objectives

1. Access internal artifacts
2. Demonstrate update/push capabilities
3. Assess supply chain impact

## Instructions

### Step 1: Search for Artifacts

**Context**: List available artifacts to identify targets.

**Command** ([[commands/jfrog-cli-push-artifact]]): First, search:
```bash
jfrog rt search --recursive
```

> This lists all accessible artifacts.

### Step 2: Push Update to Artifact

**Context**: Upload a test file to demonstrate manipulation.

**Command** ([[commands/jfrog-cli-push-artifact]]):
```bash
jfrog rt upload test-file.txt repo-name/
```

> This pushes the file, confirming write access.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]
- [[Discovery]]

### Techniques

- [[Supply Chain Compromise]]

### Sub-Techniques

- [[Compromise Software Supply Chain]]

## Commands Used

- [[commands/jfrog-cli-push-artifact]]

## Tools Used

- [[tools/JFrog-CLI]]

## Tags

- [[Supply Chain Compromise]]
- #artifact-manipulation
