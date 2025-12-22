---
tags:
  - xss
  - injection
  - group-creation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.549Z'
sub_techniques: []
id: ef5e83be-11bf-4b49-8580-443b8338cea2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Group-Conversation

## Summary

This procedure uses admin access to create a group conversation in Nextcloud Talk with a malicious HTML payload in the name, injecting content that will be rendered unsafely in the desktop client.

## Description

By setting the group name to an HTML payload like an `<img>` tag, an attacker with admin privileges can prepare for XSS. The payload is stored on the server without sanitization and later displayed in client notifications. This targets the web-based Talk interface and assumes server access. Expected outcomes include a group with embedded HTML that invites the victim user.

## Requirements

1. Admin login to Nextcloud web interface
2. Nextcloud Talk app enabled
3. Regular user account for invitation

## Defense

Defensive measures and detection strategies:

- Sanitize all user-input fields, including group names, on the server side
- Implement content security policies (CSP) in Talk rendering
- Log and review group creation events for suspicious payloads

## Objectives

1. Inject HTML payload into group name
2. Invite the target user to the group
3. Prepare for payload delivery via call

## Instructions

### Step 1: Open Nextcloud Talk

**Context**: Access the Talk interface as admin.

Log in to the web interface, click the Talk icon in the top menu.

> Talk dashboard loads, showing conversation options.

### Step 2: Create Group with Malicious Name

**Context**: Initiate a new group and embed the payload in the name field.

Click "New conversation", select group, enter name as `<img src="https://avatars.githubusercontent.com/u/99037623">`, and create.

> Group is created; the name displays with raw HTML in the interface.

### Step 3: Add Regular User

**Context**: Invite the victim to join the malicious group.

In the group settings, search for and add the regular user.

> Invitation sent; user can see the group upon login.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[group-creation]]
