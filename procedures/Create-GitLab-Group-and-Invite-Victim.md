---
tags:
  - gitlab
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands//add_contacts]]'
  - '[[commands//remove_contacts]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 53c54a7d-b51f-4e9a-8eb9-d959deddcd00
created_at: '2025-12-11T03:47:49.780Z'
updated_at: '2025-12-11T03:47:49.780Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Create GitLab Group and Invite Victim

## Summary

This procedure sets up a new GitLab group and invites a victim user, establishing the environment for exploiting vulnerabilities in group features.

## Description

Creating a group allows enabling specific features like Customer Relations. Inviting the victim ensures they interact with the vulnerable components. This is a preparatory step for attacks like XSS in GitLab.

## Requirements

1. Authenticated GitLab account with group creation permissions
2. Victim's GitLab username or email
3. Access to GitLab web interface

## Defense

Defensive measures and detection strategies:

- Monitor group creation and invitation logs for suspicious activity
- Restrict group creation to trusted users

## Objectives

1. Establish a controlled group for feature exploitation
2. Involve the victim in the group
3. Prepare for feature-specific attacks

## Instructions

### Step 1: Create New Group

**Context**: Navigate to GitLab and create a new group.

> Create the group via the web interface.

### Step 2: Invite Victim

**Context**: Under 'Invite Members (optional)', add the victim's details and send invitation.

> Ensure the victim accepts the invitation to gain access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #setup
