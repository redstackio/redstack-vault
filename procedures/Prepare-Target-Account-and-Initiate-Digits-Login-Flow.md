---
id: proc-digits-prepare-target-3
tags:
  - phishing
  - login-initiation
  - oauth
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:31:52.804Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Prepare Target Account and Initiate Digits Login Flow

## Summary

This procedure sets up a target account in an OAuth app like Periscope and delivers the malicious Digits URL to the victim to start the authentication process, tricking them into authorizing on the attacker's behalf.

## Description

Using a Periscope account tied to a phone number, the attacker prepares by ensuring the app is authorized via Digits. The malicious URL is then shared with the victim (e.g., via email), initiating the login. This step relies on social engineering and targets web users. Expected outcome: Victim enters the auth flow without suspicion.

## Requirements

1. Access to a Periscope.tv account with phone-linked Digits auth
2. Method to deliver URL (e.g., email, link shortening)
3. Victim interaction (click and authenticate)

## Defense

Defensive measures and detection strategies:

- Educate users on verifying login URLs
- Implement domain pinning in auth flows
- Detect unusual auth initiations from external links

## Objectives

1. Simulate or use real victim account
2. Deliver malicious URL effectively
3. Trigger Digits auth without alerts

## Instructions

### Step 1: Set Up Target Account

**Context**: Ensure the target app is ready for Digits auth.

Log into Periscope.tv and confirm phone number association with Digits.

> If needed, authorize the app via legitimate Digits flow first. Expected output: Account ready for re-auth.

### Step 2: Deliver Malicious URL

**Context**: Send the crafted URL to victim.

Embed in a phishing message: "Login to Periscope via Digits: [malicious URL]"

> Victim clicks and sees legitimate Digits page. Expected output: Auth flow begins, victim prompted for phone/OTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[login-initiation]]
- [[oauth]]
