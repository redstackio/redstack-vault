---
tags:
  - account-takeover
  - shopify
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
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9b1b5ebb-aa96-4694-a5af-431b562510fa
created_at: '2025-12-11T03:47:56.672Z'
updated_at: '2025-12-11T03:47:56.672Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Confirm Arbitrary Email and Add Managed Store

## Summary

This procedure adds the target store as a managed store after successful email confirmation, granting unauthorized collaborator access.

## Description

Once the arbitrary email is confirmed, the attacker can add the store associated with that email, automatically converting the staff account to a collaborator and providing access.

## Requirements

1. Confirmed arbitrary email
2. Target store details

## Defense

Defensive measures and detection strategies:

- Require additional verification for managed store additions
- Monitor for unauthorized collaborator conversions

## Objectives

1. Gain store access
2. Achieve account takeover

## Instructions

### Step 1: Add Managed Store

**Context**: Navigate to managed stores and add the target.

Go to https://partners.shopify.com/[ID]/managed_stores and add the store, which converts the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #account-takeover
- #shopify
