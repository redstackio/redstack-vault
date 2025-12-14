---
id: proc-omise-invite-init-001
tags:
  - invitation
  - business-logic
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
updated_at: '2025-12-14T17:24:22.237Z'
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
# Initiate Team Member Invitation

## Summary

This procedure triggers the team invitation form in the Omise dashboard to prepare the POST request for interception and race condition exploitation.

## Description

The Omise dashboard's team feature allows inviting members via a web form that submits to /team/memberships. This step sets up the normal invitation flow, which lacks synchronization for concurrent requests, enabling duplicates. Prerequisites include authenticated access; outcomes position the request for modification.

## Requirements

1. Authenticated session in Omise dashboard
2. Test email address for invitation
3. Permissions to manage team members

## Defense

Defensive measures and detection strategies:

- Add client-side duplicate checks before submission
- Rate limit invitation requests per user/session
- Server-side logging of invitation attempts

## Objectives

1. Populate and submit invitation form
2. Generate interceptable POST request
3. Avoid triggering errors prematurely

## Instructions

### Step 1: Navigate to Team Section

**Context**: Locate the invitation feature.

From dashboard, go to team management.

> Team page loads with invite option.

### Step 2: Fill and Submit Form

**Context**: Enter details to initiate request.

Input test email, select roles (admin/technical), and submit.

> Form submits, request ready for proxy interception.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- invitation
- business-logic
