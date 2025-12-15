---
id: proc-create-accounts-csrf
tags:
  - account-creation
  - setup
  - csrf-prep
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:27:15.336Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-Test-Accounts-for-CSRF

## Summary

This procedure sets up victim and attacker accounts on the target platform (Infogram) to prepare for CSRF exploitation testing, ensuring a controlled environment for demonstrating silent login forgery.

## Description

In a CSRF attack on login forms, the attacker needs both a victim account (to simulate the target's session) and their own account (whose credentials will be forged). Registration is typically open on platforms like Infogram, allowing free account creation via email and basic details. This step confirms account functionality before proceeding to PoC crafting. Expected outcomes include verified logins, setting the stage for session hijacking without authentication prompts.

## Requirements

1. Access to email for verification (if required by platform)
2. Web browser to navigate registration forms
3. No special privileges needed; public registration endpoint

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation to prevent abuse
- Monitor for anomalous registration patterns from single IPs
- Require CAPTCHA on signup to deter automated setups

## Objectives

1. Establish a victim session for CSRF targeting
2. Prepare attacker credentials for PoC injection
3. Validate platform registration flow

## Instructions

### Step 1: Register Victim Account

**Context**: Create a standard user account to represent the target victim, logging in to establish a session.

Navigate to the Infogram registration page and fill in details like email, username, and password. Submit the form and verify via email if prompted.

**Expected Output**: Successful login to victim dashboard.

### Step 2: Register Attacker Account

**Context**: Create the attacker's account whose credentials will be used in the CSRF PoC for silent takeover.

Repeat the registration process with different details. Note the exact username and password for later use in the HTML form.

**Expected Output**: Attacker account active and login confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[setup]]
- [[csrf-prep]]
