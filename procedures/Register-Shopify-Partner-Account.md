---
id: proc-uuid-1
tags:
  - account-creation
  - shopify
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
updated_at: '2025-12-14T03:15:52.977Z'
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
# Register-Shopify-Partner-Account

## Summary

This procedure outlines the creation of a new Shopify partner account, providing initial access to the platform's editable features, which is a prerequisite for exploiting vulnerabilities in account settings.

## Description

In the context of testing Shopify's partner platform, registering an account simulates an attacker's setup phase. The process involves navigating to the public signup page, providing basic details like email and password, and verifying via email. This grants access to the dashboard at https://app.shopify.com, enabling further interaction with vulnerable endpoints. Expected outcomes include a functional account without restrictions on profile edits.

## Requirements

1. Valid email address for verification
2. Internet access and a web browser
3. No prior Shopify credentials needed

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account registrations via rate limiting on signup endpoints
- Implement CAPTCHA on registration forms to deter automated abuse

## Objectives

1. Gain authenticated access to Shopify partner features
2. Establish a base for injecting payloads into profile fields
3. Validate open registration as an entry vector

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Begin the registration process by accessing the public signup endpoint.

No specific command; use browser to visit https://partners.shopify.com/signup.

> Fill in the form with name, email, password, and submit. Check email for verification link.

### Step 2: Complete Verification

**Context**: Verify the account to activate dashboard access.

No specific command; click the verification link in the email.

> Upon verification, log in to access https://app.shopify.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[shopify]]
