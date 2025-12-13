---
tags:
  - phishing
  - saml
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5015baae-c819-4537-a8dc-0adb799ee14a
created_at: '2025-12-13T09:01:26.488Z'
updated_at: '2025-12-13T09:01:26.488Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Manipulate SAML Email Domain for Phishing

## Summary

This procedure exploits configuration weaknesses by adding extra dots to domains for phishing redirects.

## Description

Manipulating domains like 'hackerone..com' allows registration of similar malicious domains for phishing.

## Requirements

1. Access to SAML config
2. Ability to register similar domains

## Defense

Defensive measures and detection strategies:

- Validate domain inputs strictly
- Use domain whitelisting

## Objectives

1. Redirect to attacker-controlled sites
2. Facilitate phishing attacks
3. Enhance exploit impact

## Instructions

### Step 1: Modify Domain Config

**Context**: Add extra dots in config dialog.

> Input manipulated domain to enable redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[Phishing]]
- [[saml]]
