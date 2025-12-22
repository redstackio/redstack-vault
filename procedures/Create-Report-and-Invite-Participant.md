---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - dos
  - social-engineering
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.804Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Report-and-Invite-Participant

## Summary

This procedure creates a dummy vulnerability report on HackerOne and invites an account with the oversized filename profile picture as a participant, ensuring the payload is included in GraphQL-fetched participant data.

## Description

HackerOne's report system allows users to create reports and add participants via a dedicated endpoint. By inviting the exploited account, the oversized filename becomes part of the JSON data returned by queries to /reports/<report-id>/participants/, amplifying the DoS when multiple users or pages load this data.

## Requirements

1. Authenticated HackerOne account with report creation permissions
2. Knowledge of the affected account's username or ID
3. Access to the reports interface

## Defense

Defensive measures and detection strategies:

- Limit participant invitations to verified relationships or rate-limit additions
- Sanitize user data in report queries to exclude oversized fields
- Audit report creation for abuse patterns, such as rapid dummy report submissions

## Objectives

1. Generate a test report to serve as a trigger point
2. Add the affected participant to include their profile data
3. Set up for DoS observation in report-related pages

## Instructions

### Step 1: Create Dummy Report

**Context**: Establish a report that can reference participants.

Navigate to the reports creation page on HackerOne and submit a benign, dummy vulnerability report (e.g., a low-severity test case). Note the generated report ID (e.g., #654270).

### Step 2: Invite Participant

**Context**: Link the affected account to the report.

Go to https://hackerone.com/reports/<report-id>/participants/ and enter the username of the account with the oversized filename. Submit the invitation.

**Expected Output**: Participant added to the list; confirmation message displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- dos
- report-invitation
- participant-list
