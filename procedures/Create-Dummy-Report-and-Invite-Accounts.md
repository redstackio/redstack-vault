---
tags:
  - dos
  - graphql
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ebc02270-cc8c-4626-85be-48b9e97e5691
created_at: '2025-12-11T06:10:22.281Z'
updated_at: '2025-12-11T06:10:22.281Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
---
# Create Dummy Report and Invite Accounts

## Summary

This procedure creates a test report and invites affected user accounts to propagate malicious data, triggering oversized responses in backend queries for denial of service.

## Description

On platforms like HackerOne, creating a report and inviting users with oversized profile filenames causes GraphQL endpoints to return large responses, leading to timeouts and service disruption for participants.

## Requirements

1. Access to report creation features
2. Knowledge of affected accounts with malicious profiles
3. Web access to the platform

## Defense

Defensive measures and detection strategies:

- Validate and sanitize data in GraphQL resolvers
- Detect rapid report creations or invitations

## Objectives

1. Trigger GraphQL queries with large data
2. Cause response timeouts
3. Amplify DoS impact

## Instructions

### Step 1: Create Report

**Context**: Initiate a new report to serve as a vector for invitations.

Navigate to the report creation page and submit a dummy report.

> Obtain the report ID for further actions.

### Step 2: Invite Affected Accounts

**Context**: Add users with oversized filenames to the report.

Use the invitation feature to add accounts, triggering queries to /reports/<report-id>/participants/.

> This propagates the large filenames into responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[dos]]
- [[graphql]]
