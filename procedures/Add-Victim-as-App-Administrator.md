---
tags:
  - social-engineering
  - admin-assignment
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:14.145Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c64ba7f8-3dc3-42af-af62-5ee7e0546cad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Add-Victim-as-App-Administrator

## Summary

This procedure invites or assigns a target victim as an administrator of the malicious VK.com application, granting them access to the developer page where the stored XSS payload will execute upon viewing.

## Description

VK.com's app management allows owners to add users as admins via invitations or direct assignment. This step requires social engineering to convince the victim to accept, setting the stage for XSS trigger when they access https://vk.com/dev/Login. The procedure targets the app settings interface post-creation.

## Requirements

1. Malicious app already created with XSS payload
2. Victim's VK username or ID
3. Attacker's control over app ownership

## Defense

Defensive measures and detection strategies:

- Require approval workflows for admin additions in developer apps
- Educate users on risks of accepting app admin roles from unknown sources
- Log and alert on unusual admin invitations

## Objectives

1. Grant victim admin access to the app
2. Position victim to encounter the stored payload
3. Enable targeted XSS delivery

## Instructions

### Step 1: Navigate to App Management

**Context**: Access the settings for the created app.

Go to the app dashboard and select admin management.

### Step 2: Invite Victim

**Context**: Search for and add the victim as admin.

Enter the victim's VK ID or username, send invitation, or assign directly if possible.

### Step 3: Confirm Addition

**Context**: Verify the victim is listed as admin.

Check the admin list; wait for acceptance if invitation-based.

**Expected Output**: Victim appears in admin roster.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[admin-assignment]]
