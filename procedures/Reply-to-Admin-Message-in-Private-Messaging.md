---
tags:
  - private-messaging
  - concrete-cms
  - navigation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: ea2803ac-1749-41b1-85ab-9480420fded9
created_at: '2025-12-14T03:46:38.233Z'
updated_at: '2025-12-14T03:46:38.233Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reply-to-Admin-Message-in-Private-Messaging

## Summary

This procedure navigates to the private messaging section in Concrete CMS and initiates a reply to an administrator's message, setting up for XSS payload injection.

## Description

As part of the stored XSS attack in Concrete CMS 8.5.2, this step involves using the authenticated low-priv session to access conversations. The target is the private messaging component where user input is vulnerable. Prerequisites include a logged-in session and an existing admin message. Expected outcome is the reply form ready for payload entry, exploiting the lack of input validation.

## Requirements

1. Active low-priv user session
2. Existing private message from an administrator
3. Web browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Log and review private message interactions for unusual patterns
- Rate-limit messaging to prevent abuse
- Sanitize all message metadata on storage

## Objectives

1. Locate a target admin conversation
2. Open the reply interface
3. Position for unsafe input submission

## Instructions

### Step 1: Access Private Messages

**Context**: Navigate from the dashboard to messaging.

In the user dashboard, click on the "Messages" or "Private Messages" link in the navigation menu.

> The messaging inbox loads, displaying conversations.

### Step 2: Select and Reply to Admin Message

**Context**: Target a specific conversation for reply.

Find and open the conversation with the administrator, then click the "Reply" button.

> The reply form appears with a message body field (msgBody).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[private-messaging]]
- [[concrete-cms]]
