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
updated_at: '2025-12-13T23:52:39.279Z'
sub_techniques: []
id: f81c6eab-2723-4d27-9dcc-ce33ee3afbb4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Erase-Job-Logs-to-Prepare-Trigger

## Summary

This procedure deletes logs and artifacts from a specific job to create a dependency failure, priming the error message for XSS payload exposure.

## Description

By erasing artifacts from the build-job, subsequent test jobs dependent on it will fail artifact retrieval, displaying the malicious job name in an error context where v-safe-html fails to sanitize the data-disable-with attribute.

## Requirements

1. Completed pipeline with jobs having artifacts
2. Access to job details UI
3. Permissions to erase logs (project member)

## Defense

Defensive measures and detection strategies:

- Prevent artifact deletion without approval
- Audit log erasure events
- Sanitize error messages referencing job names

## Objectives

1. Remove dependencies to force error state
2. Expose malicious job name in UI
3. Set up for retry interaction

## Instructions

### Step 1: Navigate to Job Details

**Context**: Locate the job with artifacts to erase.

Go to CI/CD > Jobs, click on "build-job".

> Expected output: Job details page loads with logs.

### Step 2: Erase Logs and Artifacts

**Context**: Trigger deletion to break dependencies.

Click the trash icon (erase button) in the job interface.

> Expected output: Confirmation dialog; artifacts and logs removed upon success.

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
- erase
- artifacts
