---
tags:
  - shopify
  - initial-access
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
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 605f3116-1e97-425f-8952-d48bd7f04864
created_at: '2025-12-11T06:10:22.800Z'
updated_at: '2025-12-11T06:10:22.800Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Create New Shopify Store and Set Victim Email

## Summary

This procedure involves creating a new Shopify store via the partners dashboard and changing the account email to the victim's address without initial verification, setting the stage for further exploitation.

## Description

In this procedure, attackers access the Shopify partners dashboard to create a new store and navigate to the account settings to update the email field. This exploits the lack of verification in legacy account flows, allowing arbitrary email changes that can be manipulated later. The target environment is Shopify's web admin interface, and the expected outcome is a store account primed for email bypass.

## Requirements

1. Access to Shopify partners dashboard
2. Knowledge of victim's email address
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement strict email verification for all changes
- Monitor for unusual account creation and email update patterns

## Objectives

1. Establish a new store account
2. Set victim's email in account settings
3. Prepare for request manipulation

## Instructions

### Step 1: Create New Store

**Context**: Access the partners dashboard and initiate store creation.

Navigate to the partners account and create a new store without specifying endpoints or payloads.

### Step 2: Navigate to Account Settings

**Context**: Go to the new store's admin settings without verifying email.

Navigate to admin/settings/account/youraccountnumber.

### Step 3: Change Email to Victim's

**Context**: Update the email field.

Change the email to the victim's email (e.g., say_ch33se+111@wearehackerone.com).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- initial-access
