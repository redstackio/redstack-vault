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
updated_at: '2025-12-13T23:52:39.277Z'
sub_techniques: []
id: 1b673847-1956-4cba-81c8-5f1d24e6953a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Retry-Job-to-Generate-Error

## Summary

This procedure retries a dependent job after artifact erasure, generating an error message that includes the unsanitized malicious job name.

## Description

Retrying the "trigger-xss" job fails due to missing artifacts from the erased job, rendering an error like "This job could not start because it could not retrieve the needed artifacts: [malicious job name]", where the payload in data-disable-with is processed.

## Requirements

1. Erased artifacts from prerequisite job
2. Access to job list UI
3. Permissions to retry jobs

## Defense

Defensive measures and detection strategies:

- Sanitize job references in error serializers (e.g., BuildDetailsEntity)
- Log retry failures with payload inspection
- Disable retries for failed dependencies

## Objectives

1. Force error rendering with malicious content
2. Display payload in clickable UI element
3. Prepare for victim interaction

## Instructions

### Step 1: Return to Job List

**Context**: Select the dependent job for retry.

Navigate to CI/CD > Jobs.

> Expected output: List of jobs visible.

### Step 2: Initiate Retry

**Context**: Trigger the failure state.

Click on "trigger-xss" job, then click the Retry button.

> Expected output: Error modal appears with artifact message containing job name.

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
- retry
- error
