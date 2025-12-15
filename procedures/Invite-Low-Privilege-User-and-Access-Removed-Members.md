---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - information-disclosure
  - authorization-bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.407Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Invite-Low-Privilege-User-and-Access-Removed-Members

## Summary

This procedure invites a low-privilege user to the Shopify Partner Team and demonstrates unauthorized access to the removed members endpoint, exposing PII of past members.

## Description

Targeting the Shopify Partner Dashboard, this exploits missing permission checks on https://partners.shopify.com/{PartnerTeam_ID}/memberships/removed. As a current member without permissions, the user can view names, removal dates, and emails of ex-staff. Prerequisites: Existing removed member and owner access for invite. Outcome: Confirmation of PII disclosure.

## Requirements

1. Owner credentials to invite low-priv user
2. Valid email for STAFF2
3. Browser access to dashboard

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization on historical data endpoints
- Anonymize or restrict PII in removed members views
- Monitor unauthorized access attempts to /memberships/removed

## Objectives

1. Gain access as low-priv user
2. Retrieve list of removed members
3. Expose personal emails via profile clicks

## Instructions

### Step 1: Invite Low-Privilege User

**Context**: Add STAFF2 without permissions.

As owner, invite STAFF2 to Team_ABC via dashboard, skipping permission assignment.

> Invitation sent; acceptance grants basic membership.

### Step 2: Join Team

**Context**: Log in as low-priv user.

STAFF2 accepts via email or dashboard.

> No permissions assigned, limiting to view-only.

### Step 3: Access Removed Members

**Context**: Navigate to vulnerable endpoint.

As STAFF2, visit https://partners.shopify.com/{PartnerTeam_ID}/memberships/removed.

> Page loads list with names and dates; no auth check.

### Step 4: View Email Details

**Context**: Reveal PII by interacting with list.

Click on removed member (STAFF1) profile.

> Displays personal email from accounts.shopify.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[pii-leak]]
- [[shopify]]
