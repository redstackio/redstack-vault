---
tags:
  - sso-integration
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: bd383b12-977d-474a-b9df-6ac25ebfc5f1
created_at: '2025-12-11T06:10:40.578Z'
updated_at: '2025-12-11T06:10:40.578Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1550]]'
---
# Integrate SSO and Set Master Password for Takeover

## Summary

This procedure integrates the confirmed email via Shopify SSO, allowing takeover of associated stores by setting a master password.

## Description

Leveraging the verified email, the attacker can link accounts and gain full control, escalating privileges to shop owner level.

## Requirements

1. Verified target email on account
2. Target has existing Shopify stores

## Defense

Defensive measures and detection strategies:

- Require multi-factor for SSO integrations
- Notify users of integration attempts

## Objectives

1. Gain access to target's stores
2. Achieve full privilege escalation

## Instructions

### Step 1: Select Integration Option

**Context**: Initiate SSO linking.

In the profile, select to integrate accounts sharing the same email, follow instructions to set a master password.

> This grants access to all stores under that email.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- sso-integration
- privilege-escalation
