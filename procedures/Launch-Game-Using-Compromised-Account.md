---
id: proc-002
name: Launch-Game-Using-Compromised-Account
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.413Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - auth-bypass
  - gaming
commands: []
platforms:
  - Gaming
  - Desktop Application
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Launch Game Using Compromised Account

## Summary

This procedure uses the compromised Steam or Epic account to launch a Rockstar game via the Games Launcher, triggering the detection of the linked Social Club account without additional authentication.

## Description

The Rockstar Games Launcher integrates with third-party platforms like Steam and Epic to allow users to launch games tied to their entitlements. By launching a game under the compromised linked account, the Launcher assumes the session is legitimate and prepares for Social Club integration, exploiting the trust in third-party authentication. This step occurs on a desktop environment with the Launcher installed and does not require any custom tools, relying on the application's native behavior.

## Requirements

1. Access to the compromised Steam or Epic account
2. Rockstar Games Launcher installed and updated
3. Ownership of a Social Club-enabled game (e.g., GTA V, RDR2) in the third-party account
4. Standard desktop OS (Windows/macOS) with internet connectivity

## Defense

Defensive measures and detection strategies:

- Implement device binding for account logins to prevent use on unauthorized machines
- Log and alert on game launches from unfamiliar IPs or devices
- Educate users on reviewing linked account activity in the Launcher settings

## Objectives

1. Initiate the game launch to activate Launcher session
2. Trigger linked account detection without credential prompts
3. Position for seamless account switching

## Instructions

### Step 1: Log into Rockstar Games Launcher

**Context**: Use the compromised third-party account to authenticate the Launcher.

Open the Rockstar Games Launcher and select the option to log in via Steam or Epic, entering the compromised credentials.

> The Launcher will authenticate via the third-party OAuth flow.

### Step 2: Select and Launch Game

**Context**: Choose a game that requires Social Club connectivity to force integration.

From the library, select GTA V or RDR2 and click 'Play'.

> The game begins loading, and the Launcher detects the linked Social Club account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[auth-bypass]]
- [[gaming]]
