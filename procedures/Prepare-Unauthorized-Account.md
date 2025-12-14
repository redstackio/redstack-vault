---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - gitlab
  - account
  - unauthorized
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:43.820Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-Unauthorized-Account

## Summary

This procedure involves logging into a secondary GitLab account without permissions to the target private project, simulating a victim user who will trigger the XSS during content viewing.

## Description

To exploit the redaction-based XSS, switch to an account lacking read access to the private project. This ensures the ReferenceRedactorFilter activates, unencoding the payload. Targets any GitLab user viewing public content. Prerequisites include two separate accounts; outcome is a session where private links appear redacted, injecting JS.

## Requirements

1. Secondary GitLab account without private project membership
2. Browser session for login
3. Verification of access denial to private URL

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication and account separation policies
- Log and alert on cross-account access attempts to private resources
- Use session isolation for different user roles

## Objectives

1. Establish a victim-like session for payload triggering
2. Confirm inaccessibility of private references
3. Set up for safe viewing of injected public content

## Instructions

### Step 1: Log Out and Sign In

**Context**: End the privileged session and start a new one with unauthorized credentials.

**Command** (UI Action):
No CLI; click user avatar > Sign out, then enter credentials for the secondary account at login page.

> Expected: Dashboard loads for the unauthorized user.

### Step 2: Verify Access Denial

**Context**: Test that the private project is inaccessible to confirm redaction trigger.

**Command** (UI Action):
Navigate to https://gitlab.com/username/private-project; expect 404 or permission error.

> Expected: Access denied message, ensuring filter activation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[account]]
