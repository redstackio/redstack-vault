---
tags:
  - shopify
  - account-manipulation
  - email-change
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:28:58.554Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c5ed6b5a-6dda-4268-80b2-a9a2eb7a05e2
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Partner-Business-Email

## Summary

This procedure updates the business email associated with a Shopify partner account, exploiting the system's failure to revoke linked permissions, which enables subsequent unauthorized access.

## Description

Shopify's partner account management allows email changes without updating or revoking collaboration permissions tied to the old email. This is performed in the account settings and confirmed via the new email. The target environment is the Shopify Partners dashboard. Expected outcome: Email changed, but old email retains permission artifacts.

## Requirements

1. Active Shopify partner account with collaboration access
2. New controlled email address for update
3. Logged-in session to partner dashboard

## Defense

Defensive measures and detection strategies:

- Automatically revoke all permissions on email changes and require re-verification
- Log and alert on account email modifications with permission audits

## Objectives

1. Simulate email deletion or change to test permission persistence
2. Maintain original permissions for exploitation
3. Enable access via old email post-change

## Instructions

### Step 1: Access Account Settings

**Context**: Locate and prepare to modify the business email in the partner profile.

Log in to https://partners.shopify.com, click on your profile icon, and select "Account settings" or "Business information".

> The business email field should be visible and editable.

### Step 2: Update and Confirm Email

**Context**: Change the email and complete verification to apply the update.

Enter the new business email address, save the changes, and check the new email for a confirmation link. Click to verify.

> Success is indicated by the profile reflecting the new email as primary.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[email-change]]
- [[permission-persistence]]
