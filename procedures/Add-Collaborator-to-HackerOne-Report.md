---
tags:
  - hackerone
  - collaborator-addition
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ruby-redact-pii]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d597cede-ffc6-47d3-b0e8-24e81129e475
created_at: '2025-12-11T06:10:15.680Z'
updated_at: '2025-12-11T06:10:15.680Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1592]]'
---
# Add Collaborator to HackerOne Report

## Summary

This procedure adds a target hacker as a collaborator to a HackerOne report, setting up for invitation and potential email disclosure.

## Description

Using the report's collaboration interface, enter the username or email of the target. This step is limited to 2 invites per report and is a precursor to sending invitations and capturing leaky GraphQL requests.

## Requirements

1. Existing dummy report on HackerOne.
2. Target hacker's username.
3. Access to the report editing features.

## Defense

Defensive measures and detection strategies:

- Audit collaborator addition logs for anomalies.
- Require verification for collaborator invites.

## Objectives

1. Populate the collaborator list with targets.
2. Prepare for invitation sending.
3. Facilitate GraphQL request triggering.

## Instructions

### Step 1: Access Collaborator Settings

**Context**: Edit the report to add collaborators.

Navigate to the report and click on the collaborators section.

> Search for the target username.

### Step 2: Add the User

**Context**: Input and confirm the addition.

Enter the username and add to the list.

> User appears in pending invites.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[hackerone]]
- [[collaborator-addition]]
