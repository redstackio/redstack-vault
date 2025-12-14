---
id: 123e4567-e89b-12d3-a456-426614174002
name: Create-Attacker-Account-and-Inject-XSS
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.428Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - injection
  - validation-bypass
platforms:
  - Web
commands:
  - '[[commands/meteor-call-create-channel-xss]]'
tools:
  - '[[tools/Browser-Developer-Tools]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Create-Attacker-Account-and-Inject-XSS

## Summary

This procedure creates a non-admin attacker account in Rocket.Chat, logs in, and exploits a validation bypass in the createRoom function to inject a stored XSS payload into a channel's name via the extraData parameter.

## Description

Using the Rocket.Chat web interface or API, register a user with username 'attacker' and password 'attacker'. Authenticate and open browser developer tools to execute a Meteor.call that creates a channel with a valid name but overrides the name in extraData with a malicious payload like '<img src onerror=alert(origin)>'. This bypasses client-side validation, stores the payload in the database, and sets up for admin invitation and triggering.

## Requirements

1. Access to the running Rocket.Chat instance
2. Browser with developer tools (e.g., Chrome DevTools)
3. Non-admin permissions for channel creation

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all extraData parameters in createRoom
- Implement server-side name validation before database storage
- Monitor for unusual Meteor.call patterns in logs

## Objectives

1. Establish attacker presence in the instance
2. Store XSS payload persistently
3. Prepare for admin interaction

## Instructions

### Step 1: Create User Account

**Context**: Register a non-admin user for exploitation.

**Command** (No CLI; use UI):
Via the Rocket.Chat registration page, create user 'attacker' with password 'attacker'.

> Expected output: Account created and login prompt appears.

### Step 2: Log In as Attacker

**Context**: Authenticate to gain session for channel creation.

**Command** (No CLI; use UI):
Enter credentials on the login page.

> Expected output: Dashboard loads with attacker session.

### Step 3: Inject XSS Payload

**Context**: Use dev tools to bypass validation and store payload.

**Command** ([[commands/meteor-call-create-channel-xss]]):
```javascript
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

> Executes in browser console. Expected output: Channel created successfully, payload stored in DB via extraData merge.

### Step 4: Invite Admin

**Context**: Add admin to channel for targeting.

**Command** (No CLI; use UI):
In the channel, use the invite member feature to add the admin user.

> Expected output: Admin joins the channel.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/meteor-call-create-channel-xss]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[xss]]
- [[injection]]
- [[validation-bypass]]
