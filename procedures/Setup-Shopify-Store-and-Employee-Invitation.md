---
tags:
  - shopify
  - setup
type: procedure
tools:
  - '[[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 807fa8a3-726b-436d-94bf-1d8367f8b0e8
created_at: '2025-12-11T03:47:56.702Z'
updated_at: '2025-12-11T03:47:56.702Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Setup Shopify Store and Employee Invitation

## Summary

This procedure sets up a Shopify store and invites an employee to create a staff account, laying the groundwork for later account conversion exploits.

## Description

In this procedure, an attacker creates a Shopify store and sends an invitation to an employee email address. This establishes a staff account that can be targeted for conversion to a collaborator account via email verification bypass. The invitation acceptance is optional but was tested in the exploit.

## Requirements

1. Access to Shopify platform for store creation
2. Attacker-controlled or test email for store ownership
3. Target employee email address

## Defense

Defensive measures and detection strategies:

- Monitor for unusual store creations and invitations
- Implement rate limiting on invitations

## Objectives

1. Establish a testable staff account
2. Prepare for account takeover
3. Verify invitation process

## Instructions

### Step 1: Create Store and Invite Employee

**Context**: Set up a Shopify store and send an invitation to an employee email address.

Navigate to Shopify dashboard, create a new store, and invite the employee via the staff management section.

### Step 2: Accept Invitation (Optional)

**Context**: Have the employee accept the invitation to become a staff member.

Access the invitation email and follow the link to accept.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #shopify
- #setup
