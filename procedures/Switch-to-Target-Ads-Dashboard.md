---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - account-switching
  - twitter
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:36.737Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Switch-to-Target-Ads-Dashboard

## Summary

This procedure allows a user with delegated access to switch into the target account's Ads & Analytics dashboard, providing a foothold for further exploitation without full owner credentials.

## Description

Twitter's multi-account management feature enables users with assigned roles to switch between accounts seamlessly. This step uses the previously assigned Ad Manager role to access the target's dashboard, where promotional tweet creation is possible. It targets the web interface at ads.twitter.com and assumes the role assignment from prior steps.

## Requirements

1. Assigned Ad Manager role on the target account
2. Logged-in session for the secondary user
3. Browser with cookies intact for session management

## Defense

Defensive measures and detection strategies:

- Monitor session switches and log IP/user agent anomalies
- Enforce session timeouts for delegated access
- Alert on frequent account switches by non-owners

## Objectives

1. Gain dashboard access using limited role
2. Set up for tweet composition in the target context
3. Validate role propagation

## Instructions

### Step 1: Log In as Assigned User

**Context**: Ensure the secondary user is authenticated.

Log in to Twitter as the assigned user (e.g., abtest66).

> Dashboard for the user's own account loads.

### Step 2: Initiate Account Switch

**Context**: Use the switch feature to select the target.

Click 'Switch accounts' and choose the target account (e.g., abtest67).

> The interface redirects to the target's Ads dashboard, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-switch
- delegation
- ads-analytics
