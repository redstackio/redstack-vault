---
id: proc-setup-fabric-org
tags:
  - setup
  - test-environment
  - fabric-io
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.777Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Test-Organization-and-Accounts

## Summary

This procedure establishes a controlled test environment in Fabric.io by creating an organization and adding admin and member accounts, preparing for vulnerability testing.

## Description

In the context of testing broken access control in Fabric.io, set up a victim organization (VictimOrg) with a primary admin (Victimadmin) and a team member (Victimmember). This simulates a real organization structure. Use the Fabric.io web interface to register accounts and create the org. Expected outcome: A functional organization with identifiable IDs for exploitation steps. Prerequisites include valid email addresses for account creation.

## Requirements

1. Access to email for account verification
2. Browser with JavaScript enabled
3. Internet connection to fabric.io

## Defense

Defensive measures and detection strategies:

- Monitor new organization creations via audit logs
- Enforce CAPTCHA on registrations to prevent abuse

## Objectives

1. Create isolated test org for safe experimentation
2. Obtain account and org IDs for request crafting
3. Ensure member addition succeeds without errors

## Instructions

### Step 1: Register Test Accounts

**Context**: Create credentials for Victimadmin and Victimmember to represent target roles.

Go to fabric.io signup page and register two accounts using distinct emails.

**Expected Output**: Confirmation emails sent; accounts activated.

### Step 2: Create Organization and Add Member

**Context**: Use Victimadmin to build VictimOrg and invite Victimmember.

Log in as Victimadmin, create new organization named VictimOrg, then invite Victimmember via email and accept the invite.

**Expected Output**: VictimOrg dashboard shows Victimmember in team list; note org_id (e.g., 54af7e07b8568e8c6a0001e) and account_id (e.g., 552787195127ae16b8000987) from browser dev tools or network tab.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[test-environment]]
