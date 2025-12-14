---
tags:
  - privilege-escalation
  - access-control
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
created_at: '2025-12-14T17:24:39.063Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:24:39.063Z'
sub_techniques: []
id: b217933f-04a9-4583-8cf2-98e5108bb708
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Achieve-Privilege-Escalation-via-Misconfigured-Access-Controls

## Summary

This procedure leverages a misconfiguration in the Stocky app's permission checks during OAuth to escalate privileges, allowing staff without 'Apps' permission to access and use restricted features as if they had full authorization.

## Description

Following the OAuth bypass, the Stocky app's access controls fail to properly validate user permissions, resulting in privilege escalation. Staff members without the 'Apps' permission can perform actions typically reserved for higher-privilege users, such as managing inventory or generating reports. This stems from inadequate checks in the authentication and authorization layers, enabling unauthorized full access. The issue was fixed promptly, but it highlights the risks of incomplete permission enforcement in OAuth-integrated apps.

## Requirements

1. Successful bypass of OAuth authentication (from prior procedure)
2. Active session in the Shopify dashboard
3. Knowledge of Stocky app features that require 'Apps' permission

## Defense

Defensive measures and detection strategies:

- Conduct regular audits of permission checks in app code, ensuring they occur after authentication
- Use role-based access control (RBAC) with granular enforcement at the API and UI levels
- Log and alert on privilege mismatches, such as low-permission users accessing high-privilege endpoints

## Objectives

1. Escalate from limited staff access to full Stocky app privileges
2. Exploit misconfigured controls to perform restricted actions
3. Assess the scope of unauthorized access possible

## Instructions

### Step 1: Access Restricted Features Post-Bypass

**Context**: With authentication bypassed, test access to features gated by 'Apps' permission.

In the now-loaded Stocky app, navigate to sections like inventory overview or stock adjustments, which should require elevated permissions.

> Expected output: Features load and are interactive without denial messages.

### Step 2: Perform Escalated Actions

**Context**: Execute operations that demonstrate privilege escalation, confirming the misconfiguration.

Attempt actions such as editing stock levels or exporting data. The lack of permission re-checks allows these to succeed.

> Expected output: Actions complete successfully, modifying or retrieving sensitive data.

### Step 3: Validate Escalation Impact

**Context**: Ensure the escalation provides meaningful unauthorized control.

Review performed actions in app logs or UI feedback to confirm they align with full admin capabilities.

> Expected output: Evidence of high-privilege operations executed by a low-privilege account.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[privilege-escalation]]
- [[access-control]]
- [[shopify]]
