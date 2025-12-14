---
id: proc-uuid-2
tags:
  - ssrf
  - gitlab-ci
  - initial-run
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Cloud
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.568Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Initial-CI-Build-Run

## Summary

Execute the GitLab CI pipeline for the first time to verify benign behavior and confirm that initial SSRF protections prevent metadata access.

## Description

Push the commit containing the .gitlab-ci.yml and run.sh to the GitLab repository, triggering the pipeline. The build runs as intended: installs dependencies, runs tests, executes run.sh (which fails to access metadata due to protections), and packs the artifact. No internal metadata is leaked in logs.

## Requirements

1. Committed pipeline files in GitLab repo
2. Permissions to trigger builds
3. Access to CI logs

## Defense

- Log all CI executions and scan for anomalous network requests
- Enforce consistent SSRF mitigations across all runs

## Objectives

1. Confirm pipeline functionality without exploitation
2. Set stage for re-run bypass

## Instructions

### Step 1: Commit and Push Files

**Context**: Trigger the pipeline via Git push.

**Command** (git push):
```bash
git add .gitlab-ci.yml run.sh
 git commit -m "Add CI pipeline"
 git push origin main
```

> This starts the initial build. Monitor in GitLab UI.

### Step 2: Monitor Build Logs

**Context**: Verify no metadata exposure.

No command; observe logs showing successful npm install, test, and pack without internal data.

> Expected: Build passes, run.sh executes but curl fails silently due to protections.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- initial-run
