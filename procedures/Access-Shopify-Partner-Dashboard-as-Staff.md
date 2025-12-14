---
id: proc-access-staff-dashboard
tags:
  - login
  - dashboard-access
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
updated_at: '2025-12-14T17:29:20.458Z'
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
# Access-Shopify-Partner-Dashboard-as-Staff

## Summary

This procedure allows a low-privilege team member to accept an invitation and log into the Shopify Partners dashboard, gaining a session for further exploitation without UI-visible financial data.

## Description

Following the invite, the staff member uses the invitation link to authenticate. This establishes a valid but permissionless session on https://partners.shopify.com/, setting the stage for intercepting requests to bypass authorization checks on the GraphQL API.

## Requirements

1. Invitation email from previous setup
2. Valid email account for the staff member
3. Web browser for authentication

## Defense

Defensive measures and detection strategies:

- Log all staff logins and correlate with permission levels
- Enable multi-factor authentication (MFA) for partner accounts
- Alert on logins from unusual IP locations

## Objectives

1. Achieve authenticated session as low-priv user
2. Confirm restricted UI access
3. Prepare for request interception

## Instructions

### Step 1: Accept Invitation

**Context**: Use the email link to initiate staff account creation.

Click the invitation link in the received email.

> This redirects to the authentication flow.

### Step 2: Authenticate

**Context**: Complete login to access the dashboard.

Provide credentials or complete signup, then log in to https://partners.shopify.com/.

> Dashboard loads with limited views due to no permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login]]
- [[shopify]]
- [[staff-access]]
