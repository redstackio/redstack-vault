---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - pii-propagation
  - data-leak
  - shopify
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:24:56.405Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Verify-PII-Propagation-After-Update

## Summary

This procedure tests the propagation of updated personal information from a removed Shopify team member's account to the unauthorized viewer, highlighting ongoing PII exposure.

## Description

In Shopify's ecosystem, changes to a removed user's profile at https://accounts.shopify.com/account sync to the Partner Dashboard's removed members view without isolation. Prerequisites: Removed member (STAFF1) and low-priv viewer (STAFF2). Outcome: Updated PII visible, enabling persistent privacy violations.

## Requirements

1. Access to removed user's Shopify account
2. Low-priv user session active
3. Browser for navigation and refresh

## Defense

Defensive measures and detection strategies:

- Decouple removed user data from live views post-removal
- Implement data caching with expiration for historical records
- Alert on PII updates viewed by unauthorized roles

## Objectives

1. Update removed user's PII
2. Observe real-time propagation
3. Confirm lack of access controls on updates

## Instructions

### Step 1: Update Personal Information

**Context**: Modify name and email as removed user.

Log into https://accounts.shopify.com/account as STAFF1 and save changes to name/email.

> Updates stored in Shopify's central account system.

### Step 2: Refresh Removed Members Page

**Context**: Check for propagated changes as low-priv user.

As STAFF2, refresh https://partners.shopify.com/{PartnerTeam_ID}/memberships/removed.

> New details appear without delay.

### Step 3: Validate Exposure

**Context**: Document the leaked updated PII.

Click profile to confirm email change visibility.

> Demonstrates ongoing unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Cloud Storage]] Data from Cloud Storage

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[data-propagation]]
- [[pii-leak]]
- [[shopify]]
