---
id: proc-liberapay-team-create-001
tags:
  - team-creation
  - setup
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:47:18.340Z'
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
# Create-Liberapay-Team

## Summary

This procedure creates a new team on Liberapay to facilitate membership and subsequent exploitation of the leave endpoint.

## Description

After authentication, navigate to the teams section to create a team. This generates a team slug (e.g., 'jio') used in the vulnerable URL. The team must be joinable by the victim. No advanced features are required; a basic team suffices for the attack setup.

## Requirements

1. Authenticated Liberapay session
2. Web browser
3. Team name (e.g., 'jio')

## Defense

Defensive measures and detection strategies:

- Rate-limit team creation to prevent abuse
- Require email verification for team admins
- Log team creation events for anomaly detection

## Objectives

1. Generate a team URL for membership
2. Enable victim to join as a prerequisite for leave exploitation
3. Set up the vulnerable endpoint path

## Instructions

### Step 1: Navigate to Teams Page

**Context**: Access the team management interface.

No specific command; visit https://liberapay.com/about/teams in the browser.

> The page loads team creation form.

### Step 2: Submit Team Creation

**Context**: Create the team with a chosen name.

No specific command; fill and submit the form with name 'jio'.

> Team created; note the URL https://liberapay.com/jio for later use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- team-creation
- setup
