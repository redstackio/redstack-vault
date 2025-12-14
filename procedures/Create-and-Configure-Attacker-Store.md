---
tags:
  - shopify
  - account-setup
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 85806303-8188-4002-afd7-add929167eeb
created_at: '2025-12-14T17:30:58.596Z'
updated_at: '2025-12-14T17:30:58.596Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-and-Configure-Attacker-Store

## Summary

This procedure involves creating a new development store in the Shopify Partners dashboard and configuring its account settings to prepare for email swapping, targeting legacy non-SSO accounts.

## Description

In the context of exploiting Shopify's email confirmation bypass, the attacker first establishes a controlled environment by creating a development store. This allows navigation to account settings without immediate email verification, setting the stage for request interception. The procedure assumes access to a Shopify Partners account and focuses on legacy systems vulnerable to inadequate validation during email updates.

## Requirements

1. Valid Shopify Partners account with development store creation permissions
2. Browser configured to proxy through Burp Suite for later steps
3. Knowledge of victim's email address (e.g., for testing: say_ch33se+111@wearehackerone.com)

## Defense

Defensive measures and detection strategies:

- Enforce SSO and 2FA on all legacy accounts to prevent merges
- Monitor for unusual development store creations tied to partner accounts
- Implement request signing or CSRF tokens on account settings endpoints

## Objectives

1. Establish a base store for email manipulation
2. Initiate email change to victim's address
3. Prepare for confirmation bypass without alerting victim

## Instructions

### Step 1: Access Partners Dashboard and Create Store

**Context**: Log in to initiate store creation without email verification to maintain control.

No specific command; perform via web interface:

- Navigate to Shopify Partners dashboard.
- Click 'Create a new store' and follow prompts without verifying email.

> This creates a development store accessible immediately.

### Step 2: Navigate to Account Settings

**Context**: Access the admin account page to prepare email change.

No specific command; web navigation:

- Go to `/admin/settings/account/youraccountnumber` in the new store.

> Page loads without email confirmation, allowing direct edits.

### Step 3: Change Email to Victim's

**Context**: Set the email to the target's to trigger the vulnerable flow.

No specific command; form submission:

- In account settings, enter victim's email (e.g., say_ch33se+111@wearehackerone.com) and submit.

> Request is sent but confirmation is bypassed in later steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[shopify]]
- [[account-setup]]
