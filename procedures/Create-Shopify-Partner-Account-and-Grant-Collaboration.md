---
tags:
  - shopify
  - initial-access
  - collaboration
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.559Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 14d3f559-b010-46f1-b27c-810f45776fd9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Shopify-Partner-Account-and-Grant-Collaboration

## Summary

This procedure establishes a Shopify partner account using a business email and secures collaboration access to a target store, setting up the foundation for permission persistence exploitation.

## Description

In the context of Shopify's partner system, this involves registering a new partner account and obtaining store owner approval for collaboration. This grants permissions that are not properly revoked later, enabling unauthorized access. Prerequisites include a valid business email and store owner cooperation (simulated or real for testing). Expected outcome: Full visibility and access to the store via the partner dashboard.

## Requirements

1. Access to a business email address for registration
2. Web browser with JavaScript enabled
3. Target store owner willing to grant collaboration (or test environment)

## Defense

Defensive measures and detection strategies:

- Monitor partner account creations and collaboration requests for anomalies
- Implement email verification on all permission grants and require re-approval on changes

## Objectives

1. Gain initial legitimate access to target store via partner collaboration
2. Establish permission linkage to business email for later manipulation
3. Prepare for email change without permission revocation

## Instructions

### Step 1: Register Partner Account

**Context**: Create and confirm a new Shopify partner account to serve as the entry point.

Navigate to https://partners.shopify.com/signup and enter the business email along with required details. Complete the registration form and submit.

> Upon submission, check the business email for a confirmation link and click it to activate the account.

### Step 2: Request and Obtain Collaboration

**Context**: Link the partner account to the target store through owner-approved access.

Log in to the partner dashboard, go to the "Stores" or "Collaborations" section, search for the target store, and send a collaboration request. Have the store owner approve via their admin panel.

> Once approved, the store appears in your partner dashboard with accessible permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[partner-account]]
- [[collaboration]]
