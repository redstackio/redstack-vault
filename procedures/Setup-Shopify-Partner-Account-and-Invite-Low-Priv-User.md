---
id: proc-setup-shopify-invite
tags:
  - setup
  - account-creation
  - shopify
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
updated_at: '2025-12-14T17:29:20.459Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Shopify-Partner-Account-and-Invite-Low-Priv-User

## Summary

This procedure sets up a Shopify Partner organization and invites a team member with no permissions, establishing a low-privilege account for subsequent exploitation of authorization bypasses.

## Description

In the context of testing improper authorization in Shopify's partner dashboard, this step creates the necessary accounts. The owner logs into https://partners.shopify.com/, navigates to Teams, and invites a staff member without selecting any permissions, including 'View financials'. This simulates an unauthorized internal user who can later exploit the GraphQL endpoint.

## Requirements

1. Valid Shopify Partner credentials for the organization owner
2. Access to email for sending and receiving invitations
3. Web browser for dashboard interaction

## Defense

Defensive measures and detection strategies:

- Implement strict permission auditing during team invites
- Monitor for unusual account creation patterns in partner organizations
- Use role-based access control (RBAC) to enforce least privilege

## Objectives

1. Establish a controlled low-privilege account
2. Verify no permissions are granted
3. Prepare for dashboard access testing

## Instructions

### Step 1: Log In as Owner

**Context**: Access the Shopify Partners dashboard to manage teams.

Navigate to https://partners.shopify.com/ and authenticate as the organization owner.

> Successful login grants access to the dashboard interface.

### Step 2: Invite Team Member

**Context**: Create a staff invite without permissions to simulate unauthorized access.

Go to Teams > Invite staff member, select no permissions (ensure 'View financials' is unchecked), enter email, and complete the invite.

> Invitation email is sent; no technical commands executed, but UI interaction confirms zero permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify]]
- [[account-invite]]
