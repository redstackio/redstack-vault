---
tags:
  - account-manipulation
  - backdoor
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:59.130Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 7509f584-7165-4f19-a668-7a59d9db955b
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Modify-POS-User-Email-to-Attacker-Controlled

## Summary

This procedure updates the email address of a POS User in the Stocky app edit form to an attacker-controlled one, facilitating credential takeover.

## Description

On the hidden edit page, alter the email field to attacker@domain.com, optionally keeping the name for legitimacy in password resets. This step in the Shopify Stocky app exploits lack of email validation for POS users. Prerequisites: Loaded edit form. Outcome: Controlled email for backdoor setup.

## Requirements

1. Access to loaded edit form
2. Attacker-owned email address
3. Active admin session

## Defense

Defensive measures and detection strategies:

- Enforce email domain whitelisting for user updates
- Require secondary verification for email changes
- Audit all user attribute modifications

## Objectives

1. Set email to attacker control
2. Maintain user legitimacy
3. Enable post-escalation login

## Instructions

### Step 1: Locate Email Field

**Context**: Identify the modifiable input.

In the form, find the email input field.

> Clear existing value.

### Step 2: Update and Preview

**Context**: Enter new email and check form.

Set to attacker@evil.com and review for errors.

> Expected: No immediate validation blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-manipulation]]
- [[backdoor]]
