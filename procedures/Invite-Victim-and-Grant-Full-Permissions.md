---
id: 333e4567-e89b-12d3-a456-426614174003
name: Invite-Victim-and-Grant-Full-Permissions
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.894Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - invitation
  - permissions
  - lateral-movement
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---

# Invite-Victim-and-Grant-Full-Permissions

## Summary

This procedure invites a victim to the attacker's site on IntenseDebate and grants full permissions to enable access to the vulnerable reinstall functionality.

## Description

By inviting the victim and escalating their permissions, the attacker ensures the victim can interact with the Tumblr2 update endpoint. This step relies on the platform's collaboration features and requires the victim to accept the invitation. It facilitates the social engineering aspect of delivering the XSS payload.

## Requirements

1. Created site with ID
2. Victim's email or username
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Require approval for permission grants
- Alert users on invitation acceptance and permission changes

## Objectives

1. Add victim as collaborator
2. Enable full access to site features
3. Expose vulnerable endpoint to victim

## Instructions

### Step 1: Send Invitation

**Context**: Use site settings to invite the victim.

In the site dashboard, locate the invitation or collaborators section and enter the victim's details.

> Submit the invitation; victim receives an email or notification.

### Step 2: Grant Permissions

**Context**: Escalate access once accepted.

After victim accepts, edit their role to grant full permissions, including reinstall access.

> Verify permissions in the user list.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[invitation]]
- [[permissions]]
- [[lateral-movement]]
