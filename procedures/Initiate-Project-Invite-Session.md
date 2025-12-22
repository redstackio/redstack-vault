---
tags:
  - invite-initiation
  - session-persistence
  - mavenlink
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.690Z'
sub_techniques: []
id: 75cd9221-b09e-4f9e-bfe4-54e0d5abc18d
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Initiate-Project-Invite-Session

## Summary

Opens the project invite dialog with an elevated user to create a pending session exploitable after privilege changes.

## Description

User B, with Team Lead access, navigates to the project and activates the invite feature without completing it. This leaves the form open, caching the session state. The vulnerability stems from no re-check on submission. Outcome: Invite console ready for later bypass.

## Requirements

1. User B session with project access and Team Lead role
2. Project created in prior step
3. No submission to keep session active

## Defense

Defensive measures and detection strategies:

- Timeout open sessions or dialogs
- Validate privileges on every action submission
- Monitor for long-open invite sessions

## Objectives

1. Create persistent invite state
2. Position for revocation bypass
3. Simulate interrupted workflow

## Instructions

### Step 1: Access Project as User B

**Context**: Enter the target project with elevated rights.

In Browser Y as User B, go to the projects list, select the created project, and verify Team Lead access.

### Step 2: Open Invite Dialog

**Context**: Initiate without finalizing to exploit persistence.

Click the 'Invite' button or link in the project interface, opening the email input console; do not enter or submit yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[invite-initiation]]
- [[session-persistence]]
- [[mavenlink]]
