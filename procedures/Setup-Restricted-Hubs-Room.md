---
id: proc-mozilla-hubs-setup-001
tags:
  - setup
  - mozilla-hubs
  - access-control
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
updated_at: '2025-12-14T17:30:46.951Z'
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
# Setup-Restricted-Hubs-Room

## Summary

This procedure configures a Mozilla Hubs room with administrative restrictions on object creation and movement, creating a controlled environment to test bypass techniques for broken access control vulnerabilities.

## Description

Mozilla Hubs is a social VR platform where rooms can be configured with permissions. This procedure simulates an admin setting up restrictions, which attackers can later bypass. It involves signing into the Hubs instance, creating a room, and disabling object-related features via the UI. The target environment is a web-based Hubs deployment like https://hello.dev.myhubs.net/. Expected outcomes include a room where joined users have no object manipulation capabilities except chat.

## Requirements

1. Access to a Mozilla Hubs admin account
2. Web browser (e.g., Chrome)
3. Room creation permissions on the Hubs instance

## Defense

Defensive measures and detection strategies:

- Enforce server-side permission checks for all room actions
- Monitor for anomalous object spawns in restricted rooms
- Log and alert on chat command usage exceeding normal patterns

## Objectives

1. Establish a baseline restricted room for vulnerability testing
2. Verify UI-based restrictions are applied
3. Prepare for subsequent bypass procedures

## Instructions

### Step 1: Sign In and Create Room

**Context**: Authenticate and initiate room creation to access admin settings.

No command; use browser UI: Navigate to https://hello.dev.myhubs.net/, sign in, click 'Create Room', name it (e.g., 'quikke-test-server'), and join.

> Room loads with default permissions.

### Step 2: Apply Restrictions

**Context**: Disable object creation and pinning to restrict non-admin users.

No command; UI steps: Click the three dots menu, select 'Edit Room Settings', uncheck 'Create and move objects' and 'Pin objects', then 'Apply Changes'.

> Settings update; rejoin to confirm restrictions (only chat available).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[mozilla-hubs]]
- [[access-control]]
