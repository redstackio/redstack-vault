---
tags:
  - csrf
  - oauth
  - pinterest
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.682Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bbb2df21-64ed-47e6-ab2d-a81ab53c00f7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Authorize Attacker OAuth Flow

## Summary

Completes the authorization on the attacker's Pinterest account to generate an authorization code for later CSRF exploitation.

## Description

After initiation, the attacker authorizes the app on Pinterest, leading to a callback with a code. The missing state allows this code to be reused maliciously. Environment: Web-based OAuth between Shopify and Pinterest.

## Requirements

1. Pinterest login credentials for attacker
2. Proxy setup for next step (e.g., Burp)
3. Active OAuth session

## Defense

Defensive measures and detection strategies:

- Require state parameter validation in OAuth callbacks
- Rate-limit OAuth attempts per user

## Objectives

1. Grant Shopify permissions to attacker's Pinterest
2. Trigger code generation
3. Enable callback interception

## Instructions

### Step 1: Log In to Pinterest

**Context**: Authorize the app.

Enter attacker's Pinterest credentials on the auth page.

> Expected: Prompt for permissions.

### Step 2: Grant Permissions

**Context**: Approve access.

Click 'Authorize' for Shopify app scopes (e.g., boards, pins).

> Expected: Redirect to callback URL with code query param.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[oauth]]
- [[pinterest]]
