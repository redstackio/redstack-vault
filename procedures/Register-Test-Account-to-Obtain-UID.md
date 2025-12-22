---
tags:
  - registration
  - uid-enumeration
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:11.929Z'
sub_techniques: []
id: ae6eba6b-3efe-4822-a9df-fab83485d74c
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Register-Test-Account-to-Obtain-UID

## Summary

This procedure involves creating a test account on the target web application to monitor registration requests and extract the numeric User ID (UID), which is later used for IDOR exploitation.

## Description

In the context of the ASP.NET application at https://target.edu, registration exposes sequential numeric UIDs in responses, allowing attackers to predict and target other users' IDs. This step requires access to the public registration form and network monitoring tools. Prerequisites include a browser with dev tools. Expected outcome: UID for use in subsequent IDOR attacks.

## Requirements

1. Network access to https://target.edu
2. Browser with developer tools for request monitoring
3. Valid registration details (short password: 6-7 chars)

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on registration to deter automation
- Log and monitor registration spikes for anomalies
- Avoid exposing UIDs in responses; use opaque identifiers

## Objectives

1. Enumerate UID format and values
2. Establish baseline for account creation
3. Prepare for IDOR targeting

## Instructions

### Step 1: Access Registration Form

**Context**: Navigate to the registration page to begin account creation.

No specific command; use browser to fill form with test data (e.g., email: test@example.com, password: short123).

> Submit the form and monitor the network tab for the POST to /chkUser.aspx.

### Step 2: Extract UID from Response

**Context**: Capture the response to identify the assigned UID.

No command; inspect response body for numeric UID (e.g., "UID=12345").

> Successful response includes UID; note it for later steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[registration]]
- [[uid-enumeration]]
