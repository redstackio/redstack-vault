---
id: proc-slack-verify-credits
name: Verify-Multiple-Credits
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.290Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - race-condition
  - web
  - slack
  - financial-gain
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Verify-Multiple-Credits

## Summary

This procedure validates the success of the race condition exploit by checking the Slack account for multiple applied $100 promotional credits from duplicate survey completions.

## Description

After concurrent request replay, the lack of synchronization allows the server to process each submission independently, awarding credits per completion. Access the account's billing or workspace settings to view the credits balance. This step confirms financial impact and can be done via the web interface. No tools beyond a browser are needed, and it serves as the final validation in the attack chain.

## Requirements

1. Active Slack session from the exploited account
2. Access to billing or credits section (may require workspace admin)
3. Browser for navigation

## Defense

Defensive measures and detection strategies:

- Audit logs for credit applications tied to survey events
- Reconcile credits against unique user actions
- Automated checks for anomalous credit balances post-registration
- User notifications for unexpected credit awards

## Objectives

1. Confirm duplicate survey processing
2. Quantify financial gain (e.g., $200 from two credits)
3. Validate overall exploit success

## Instructions

### Step 1: Log into Slack Account

**Context**: Ensure session is active from the creation process.

Visit https://yourteam.slack.com and log in if needed.

> Dashboard should load with the new workspace.

### Step 2: Check Credits Section

**Context**: Navigate to where promotional credits are displayed.

Go to Workspace settings > Billing or Promotions tab.

> Look for entries showing multiple $100 credits applied around the survey completion time.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[race-condition]]
- [[web]]
- [[slack]]
- [[financial-gain]]
