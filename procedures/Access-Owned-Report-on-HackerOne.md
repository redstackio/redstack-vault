---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - access-control
  - hackerone
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:26:27.590Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Owned-Report-on-HackerOne

## Summary

This procedure outlines how to log in to the HackerOne platform and access a report owned by the authenticated user, setting the stage for further actions like inviting collaborators in an attack chain targeting access control flaws.

## Description

In the context of testing improper access control on HackerOne, this initial step ensures the attacker has a valid entry point into a specific report. The platform requires authentication, but once inside an owned report, subsequent API calls may lack proper checks. This procedure assumes a standard web browser interaction and targets the HackerOne web application.

## Requirements

1. Valid HackerOne account with at least one owned report.
2. Web browser (e.g., Chrome, Firefox) with internet access.
3. No special tools needed for this step.

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to restrict report access to owners only.
- Log all report access attempts and monitor for anomalous user behavior.

## Objectives

1. Gain access to a user-owned report to enable collaborator management.
2. Verify authentication and report visibility.
3. Prepare for invitation process without triggering alerts.

## Instructions

### Step 1: Log In to HackerOne

**Context**: Authenticate to the platform to access personal reports.

Navigate to https://hackerone.com and log in with valid credentials. Upon successful login, the dashboard will display owned reports.

### Step 2: Select and Open Report

**Context**: Choose a report to target for the vulnerability test.

From the reports list, click on one owned by the user (e.g., via https://hackerone.com/reports/<id>). The page should load with full management options, including collaborators.

**Expected Output**: Report details page with participant management UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-control]]
- [[hackerone]]
