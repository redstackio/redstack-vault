---
tags:
  - setup
  - shopify-ping
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 91778bdf-2f48-4e48-a674-032a2933cb5e
created_at: '2025-12-14T17:29:57.283Z'
updated_at: '2025-12-14T17:29:57.283Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-High-Priv-Conversation

## Summary

This procedure establishes initial conversation history for a high-privileged user in Shopify Ping with KIT, setting the stage for later exploitation by creating readable content.

## Description

In the attack scenario, the attacker first uses high-privileged credentials to log into Shopify Ping and interact with KIT. This creates conversation data that can be accessed post-exploitation. The target environment is a Shopify store with KITCRM integration. Prerequisites include admin access to create the setup. Expected outcome is verifiable chat history without alerting defenses.

## Requirements

1. High-privileged Shopify user credentials
2. Access to Shopify Ping mobile app or web interface
3. Internet connectivity to kitcrm.com

## Defense

Defensive measures and detection strategies:

- Monitor unusual login patterns from high-priv accounts
- Implement session logging for KIT interactions

## Objectives

1. Create initial KIT conversation for high-priv user
2. Ensure history is established for validation
3. Avoid triggering any alerts during setup

## Instructions

### Step 1: Login and Interact

**Context**: Access Shopify Ping and send sample messages to KIT.

No specific command; use the app interface to log in with high-priv credentials and chat with KIT.

> Expected output: Messages sent and responses received from KIT.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify-ping]]
