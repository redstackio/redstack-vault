---
tags:
  - 2fa-setup
  - coinbase
  - authentication
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.883Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: f085855c-14ff-4892-9b81-80b2465db18a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-2FA-for-BTC-Withdrawals-in-Coinbase

## Summary

This procedure sets up two-factor authentication (2FA) specifically for Bitcoin (BTC) withdrawals in a Coinbase account, establishing a security baseline that can be tested for bypass vulnerabilities.

## Description

In the context of testing Coinbase's security features, this step involves navigating the web-based account settings to enable 2FA requirements for any BTC send or withdrawal actions. This simulates a secure user configuration, ensuring that standard withdrawals would prompt for 2FA verification via an authenticator app or SMS. The procedure is essential for demonstrating flaws where certain features, like paper wallet exports, fail to enforce these checks, potentially allowing unauthorized fund movements.

## Requirements

1. Active Coinbase account with login credentials
2. Access to 2FA setup method (e.g., Google Authenticator app or phone for SMS)
3. BTC balance in the account (optional for setup, required for testing)

## Defense

Defensive measures and detection strategies:

- Regularly audit 2FA settings in account dashboards to ensure they are enabled
- Monitor login and withdrawal logs for unusual activity patterns
- Implement additional layers like withdrawal limits or email confirmations

## Objectives

1. Activate 2FA to require verification for BTC withdrawals
2. Confirm setup by attempting a standard withdrawal that prompts for 2FA
3. Prepare account for vulnerability testing

## Instructions

### Step 1: Access Account Settings

**Context**: Log in to Coinbase and reach the security configuration area to modify authentication rules.

Navigate to the Coinbase dashboard, click on your profile icon, and select "Settings" > "Security". Locate the 2FA section and enable it if not already active.

### Step 2: Configure 2FA for BTC Withdrawals

**Context**: Specify that 2FA is required for cryptocurrency sends, focusing on BTC.

In the security settings, find the option for "Require 2FA for withdrawals" or similar, and toggle it on for BTC specifically. Scan the QR code with your authenticator app to link it, or enter your phone number for SMS verification. Save changes and verify by attempting a small test withdrawal, which should now prompt for the 2FA code.

> Upon success, a confirmation banner appears, and future standard BTC sends require the code.

### Step 3: Validate Configuration

**Context**: Ensure the settings are applied correctly before proceeding to bypass tests.

Attempt a regular BTC transfer to an external address (e.g., another wallet). The system should interrupt with a 2FA prompt. If it does, the setup is confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- 2fa-setup
- coinbase
- authentication
