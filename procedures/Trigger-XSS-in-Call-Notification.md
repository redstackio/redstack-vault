---
tags:
  - xss
  - execution
  - notification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Desktop
  - Windows 10
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.546Z'
sub_techniques: []
id: 4b68fdfd-a5e8-4ef5-b966-ee341e31a461
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Call-Notification

## Summary

This procedure initiates a call in the malicious group conversation to trigger the rendering of the unsanitized group name in the Nextcloud Desktop Client's call notification popup, executing the injected HTML payload.

## Description

Starting a call causes the desktop client to fetch and display the group name as HTML without sanitization, leading to XSS execution in the client's context. This can load external resources or run scripts, enabling phishing or further attacks. The procedure assumes the desktop client is running and the user is in the group. Expected outcomes include visible payload execution, such as an image loading in the popup.

## Requirements

1. Admin access to start the call via web interface
2. Regular user with desktop client open and logged in
3. Membership in the malicious group

## Defense

Defensive measures and detection strategies:

- Sanitize group names in desktop client rendering before HTML parsing
- Implement popup isolation or sandboxing for notifications
- Monitor client for unexpected resource loads from notifications

## Objectives

1. Initiate a call to trigger the notification
2. Observe HTML execution in the desktop popup
3. Validate arbitrary code injection potential

## Instructions

### Step 1: Start Call as Admin

**Context**: Use the web interface to begin a voice or video call in the group.

Log in as admin, open the malicious group in Talk, click the call button (phone or video icon).

> Call starts; notification is pushed to group members.

### Step 2: Observe Execution on Client

**Context**: Monitor the desktop client for the popup and payload execution.

On the regular user's Windows machine, ensure the client is running; the call notification should appear with the group name rendered as HTML.

> The `<img>` tag executes, loading the external image in the popup context.

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
- [[Execution]]
- [[notification]]
