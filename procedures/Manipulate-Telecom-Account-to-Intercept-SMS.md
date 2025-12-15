---
id: proc-att-sms-intercept-16696-2
tags:
  - sms-interception
  - telecom-compromise
type: procedure
tools:
  - '[[tools/ATT-Text-to-Web]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:45.418Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Manipulate-Telecom-Account-to-Intercept-SMS

## Summary

This procedure details compromising a telecom account (e.g., ATT) via email-linked resets to enable SMS interception, allowing attackers to capture 2FA codes sent to the target's phone.

## Description

Attackers use email access to reset the telecom account password, then configure features like 'Text to Web' and call forwarding. This creates an adversary-in-the-middle position for SMS traffic, targeting web portals of telecom providers. The scenario assumes the telecom account is linked to email recovery. Outcomes include real-time visibility of authentication messages, facilitating 2FA bypasses on services like exchanges.

## Requirements

1. Access to the target's email for password reset initiation
2. Knowledge of the telecom provider (e.g., ATT) and its web interface
3. Attacker's web browser for configuring forwarding features

## Defense

Defensive measures and detection strategies:

- Use app-based or hardware 2FA instead of SMS to avoid interception
- Enable telecom account alerts for feature changes like call forwarding
- Regularly review SMS logs and disable unnecessary web viewing services

## Objectives

1. Redirect SMS traffic to attacker-viewable channels
2. Capture authentication codes for linked services
3. Maintain stealth during interception

## Instructions

### Step 1: Reset Telecom Password

**Context**: Leverage email access to regain control of the ATT account.

Use the compromised email to initiate and complete a password reset on the ATT web portal.

> Enter the new password and log in successfully.

### Step 2: Enable SMS Interception Features

**Context**: Configure ATT services to expose SMS content online.

Navigate to account settings and activate 'Text to Web' to view messages on a web page; also enable call forwarding if needed.

> Test by sending a verification SMS to confirm visibility.

### Step 3: Verify Interception

**Context**: Ensure all incoming SMS are capturable for subsequent steps.

Monitor the web interface for real-time SMS arrivals, including test codes.

> Expected output: Clear view of SMS content without alerting the target.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ATT-Text-to-Web]]

## Tags

- [[sms-interception]]
- [[telecom-compromise]]
