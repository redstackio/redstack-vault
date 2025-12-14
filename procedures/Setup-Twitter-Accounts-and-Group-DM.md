---
id: proc-uuid-001
name: Setup-Twitter-Accounts-and-Group-DM
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:28.841Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - twitter
  - setup
  - dm
commands: []
platforms:
  - Web
tools: []
skill_level: basic
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Setup-Twitter-Accounts-and-Group-DM

## Summary

This procedure establishes the foundational elements for testing IDOR in Twitter group DMs by creating multiple accounts and initiating a shared conversation.

## Description

In the context of exploiting Twitter's DM system, this step involves registering three distinct user accounts and forming a group direct message among them. This setup is crucial to simulate a real-world scenario where a participant leaves a conversation but retains unauthorized access via IDOR. The target environment is Twitter's web platform, requiring only standard account creation capabilities. Expected outcomes include an active group DM ready for further manipulation.

## Requirements

1. Access to email addresses for account verification.
2. Web browser with JavaScript enabled.
3. No special privileges; standard user registration.

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from similar IP addresses.
- Implement CAPTCHA on signup to deter automated setups.

## Objectives

1. Create three functional Twitter accounts.
2. Initiate a group DM to generate a conversation ID.
3. Verify group participation among all accounts.

## Instructions

### Step 1: Create Twitter Accounts

**Context**: Register three separate accounts to act as participants A, B, and C in the group DM.

Navigate to twitter.com and complete the signup process for each account using unique email addresses and usernames.

> Upon verification, log in to each account to confirm access.

### Step 2: Initiate Group DM

**Context**: From account A, create a multi-participant direct message including B and C.

Log in to account A, click the envelope icon for messages, select 'New message', add accounts B and C as participants, and send an initial message to activate the group.

> The group DM URL will contain a conversation ID, visible in the address bar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[setup]]
- [[dm]]
