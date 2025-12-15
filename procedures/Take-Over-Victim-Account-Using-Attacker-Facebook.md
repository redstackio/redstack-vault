---
tags:
  - account-access
  - facebook-login
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:11.977Z'
sub_techniques: []
id: 782dcd29-efbf-40a0-80aa-b8e4f91a004a
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Take-Over-Victim-Account-Using-Attacker-Facebook

## Summary

This final procedure authenticates into the victim's Badoo account using the attacker's Facebook credentials post-hijack, granting complete unauthorized access to the victim's data and functionality.

## Description

After the link override, the victim's Badoo account is now tied to the attacker's Facebook, allowing login via Facebook OAuth as if it were the owner's. This results in full takeover, including access to personal info, matches, and messages, with impact amplified in a social app like Badoo/Bumble.

## Requirements

1. Hijacked link confirmed from previous step
2. Attacker's Facebook credentials
3. Victim's Badoo login page access

## Defense

Defensive measures and detection strategies:

- Send email/SMS alerts for account link changes
- Require multi-factor for linking modifications
- Monitor login patterns for IP/session mismatches

## Objectives

1. Gain persistent access to victim's account
2. Exfiltrate or manipulate data as needed
3. Demonstrate full impact of the CSRF chain

## Instructions

### Step 1: Log Out of Victim Session

**Context**: Clear any existing auth.

If logged in, log out from the victim's Badoo account.

### Step 2: Initiate Facebook Login

**Context**: Use the hijacked link.

On m.badoo.com login page, select 'Log in with Facebook' and authorize with attacker's credentials.

### Step 3: Access Victim Profile

**Context**: Confirm takeover.

Upon success, the dashboard shows the victim's profile, chats, and settings accessible.

### Step 4: Validate Full Access

**Context**: Test privileges.

Perform actions like viewing private photos or sending messages to verify control.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-access]]
- [[facebook-login]]
