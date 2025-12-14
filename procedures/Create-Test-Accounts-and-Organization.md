---
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:23.060Z'
sub_techniques: []
id: ca4bcd7b-f2bb-4609-98bc-f7dcb3072b1d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Test-Accounts-and-Organization

## Summary

This procedure sets up victim and attacker accounts and creates an organization to prepare for IDOR exploitation in the API keys management system.

## Description

In a web-based platform, register two accounts to simulate owner-victim and low-privilege attacker roles. Use the victim to create an organization, capturing the ORG-UUID for targeting the vulnerable API endpoints. This establishes the controlled environment needed to demonstrate unauthorized access without affecting production data.

## Requirements

1. Access to email services for registration and invitations
2. Web browser for manual navigation and form submissions
3. Target platform URL (e.g., https://target-platform.com)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation
- Monitor for multiple registrations from similar IPs
- Require CAPTCHA on signup to prevent automated abuse

## Objectives

1. Establish isolated test accounts
2. Create target organization with UUID
3. Ensure victim ownership for key creation

## Instructions

### Step 1: Register Victim Account

**Context**: Create the primary account that will own the organization and API keys.

Navigate to https://target-platform.com/register and submit the form with victim email and credentials.

> Expected: Confirmation email and successful login.

### Step 2: Register Attacker Account

**Context**: Create the secondary account for exploitation with limited permissions.

Repeat registration at https://target-platform.com/register using a different email.

> Expected: Second account active and login successful.

### Step 3: Create Organization

**Context**: Set up the vulnerable entity under victim control.

Log in as victim, go to https://target-platform.com/organization, fill in details, and submit. Copy the ORG-UUID from the URL or response.

> Expected: Dashboard loads with ORG-UUID visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- setup
