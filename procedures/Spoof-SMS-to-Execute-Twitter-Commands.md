---
tags:
  - sms-spoofing
  - twitter
  - account-takeover
  - business-logic
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile (SMS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.004]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.154Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: cf16562e-0714-4685-9730-006e8b9092a4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[T1566.004]]'
  - '[[Exploit Public-Facing Application]]'
---
# Spoof-SMS-to-Execute-Twitter-Commands

## Summary

This procedure exploits a flaw in Twitter's SMS command system by spoofing the victim's phone number to send commands to short codes, allowing unauthenticated control over account functions such as tweeting, direct messaging, 2FA removal, and more on any SMS-enabled account.

## Description

The attack targets Twitter's geographical short codes used in regions like the UK, India, and Australia, where longcode networks enable SMS spoofing. By impersonating the target's phone number, attackers can issue commands documented in Twitter's help pages without authentication, as the system lacks proper sender validation and relies on inadequate carrier protections. This enables critical impacts like impersonation of high-profile accounts or mass abuse, affecting millions of users. Prerequisites include access to an SMS spoofing service and knowledge of the target's phone number and Twitter SMS commands.

## Requirements

1. Target's phone number associated with an SMS-enabled Twitter account
2. Access to SMS spoofing capabilities (e.g., online services or APIs that allow sender ID spoofing)
3. Knowledge of Twitter's short codes for the target's region (e.g., UK geographical short codes) and supported SMS commands
4. No direct network access to Twitter; operates via public SMS gateways

## Defense

Defensive measures and detection strategies:

- Enforce mandatory PIN authentication for all SMS commands on Twitter
- Implement sender IP validation or additional factors beyond carrier protections
- Monitor for anomalous SMS command patterns, such as rapid actions from spoofed numbers
- Educate users to disable SMS features or enable app-based 2FA exclusively
- Carrier-level blocks on spoofed SMS to short codes

## Objectives

1. Gain unauthenticated access to perform actions on the target Twitter account
2. Escalate to account takeover by removing 2FA or sending sensitive DMs
3. Enable impersonation or abuse for broader impact

## Instructions

### Step 1: Identify Target and Short Code

**Context**: Determine the target's phone number and the appropriate Twitter short code based on their region and carrier (e.g., UK longcode networks are vulnerable).

Consult Twitter's help pages for supported SMS commands (e.g., 'FOLLOW username' or 'TWEET Hello World'). No command execution here; this is reconnaissance.

### Step 2: Spoof SMS and Send Command

**Context**: Use an SMS spoofing service to send a command impersonating the target's phone number to Twitter's short code, executing the desired action without target interaction.

Select a spoofing service, input the target's phone as sender, Twitter's short code as recipient, and the command (e.g., 'DM @targetuser Secret message').

**Expected Output**: The command processes successfully, resulting in the action on the target account (e.g., a DM sent, verifiable by logging into the account or observing public changes like tweets).

### Step 3: Verify and Escalate

**Context**: Confirm the action succeeded and chain to further commands if needed (e.g., remove 2FA with '2FA OFF').

Monitor the target account via web or app for changes. Repeat spoofing for additional actions like blocking users or deleting tweets.

**Expected Output**: Full control confirmed, such as 2FA disabled or unauthorized tweets posted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[T1566.004]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[sms-spoofing]]
- [[twitter]]
- [[account-takeover]]
- [[business-logic]]
