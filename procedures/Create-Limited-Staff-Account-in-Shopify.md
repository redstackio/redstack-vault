---
tags:
  - shopify
  - staff-account
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c32357a9-4025-4ac6-b255-8d0b4012112a
created_at: '2025-12-14T17:29:57.128Z'
updated_at: '2025-12-14T17:29:57.128Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-Limited-Staff-Account-in-Shopify

## Summary

This procedure creates a new staff account in Shopify Plus with restricted 'Settings' permissions only, simulating a low-privilege user for testing access controls.

## Description

In the context of Shopify's admin panel, owners can add staff members with granular permissions. This step abuses the ability to create accounts with minimal access to later probe for escalations. The target environment is a Shopify Plus store admin interface. Expected outcome is a functional staff account that can access settings without broader privileges.

## Requirements

1. Valid Shopify Plus owner credentials
2. Access to the admin URL (e.g., https://your-shop.myshopify.com/admin)
3. Email address for the new staff member

## Defense

Defensive measures and detection strategies:

- Enforce principle of least privilege for staff accounts
- Monitor staff account creations via audit logs in Shopify
- Require approval workflows for new staff additions

## Objectives

1. Establish a controlled low-privilege entry point
2. Verify permission boundaries
3. Prepare for escalation testing

## Instructions

### Step 1: Navigate to Staff Management

**Context**: Access the account settings to add a new staff member.

Log in as the store owner and visit the staff creation page.

### Step 2: Configure Permissions

**Context**: Set permissions to 'Settings' only to limit scope.

In the permission selector, uncheck all except 'Settings', then save and send invitation.

> Expected output: Email sent to the provided address with a setup link.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[shopify]]
- [[staff-creation]]
- [[access-control]]
