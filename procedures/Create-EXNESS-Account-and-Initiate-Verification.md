---
id: proc-exness-account-create-001
tags:
  - account-creation
  - kyc-initiation
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
updated_at: '2025-12-14T17:25:12.750Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create EXNESS Account and Initiate Verification

## Summary

This procedure registers a new user account on EXNESS's platform and starts the identity verification process, setting the stage for exploiting business logic flaws in KYC by entering arbitrary personal details.

## Description

Account creation uses a valid email and phone for basic verification, then navigates to profile settings to begin KYC. Personal information is entered without document matching, exploiting the lack of upfront validation. This occurs on my.exness.com, with expected approval after document submission in later steps. Target environment: Web browser accessing EXNESS portals.

## Requirements

1. Valid email address and phone number
2. Internet access to my.exness.com
3. Browser configured for proxy if intercepting

## Defense

Defensive measures and detection strategies:

- Rate-limit account creations and verification attempts
- Implement CAPTCHA on registration to deter automation
- Log and monitor rapid successive verifications from same IP

## Objectives

1. Gain initial access to a user account
2. Reach the KYC verification flow
3. Enter unverified personal details

## Instructions

### Step 1: Register Account

**Context**: Create a basic account to access profile features.

No command; use web form:
- Visit https://my.exness.com and select registration.
- Provide email and create password; confirm via email code.

> Account dashboard accessible upon success.

### Step 2: Verify Phone and Start KYC

**Context**: Complete basic auth and initiate verification.

No command; use web interface:
- Enter profile settings at https://my.exness.com/pa/settings/profile.
- Verify phone with SMS code.
- Click verification button to start KYC flow.

> Prompts for personal info and documents appear.

### Step 3: Enter Personal Information

**Context**: Input arbitrary details to mismatch with upcoming documents.

No command; form submission:
- Fill name, DoB, address with test values (e.g., fake name/address).
- Proceed to document upload.

> Flow advances without validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- registration
- verification-start
