---
tags:
  - account-setup
  - facebook-linking
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
updated_at: '2025-12-14T17:33:11.990Z'
sub_techniques: []
id: a0c8b128-8c7c-409d-bd3d-496a1c025e23
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Attacker-and-Victim-Accounts-with-Linked-Facebook-Profiles

## Summary

This procedure sets up the foundational environment for a CSRF-based account takeover attack by creating separate Badoo accounts for the attacker and victim, each linked to distinct Facebook profiles, ensuring the attack can simulate real-world linking overrides.

## Description

In the context of exploiting a CSRF vulnerability in Badoo's Facebook photo import feature, this initial setup is crucial. It involves registering accounts on m.badoo.com and associating them with different Facebook profiles via the standard linking mechanism. This allows the attacker to generate tokens tied to their Facebook while the victim has an independent link, highlighting the lack of validation in link modifications. Expected outcomes include verified links that can be hijacked later without re-authentication.

## Requirements

1. Access to two distinct Facebook accounts (attacker's and victim's)
2. Web browser with cookies enabled for session management
3. Email addresses or phone numbers for Badoo registration (can be temporary for testing)
4. No VPN or proxy needed, but use incognito modes to separate sessions

## Defense

Defensive measures and detection strategies:

- Implement account linking verification prompts requiring re-authentication for changes
- Monitor for anomalous link modifications via server-side logging of Facebook token usage
- Educate users on verifying linked accounts regularly and avoiding unsolicited URLs

## Objectives

1. Establish isolated attacker and victim Badoo environments
2. Confirm active Facebook integrations for both accounts
3. Prepare for token generation and hijacking without setup errors

## Instructions

### Step 1: Register Attacker Badoo Account

**Context**: Create the attacker's base account to initiate malicious actions.

Navigate to m.badoo.com, select 'Sign Up', and register using email or phone. Complete profile setup minimally.

### Step 2: Link Attacker's Facebook Profile

**Context**: Associate the attacker's Facebook to enable photo import token generation.

Go to account settings > 'Connect with Facebook'. Authorize the link via Facebook OAuth. Verify by checking profile shows Facebook-linked status.

### Step 3: Register Victim Badoo Account

**Context**: Set up the target's account to simulate a real user.

In a separate browser or incognito window, repeat registration for the victim using different credentials.

### Step 4: Link Victim's Facebook Profile

**Context**: Establish the victim's independent link to be overridden later.

Follow the same linking process, using the victim's Facebook account. Confirm no overlap with attacker's profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-setup]]
- [[facebook-linking]]
