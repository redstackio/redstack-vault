---
id: proc-openmage-account-setup-001
tags:
  - account-creation
  - setup
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:25:33.616Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-User-Accounts-and-Addresses-in-OpenMage

## Summary

This procedure sets up two user accounts and adds addresses to them in the OpenMage application, providing the necessary prerequisites for testing IDOR vulnerabilities in the address editing feature.

## Description

In the context of exploiting IDOR in OpenMage, this initial setup involves registering two distinct user accounts on the demo site (demo.openmage.org) to simulate an attacker and a victim. Each account is then used to create sample addresses, generating unique address IDs that will be targeted in subsequent exploitation steps. This establishes the baseline for demonstrating unauthorized access and resource manipulation. The target environment is a web-based PHP e-commerce platform accessible via standard HTTP.

## Requirements

1. Access to the OpenMage demo site (demo.openmage.org)
2. Valid email addresses for registration (e.g., temporary emails if needed)
3. Web browser for manual registration and address addition
4. No special credentials required beyond public registration

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification on registration to prevent bulk account creation
- Monitor for unusual registration patterns from the same IP
- Rate limit address creation per user session

## Objectives

1. Establish attacker and victim accounts for IDOR simulation
2. Generate valid address IDs for cross-account manipulation
3. Prepare session cookies for authenticated requests

## Instructions

### Step 1: Register User Accounts

**Context**: Create two separate accounts to obtain distinct sessions and address spaces.

No specific command; use the web interface:

Navigate to the registration page and fill in details for account 1 (attacker@example.com) and account 2 (victim@example.com).

> Expected output: Success message and login redirect.

### Step 2: Add Addresses to Each Account

**Context**: Create at least one address per account to acquire targetable IDs.

No specific command; use the address management UI:

Log in to each account, go to 'My Account > Address Book > Add New Address', enter sample data (e.g., 123 Main St, Anytown, 12345), and save.

> Expected output: Address listed with an auto-generated ID (visible in edit URL or via inspection).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-creation
- setup
- web
