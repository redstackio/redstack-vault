---
tags:
  - authentication
  - user-invite
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.977Z'
skill_level: basic
impact_level: low
sub_techniques: []
id: 4f16f809-e182-4288-bd6e-4562f6e4d58e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Invite-and-Authenticate-Test-User

## Summary

This procedure invites a test user to the sandbox program with limited permissions and authenticates them to simulate an authorized but scoped actor in the access control test.

## Description

To reproduce the vulnerability, a secondary user (User B) is granted 'Report' and 'Engagement' access, allowing interaction with reports but not full admin privileges. This setup tests if limited users can be leveraged for cross-program actions. Authentication uses standard HackerOne login flows.

## Requirements

1. Created sandbox program from prior procedure
2. Secondary HackerOne account for User B
3. Email access for invitation

## Defense

Defensive measures and detection strategies:

- Audit invitation logs for anomalous patterns
- Limit invitation scopes to verified users
- Implement approval workflows for program access

## Objectives

1. Grant scoped access to simulate restricted user
2. Ensure User B can engage with reports
3. Prepare for request interception

## Instructions

### Step 1: Generate Invitation

**Context**: Invite User B with specific permissions from the sandbox settings.

In the program settings, go to 'Members' or 'Invites', enter User B's email, select 'Report' and 'Engagement' roles, and send the invite.

> Expected output: Invitation email sent to User B.

### Step 2: Accept Invitation

**Context**: User B joins the program.

User B checks email, clicks the link, and accepts the invitation on HackerOne.

> Expected output: User B added to program members list.

### Step 3: Authenticate and Verify Access

**Context**: Log in and confirm permissions.

User B logs in to HackerOne, navigates to the sandbox, and verifies ability to view and engage with reports.

> Expected output: Reports section accessible; no admin functions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- user-invite
