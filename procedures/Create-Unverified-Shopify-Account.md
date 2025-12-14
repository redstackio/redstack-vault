---
tags:
  - account-creation
  - unverified-email
  - shopify
type: procedure
tools:
  - '[[tools/Browser-Developer-Console]]'
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
updated_at: '2025-12-14T17:29:45.007Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 076f47ca-a2be-4509-950a-aeeda9ab1727
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Unverified-Shopify-Account

## Summary

This procedure creates a new Shopify Partners account using a victim's email address without completing email verification, setting the stage for linking external logins and creating a backdoor.

## Description

In the Shopify Partners portal, accounts created with arbitrary emails (e.g., using email aliasing like +victim) do not require immediate verification. This allows attackers to claim the email space before the victim, enabling subsequent external login linking without checks. The target environment is the web-based Shopify registration at partners.shopify.com. Expected outcomes include an unverified account with an accessible profile page containing an account ID.

## Requirements

1. Internet access to partners.shopify.com
2. Victim's email address (no control over it needed)
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Enforce mandatory email verification before any account actions, including external login linking
- Rate-limit account creations per email domain
- Monitor for rapid account creations with similar email patterns and flag for review

## Objectives

1. Establish control over the victim's email namespace in Shopify
2. Obtain an account ID for further manipulation
3. Prepare for external authentication bypass

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the Shopify Partners signup to initiate account creation.

No command required; use browser to go to https://partners.shopify.com/signup.

> Fill in the form with the victim's email (e.g., saltymermaid+victim@wearehackerone.com), name, and password. Submit to create the account.

### Step 2: Confirm Account Creation

**Context**: Verify the account is created and unverified.

No command; after submission, note the account ID from the redirect or profile URL.

> Expected: Redirect to profile or dashboard without email verification prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Console]]

## Tags

- [[account-creation]]
- [[unverified-email]]
- [[shopify]]
