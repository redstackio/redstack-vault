---
id: uuid-invite-user-1
tags:
  - hackerone
  - sandbox
  - business-logic
  - invitation
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Create Account]]'
updated_at: '2025-12-14T17:30:07.396Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Create Account]]'
---
# Invite-User-to-Sandbox-Program

## Summary

This procedure exploits the lack of backend enforcement to successfully invite a new user as a team member to a HackerOne sandbox program, violating platform policy.

## Description

Despite documentation restricting invitations in sandbox programs, the feature functions due to a business logic error. This allows attackers to grant unauthorized access to testing features. The attack scenario involves a standard user submitting an invite via the web UI, with outcomes including expanded program access for the invitee.

## Requirements

1. Access to the team members page in a sandbox program
2. Target user's HackerOne handle or email
3. Active session

## Defense

Defensive measures and detection strategies:

- Enforce program type checks on invitation endpoints
- Log and alert on successful invitations to sandbox programs
- Review invited users periodically

## Objectives

1. Bypass invitation restrictions in sandbox mode
2. Grant unauthorized team access
3. Demonstrate potential for feature misuse

## Instructions

### Step 1: Enter User Details

**Context**: Locate and fill the invitation form on the team members page.

Click the invite button, input the new security member's HackerOne username or email, and select the role (e.g., security member).

> The form accepts input without validation errors.

### Step 2: Submit and Confirm Invitation

**Context**: Complete the process to send the invite.

Submit the form and monitor for confirmation.

> A success message appears, and the invite is dispatched; the user can accept to join the program.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Create Account]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[hackerone]]
- [[sandbox]]
- [[business-logic]]
- [[invitation]]
