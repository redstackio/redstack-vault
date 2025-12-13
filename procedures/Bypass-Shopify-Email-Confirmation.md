---
tags:
  - email-bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4e18809d-32c9-4755-a79f-0d5e02523c4f
created_at: '2025-12-13T09:01:26.823Z'
updated_at: '2025-12-13T09:01:26.823Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass Shopify Email Confirmation

## Summary

This procedure bypasses the email confirmation step during Shopify store signup, allowing an attacker to associate a new store with a victim's email address without verification, setting the stage for further exploits like account merging.

## Description

The attack targets the store signup and email confirmation process in Shopify. By using a similar email and exploiting a known bypass (from report #791775), the attacker creates a store linked to the victim's email. This is effective against accounts with SSO enabled but no 2FA. Expected outcome is unauthorized association of the email without confirmation.

## Requirements

1. Victim's email address
2. Access to Shopify signup page
3. Knowledge of bypass method from report #791775

## Defense

Defensive measures and detection strategies:

- Implement stricter email validation and confirmation tokens
- Monitor for unusual store creations with similar emails

## Objectives

1. Create new store without email confirmation
2. Associate victim's email with attacker-controlled store
3. Prepare for account merging

## Instructions

### Step 1: Sign Up for New Store

**Context**: Initiate signup with modified victim email.

Navigate to Shopify signup and create a new store (e.g., h48ngalog.myshopify.com) using a similar email (e.g., ngalog+1@wearehackeorne.com).

> This sets up the store without immediate confirmation.

### Step 2: Apply Bypass Method

**Context**: Bypass the confirmation as per known vulnerability.

Follow the method from report #791775 to skip email verification.

> Ensures access to the store dashboard without verifying the email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[email-bypass]]
- [[shopify]]
