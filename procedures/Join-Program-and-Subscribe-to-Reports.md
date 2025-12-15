---
id: proc-001-join-subscribe
tags:
  - access-control
  - subscription
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:28.266Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Join-Program-and-Subscribe-to-Reports

## Summary

This procedure establishes a legitimate subscriber relationship to reports in a HackerOne program, setting the stage for demonstrating persistent access flaws.

## Description

In the context of the HackerOne platform, users join programs to participate in bug bounty activities. Upon joining, they can subscribe to report notifications, creating a backend relationship between the User object and the Report model. This is typically automatic or manual via UI, using Ruby on Rails associations. The procedure assumes a valid account and targets web-based interactions.

## Requirements

1. Valid HackerOne account credentials
2. Internet access to the HackerOne platform
3. Target program invitation or public join option

## Defense

Defensive measures and detection strategies:

- Implement strict subscriber cleanup on program exit
- Log all subscription changes for auditing
- Use role-based access controls to limit notification scopes

## Objectives

1. Gain authorized access to program reports
2. Establish persistent subscriber link
3. Prepare for removal testing

## Instructions

### Step 1: Log In and Navigate to Program

**Context**: Authenticate and locate the target program dashboard.

Log in to HackerOne at https://hackerone.com using valid credentials. Search for and select the target program.

### Step 2: Join the Program

**Context**: Become a member to enable subscription features.

Click 'Join Program' or accept invitation. Confirm membership in the dashboard.

### Step 3: Subscribe to Reports

**Context**: Activate notifications for report updates.

In program settings or report view, enable subscriptions. This adds the user to the Report model's subscribers association.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control
- subscription
