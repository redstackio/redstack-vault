---
tags:
  - graphql
  - setup
  - hackerone
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.473Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c8a3e305-0542-4d4f-b6f7-0eae7fe2fb01
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Report-to-Obtain-ID

## Summary

This procedure sets up a controlled environment in HackerOne by creating a test program and submitting a report to obtain a valid report ID, which is encoded for use in GraphQL mutations. It is a prerequisite for exploiting invitation system vulnerabilities without affecting real reports.

## Description

In the context of testing HackerOne's bug bounty platform, an authenticated user creates a private test program and submits a dummy report. The report's numeric ID (e.g., 626371) is retrieved from the UI or API, then converted to a base64-encoded Global ID format required by GraphQL. This step ensures the exploit targets a non-sensitive report, minimizing risk during reproduction. The vulnerability discovery involved this setup to craft mutations safely.

## Requirements

1. Authenticated HackerOne account with program creation permissions.
2. Web browser or API access to hackerone.com.
3. Base64 encoding tool (e.g., online encoder or command-line base64).

## Defense

Defensive measures and detection strategies:

- Monitor for unusual program/report creation patterns from low-privilege accounts.
- Implement rate limiting on report submissions to prevent abuse in testing scenarios.

## Objectives

1. Acquire a valid, controllable report ID for mutation testing.
2. Ensure setup does not impact production data.
3. Prepare encoded ID for GraphQL exploitation.

## Instructions

### Step 1: Create Test Program

**Context**: Log in and establish a test program to host the report.

No specific command; use HackerOne UI: Navigate to Programs > New Program, set as private/test, save to get program handle.

> Successful creation shows program dashboard.

### Step 2: Submit Test Report

**Context**: Submit a benign report within the test program to generate an ID.

Use UI: Go to the program > New Report, enter dummy details (e.g., "Test vulnerability report"), submit.

> Report submission redirects to /reports/{ID}, e.g., /reports/626371.

### Step 3: Encode Report ID

**Context**: Convert the numeric ID to base64 Global ID format.

Use command-line or tool: Prefix ID with "gid://hackerone/Report/" then base64 encode.

```bash
echo -n "gid://hackerone/Report/626371" | base64
```

> Output: Z2lkOi8vaGFja2Vyb25lL1JlcG9ydC82MjYzNzE=.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[graphql]]
- [[setup]]
- [[hackerone]]
