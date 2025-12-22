---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - verification
  - ui-access
  - denial
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.923Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Web-UI-Access-Denial

## Summary

This procedure tests anonymous access to the Weblate web UI after removing Guest permissions, confirming that the interface properly denies access to project details while setting up for API bypass testing.

## Description

As part of reproducing the Weblate vulnerability, this step uses a browser to attempt accessing a protected project URL. The UI enforcement serves as a control to isolate the issue to the API layer, where permissions are not checked. This is crucial for understanding the discrepancy in access controls within the Django framework.

## Requirements

1. Running Weblate instance on port 8000
2. Browser (e.g., Chrome, Firefox) for anonymous navigation
3. Knowledge of the test project URL (e.g., /projects/testproject/)

## Defense

Defensive measures and detection strategies:

- Audit UI and API permission middleware for consistency
- Log all anonymous access attempts to projects
- Use rate limiting on UI endpoints to prevent enumeration

## Objectives

1. Confirm UI correctly blocks anonymous access
2. Validate setup before API testing
3. Highlight vulnerability scope

## Instructions

### Step 1: Navigate to Project UI

**Context**: Attempt to view the project as an unauthenticated user to trigger denial.

Open a browser and go to http://192.168.1.129:8000/projects/testproject/ without logging in.

> Expected: Permission denied page or redirect to login.

### Step 2: Check for Details Exposure

**Context**: Ensure no partial information leaks in the denial response.

Inspect the page source or network tab for any unintended data exposure.

> Expected: No project metadata visible; clean denial message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[ui-access]]
- [[denial]]
