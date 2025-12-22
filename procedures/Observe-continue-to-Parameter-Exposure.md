---
tags:
  - gitlab
  - parameter-exposure
  - error-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:26.205Z'
sub_techniques: []
id: 88a76b8e-f0a1-4b37-8d82-a662282db71b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Observe-continue-to-Parameter-Exposure

## Summary

This procedure involves triggering an import attempt without edit permissions to observe the continue[to] parameter in the error message, revealing potential redirect vulnerabilities.

## Description

By attempting to use the Repository Import feature on a project where the user only has view permissions, GitLab returns an error that inadvertently exposes the continue[to] parameter. This leakage occurs without requiring privileged access, providing insight into redirect mechanisms.

## Requirements

1. GitLab user with view-only permissions on a project
2. Access to the Repository Import page
3. Ability to inspect HTTP responses or error messages in the browser

## Defense

Defensive measures and detection strategies:

- Sanitize error messages to avoid parameter reflection
- Implement permission checks before processing redirects
- Monitor for anomalous error patterns in logs

## Objectives

1. Trigger permission-denied error in import workflow
2. Extract and analyze exposed parameters
3. Confirm vulnerability scope to view-level access

## Instructions

### Step 1: Initiate Import Without Permissions

**Context**: Simulate a failed import to generate error output.

Navigate to http://<instance>/<user>/<repository>/import and submit an import request (e.g., enter a dummy repository URL).

**Expected Output**: Error page with message 'You're not allowed to make changes to this project directly' and continue[to] parameter visible in the URL or response.

### Step 2: Inspect Parameter

**Context**: Document the exposed parameter for further exploitation.

View the page source or URL bar to note the continue[to]= value, which may reflect input or default to internal paths.

**Expected Output**: Parameter confirmed as manipulable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[parameter-exposure]]
- [[error-leak]]
