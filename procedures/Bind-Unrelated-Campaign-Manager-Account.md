---
id: proc-linkedin-bind-account-001
tags:
  - authorization-bypass
  - privilege-escalation
  - linkedin
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:12.374Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bind-Unrelated-Campaign-Manager-Account

## Summary

This procedure exploits an authorization vulnerability in LinkedIn Marketing Solutions - Business Manager, allowing an attacker with a legitimate account to bind an unrelated Campaign Manager account to their own Business Manager. This results in unauthorized access to the target's ad campaigns, enabling potential takeover and classified as critical privilege escalation.

## Description

The vulnerability stems from insufficient validation when binding Campaign Manager accounts in the Business Manager interface. An attacker can input any Campaign Manager account ID without ownership verification, granting them control over the associated advertising resources. This was discovered through manual testing of LinkedIn's advertising platform features. The attack requires only standard web access and a valid attacker account, with outcomes including viewing, editing, or hijacking ad campaigns. Prerequisites include identifying the target account ID via public sources or prior reconnaissance.

## Requirements

1. Valid credentials for a LinkedIn Business Manager account
2. Knowledge of the target Campaign Manager account ID (e.g., from URL parameters or public disclosures)
3. Standard web browser access to LinkedIn's marketing platform

## Defense

Defensive measures and detection strategies:

- Implement strict ownership validation during account binding operations
- Monitor for anomalous bindings where the binding account does not match the bound account's owner
- Use rate limiting and logging on account integration endpoints to detect abuse

## Objectives

1. Gain unauthorized access to target Campaign Manager
2. Escalate privileges to manage ad accounts
3. Enable ad account takeover for further exploitation

## Instructions

### Step 1: Access Business Manager Dashboard

**Context**: Log in to initiate the binding process from a controlled account.

Navigate to LinkedIn Marketing Solutions and sign in to your Business Manager account. Ensure you have permissions to manage accounts.

### Step 2: Locate Account Binding Feature

**Context**: Identify the interface for integrating external accounts.

Go to the 'Settings' or 'Accounts' section in Business Manager. Look for options related to 'Campaign Manager' integration or 'Add Account'.

### Step 3: Input Target Account ID

**Context**: Exploit the lack of authorization checks by binding an unrelated account.

Enter the target Campaign Manager account ID in the binding field. Submit the binding request without providing ownership proof.

### Step 4: Verify Access

**Context**: Confirm successful escalation by accessing target resources.

After binding, navigate to the integrated accounts list. Attempt to view or edit campaigns from the target account to validate access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authorization-bypass
- privilege-escalation
- linkedin
- account-takeover
