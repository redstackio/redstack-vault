---
id: proc-add-unauthorized-participant
tags:
  - access-grant
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.577Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Unauthorized-Participant-to-Report

## Summary

This procedure adds an unauthorized user as a participant to a HackerOne report, granting them limited access that can be exploited to query sensitive internal data via APIs.

## Description

As part of the information disclosure attack on HackerOne, the team owner adds the attacker's account to the report. This simulates a scenario where a non-team member gains participant status, allowing API access without full team privileges. The target is the HackerOne web interface, requiring owner access. Outcomes include the attacker viewing basic report details and querying endpoints.

## Requirements

1. Team owner access to the target report
2. Attacker's HackerOne username
3. Report ID from prior setup

## Defense

Defensive measures and detection strategies:

- Audit participant additions for approval workflows
- Log and alert on additions by non-admins

## Objectives

1. Grant partial access to unauthorized user
2. Enable API queries from participant account
3. Set up for disclosure exploitation

## Instructions

### Step 1: Navigate to Report Participants

**Context**: Access the report management section to add users.

Log in as team owner, open the report, and go to the Participants tab.

> This displays current participants and an add option.

### Step 2: Add Attacker as Participant

**Context**: Input the attacker's details to grant access.

Enter the attacker's username, select participant role, and confirm addition.

> Attacker receives an invitation; upon acceptance, they can view the report but not internal team areas.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-grant
- hackerone
