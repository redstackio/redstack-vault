---
tags:
  - auth-bypass
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:48.314Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 1b598a85-7ac1-4bdc-837e-5e5c3d3bb751
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Confirm-Report-Submission-Ban

## Summary

This procedure verifies that the account ban is active by attempting to submit a report through the standard UI or direct request, expecting a failure.

## Description

After receiving ban confirmation, attempt to create a vulnerability report directly via the HackerOne web interface or a simple HTTP request. This step confirms that UI/GraphQL-based restrictions are enforced, setting the stage for API bypass. The target environment is the HackerOne web platform, and success is indicated by a 403 Forbidden response.

## Requirements

1. Banned HackerOne account
2. Web browser or HTTP client
3. Access to report creation UI

## Defense

Defensive measures and detection strategies:

- Ensure consistent ban enforcement across all endpoints
- Log failed submission attempts
- Alert on repeated ban confirmation tests

## Objectives

1. Validate ban activation on UI paths
2. Identify enforcement gaps for API
3. Expected outcome: 403 error on submission

## Instructions

### Step 1: Attempt UI Report Creation

**Context**: Use the HackerOne dashboard to try submitting a test report.

**Command** (Manual UI action):

Log in and navigate to create a new report for any program.

> Fill in basic details and submit. Expected output: 403 Forbidden error, preventing report creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- hackerone
