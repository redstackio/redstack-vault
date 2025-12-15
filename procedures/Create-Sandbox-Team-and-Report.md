---
id: proc-create-sandbox-team-report
tags:
  - setup
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
updated_at: '2025-12-14T17:30:35.579Z'
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
# Create-Sandbox-Team-and-Report

## Summary

This procedure sets up a sandbox team and report on HackerOne to simulate an environment for testing information disclosure vulnerabilities, allowing controlled internal actions without affecting production.

## Description

In the context of exploiting HackerOne's internal activity disclosure, this initial setup creates a new team in sandbox mode and submits a report. This establishes a report ID that can be used for participant addition and API queries. The target environment is the HackerOne web platform, requiring a valid account with team creation privileges. Expected outcomes include obtaining a unique report ID for subsequent exploitation steps.

## Requirements

1. Valid HackerOne account with permissions to create teams
2. Access to sandbox mode (available in HackerOne settings)
3. Internet connectivity to the HackerOne web interface

## Defense

Defensive measures and detection strategies:

- Monitor team and report creation logs for unusual sandbox usage
- Implement rate limiting on team creation to prevent abuse in testing

## Objectives

1. Establish a controlled testing environment
2. Generate a report ID for vulnerability reproduction
3. Ensure isolation from production data

## Instructions

### Step 1: Create Sandbox Team

**Context**: Log in as the victim and enable sandbox mode to create a non-production team.

Navigate to the HackerOne dashboard, go to Teams > Create Team, and select sandbox mode. Provide team details and submit.

> This creates a team isolated for testing, visible only to the owner initially.

### Step 2: Submit Test Report

**Context**: Within the new team, create a report to serve as the target for the attack.

From the team dashboard, select Submit Report, fill in dummy vulnerability details, and submit to generate a report ID.

> Successful submission returns a report page with an ID like #123456, ready for participant addition.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- hackerone
