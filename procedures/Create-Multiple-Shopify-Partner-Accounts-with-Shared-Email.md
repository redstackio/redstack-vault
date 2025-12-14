---
tags:
  - shopify
  - account-creation
  - web
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
updated_at: '2025-12-14T17:32:01.291Z'
sub_techniques: []
id: 77840997-cf92-4b93-9869-2077992f7646
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Create Multiple Shopify Partner Accounts with Shared Email

## Summary

This procedure creates two Shopify partner accounts using the same business email address, setting up the conditions for exploiting the account conversion logic in the authorization system.

## Description

In the Shopify Partners platform, the system allows multiple registrations with the same email if not fully verified, enabling shared email linkage. This is a prerequisite for bypassing collaborator approval by tricking the system into treating one account as an 'existing' conversion candidate. The attack targets partners.shopify.com and requires no special privileges.

## Requirements

1. Access to a business email address (e.g., Gmail or custom domain)
2. Web browser with JavaScript enabled
3. Internet connection to partners.shopify.com

## Defense

Defensive measures and detection strategies:

- Implement email uniqueness checks during partner registration
- Require full verification before allowing multiple accounts per email
- Monitor for rapid successive registrations from the same IP/email

## Objectives

1. Establish linked accounts for conversion exploitation
2. Avoid triggering email verification locks
3. Prepare for collaborator request submission

## Instructions

### Step 1: Register First Partner Account

**Context**: Initiate the first account to establish the email baseline.

Navigate to https://partners.shopify.com/signup and fill in details using the shared business email (e.g., attacker@business.com), name, and password. Submit without completing any email verification if possible.

> Expected output: Account created with dashboard access; email may show pending verification.

### Step 2: Register Second Partner Account

**Context**: Create the second account immediately to link via the shared email.

Repeat the registration process using the exact same business email, but vary other details like name slightly. The system should allow it due to incomplete verification on the first.

> Expected output: Second account dashboard accessible; shared email now links both.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[account-creation]]
