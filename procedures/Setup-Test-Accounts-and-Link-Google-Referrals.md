---
id: proc-setup-insightly-accounts
tags:
  - account-setup
  - google-link
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
updated_at: '2025-12-14T17:27:57.470Z'
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
# Setup Test Accounts and Link Google Referrals

## Summary

This procedure involves creating two test accounts on the Insightly platform and linking unique Google referral accounts to each, allowing the identification of distinct linked account IDs necessary for subsequent CSRF exploitation.

## Description

In the context of testing the CSRF vulnerability in Insightly's user settings, this step establishes the environment by simulating attacker and victim accounts. Each account is linked to a Google account via the referrals feature, resulting in unique IDs that can be targeted. This setup confirms the vulnerability's prerequisites and provides the necessary identifiers for crafting the exploit. The process requires access to the Insightly web interface and valid Google credentials for linking.

## Requirements

1. Access to the Insightly registration page (https://crm.na1.insightly.com)
2. Valid email addresses for account creation
3. Google accounts for linking referrals
4. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement account creation rate limiting to prevent bulk testing
- Monitor for unusual referral linking patterns from new accounts
- Require email verification before linking external services

## Objectives

1. Establish authenticated accounts for testing
2. Link Google referrals to obtain unique IDs
3. Prepare environment for vulnerability exploitation

## Instructions

### Step 1: Create Test Accounts

**Context**: Register two separate accounts on Insightly to simulate attacker (Account A) and victim (Account B) scenarios.

Navigate to https://crm.na1.insightly.com and complete the registration process for both accounts using different email addresses.

### Step 2: Link Google Referrals

**Context**: Access the referrals settings and link a Google account to each test account, noting the assigned IDs.

Log in to each account, navigate to https://crm.na1.insightly.com/users/referrals, and follow the prompts to link a Google account. Observe and record the unique linked account ID for each (e.g., via browser developer tools or page source).

**Expected Output**: Successful linking confirmation with visible unique IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-setup]]
- [[google-link]]
