---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - setup
  - shopify
  - team-management
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
updated_at: '2025-12-14T17:24:56.413Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Removed-Team-Member-in-Shopify

## Summary

This procedure sets up a test environment by inviting a user to a Shopify Partner Team and then removing them, simulating a past team member for testing information disclosure.

## Description

In the context of Shopify's Partner Dashboard, this involves using owner privileges to manage team invitations and removals. The target is the team management interface at https://partners.shopify.com. Prerequisites include owner access to a Partner Team (e.g., Team_ABC). Expected outcome is a removed member whose PII can be tested for exposure.

## Requirements

1. Owner-level credentials for Shopify Partner Dashboard
2. Valid email for test user (STAFF1)
3. Access to email for invitation acceptance

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to restrict invitation/removal actions to admins
- Log all team management actions for anomaly detection (e.g., frequent invites/removals)
- Use audit trails to monitor access to removed members data

## Objectives

1. Create a removed team member for vulnerability testing
2. Ensure removal logs PII like name, email, and date
3. Prepare environment for unauthorized access simulation

## Instructions

### Step 1: Invite Test User

**Context**: Send invitation to join the Partner Team.

Navigate to the Partner Dashboard team section and invite STAFF1 to Team_ABC, assigning basic permissions.

> Invitation is sent via email; no command required, manual UI action.

### Step 2: Accept Invitation

**Context**: Have the test user join the team.

STAFF1 accepts via email link or dashboard login.

> Successful join confirms active membership.

### Step 3: Remove Test User

**Context**: Simulate ex-staff by removing from team.

As owner, select removal in the dashboard UI for STAFF1.

> Removal records date and disassociates from team.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[setup]]
- [[shopify]]
- [[team-invite]]
