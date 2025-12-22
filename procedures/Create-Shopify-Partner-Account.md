---
tags:
  - shopify
  - account-setup
type: procedure
tools:
  - '[[tools/HTTP-Proxy-(e.g.,-Burp-Suite)]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9b437af0-fd74-4810-9fa7-770cd53bcd33
created_at: '2025-12-11T03:47:56.699Z'
updated_at: '2025-12-11T03:47:56.699Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Shopify Partner Account

## Summary

This procedure involves logging into or creating a Shopify Partners account to access the dashboard for email manipulation.

## Description

The attacker needs a Partners account to change emails and exploit the verification process. This step ensures access to the settings page where email changes are initiated.

## Requirements

1. Web browser access
2. Valid credentials or ability to register

## Defense

Defensive measures and detection strategies:

- Monitor for new partner account creations
- Enforce strong authentication

## Objectives

1. Gain access to Partners Dashboard
2. Prepare for email change operations

## Instructions

### Step 1: Login or Register

**Context**: Access or register for a Shopify Partners account.

Navigate to https://partners.shopify.com and login or create a new account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #shopify
- #account-setup
