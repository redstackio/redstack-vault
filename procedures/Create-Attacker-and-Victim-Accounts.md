---
id: proc-uuid-1
tags:
  - account-creation
  - setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.200Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Attacker-and-Victim-Accounts

## Summary

This procedure sets up two TaxJar accounts to simulate an attacker-victim scenario for testing CSRF in the CSV import feature.

## Description

In the context of exploiting CSRF on app.taxjar.com, creating separate accounts allows isolation of the attack: the attacker uploads a malicious CSV, while the victim is tricked into importing it. This requires no special privileges, just standard registration. Expected outcome is two functional accounts for the full attack chain.

## Requirements

1. Internet access to app.taxjar.com
2. Valid email addresses for registration
3. No prior TaxJar access needed

## Defense

Defensive measures and detection strategies:

- Monitor for unusual account creations from the same IP
- Implement CAPTCHA on registration to deter bulk setups

## Objectives

1. Establish isolated attacker environment
2. Prepare victim profile for testing
3. Ensure accounts are authenticated independently

## Instructions

### Step 1: Register Attacker Account

**Context**: Create the primary account for uploading the malicious CSV.

Navigate to https://app.taxjar.com/signup and complete registration with an email and password. Verify email if required and log in.

### Step 2: Register Victim Account

**Context**: Set up a separate account to receive the unauthorized import.

Repeat the registration process with a different email (e.g., for user Alex). Log in to confirm access to the dashboard and CSV import feature.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-setup]]
- [[taxjar]]
