---
id: proc-verify-deletion
tags:
  - verification
  - impact-assessment
  - fabric-io
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.768Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Member-Deletion

## Summary

Confirm the success of the unauthorized deletion by inspecting the victim organization's team members as the original admin.

## Description

Log in as Victimadmin to VictimOrg settings and check the team list. The absence of Victimmember validates the exploit. This step assesses the impact on organization management in Fabric.io.

## Requirements

1. Victimadmin credentials
2. Access to VictimOrg dashboard

## Defense

Defensive measures and detection strategies:

- Enable notifications for member removals
- Review audit logs for unexpected changes

## Objectives

1. Validate exploit efficacy
2. Measure disruption to team access
3. Identify any residual traces

## Instructions

### Step 1: Login and Check Team

**Context**: Access the org to observe changes.

Log in as Victimadmin, navigate to VictimOrg > Settings > Team members.

**Expected Output**: Victimmember missing from list; only Victimadmin remains.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[impact-assessment]]
