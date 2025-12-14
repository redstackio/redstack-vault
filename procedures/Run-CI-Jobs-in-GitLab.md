---
tags:
  - xss
  - gitlab
  - ci-cd
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.282Z'
sub_techniques: []
id: 32e32aed-2bc9-4c3f-8696-90529cdfe849
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-CI-Jobs-in-GitLab

## Summary

This procedure triggers and monitors the execution of the malicious CI pipeline to process job names containing XSS payloads.

## Description

Once the .gitlab-ci.yml is committed, GitLab automatically runs the pipeline if configured, or manually via UI. Jobs execute simple echo scripts, ensuring completion and log generation, which sets the stage for later error triggers involving the unsanitized job names.

## Requirements

1. Committed .gitlab-ci.yml with malicious jobs
2. GitLab UI access
3. Pipeline triggers enabled

## Defense

Defensive measures and detection strategies:

- Validate job names for HTML/JS patterns before pipeline execution
- Log and alert on suspicious script outputs
- Rate-limit pipeline runs

## Objectives

1. Execute jobs to embed payloads in GitLab's internal state
2. Generate logs and artifacts for dependency setup
3. Confirm pipeline success

## Instructions

### Step 1: Trigger Pipeline

**Context**: Initiate the CI run to process jobs.

Navigate to the project's CI/CD > Pipelines tab and click "Run Pipeline" if manual, or push a commit.

> Expected output: Pipeline starts, jobs queue.

### Step 2: Monitor Job Completion

**Context**: Wait for all stages to finish, verifying no errors in execution.

View the Jobs tab; jobs should show "passed" with echo outputs.

> Expected output: Green status for build and test stages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- gitlab
- pipeline
