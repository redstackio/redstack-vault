---
tags:
  - 2fa-setup
  - account-creation
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.378Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 67bc3c5c-8154-4c0e-92a1-b3ce59b42bdf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare Shopify Account for 2FA Interception

## Summary

This procedure sets up an attacker-controlled Shopify account to reach the 2FA activation stage, enabling request interception for subsequent tampering. It establishes the foundation for exploiting the lack of server-side phone number validation.

## Description

In the context of Shopify's web platform, create a new account and navigate to the 2FA settings to prepare for capturing the activation request. This step assumes the attacker has no prior access and uses the platform's self-registration. The outcome is readiness to intercept HTTP traffic, targeting users with SMS-based 2FA. Prerequisites include a proxy tool like Burp Suite configured for the browser.

## Requirements

1. Internet access to shopify.com
2. Burp Suite installed and browser proxied through it
3. No credentials needed initially; free trial account suffices

## Defense

Defensive measures and detection strategies:

- Monitor for unusual account creation patterns from suspicious IPs
- Implement CAPTCHA on registration to deter automated setups
- Log 2FA activation attempts and alert on rapid sequences

## Objectives

1. Gain access to Shopify account management
2. Reach 2FA setup without triggering alerts
3. Position for request interception

## Instructions

### Step 1: Create New Shopify Account

**Context**: Register a disposable account to avoid linking to the attacker's real identity.

No command executed; perform via web UI:

- Navigate to shopify.com and start free trial registration
- Provide fake store name, email, and password

> Expected: Account dashboard loads successfully.

### Step 2: Navigate to 2FA Activation

**Context**: Access the settings to initiate 2FA setup for request capture.

No command; UI navigation:

- Go to Account Settings > Security > Enable Two-Factor Authentication
- Select SMS method and prepare to enter phone number

> Expected: 2FA setup form appears, ready for input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- 2fa-setup
- account-creation
