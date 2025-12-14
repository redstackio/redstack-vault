---
id: proc-uuid-7
tags:
  - master-password
  - takeover
  - sso
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:58.655Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Set-Master-Password-for-Account-Takeover

## Summary

This procedure finalizes the takeover by setting a shared master password for all integrated accounts.

## Description

The SSO feature allows a single password to control multiple stores, enabling full escalation without per-account verification.

## Requirements

1. Initiated SSO integration
2. List of linked accounts visible

## Defense

Defensive measures and detection strategies:

- Mandate unique passwords per account
- 2FA for SSO integrations
- Audit logs for master password sets

## Objectives

1. Create shared credential
2. Gain control over targets

## Instructions

### Step 1: Follow Integration Prompts

**Context**: Complete SSO setup.

Proceed through the integration wizard, selecting accounts to link.

> Prompts for master password creation.

### Step 2: Set and Confirm Password

**Context**: Establish control credential.

Enter a strong master password and confirm it.

> Integration completes; access to target stores granted via login with new password.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[master-password]]
- [[takeover]]
- [[sso]]
- [[shopify]]
