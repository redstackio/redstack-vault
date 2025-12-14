---
tags:
  - account-creation
  - shopify
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:43.852Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 48d58a3b-8346-47bb-98f1-dbb74f54c259
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create-New-Shopify-Account

## Summary

This procedure registers a new Shopify account during the Collabs early access application, providing the credentials needed for onboarding and authenticated access.

## Description

As part of the attack chain for Shopify Collabs XSS exploitation, creating a new account is a legitimate step that grants access to the platform's creator features. The process occurs within the application flow, requiring basic user details like email and password. Once completed, it redirects to the onboarding page, enabling further setup. This step ensures the attacker has a valid session for the vulnerability exploitation.

## Requirements

1. Web browser
2. Valid email address for registration
3. No prior Shopify account

## Defense

Defensive measures and detection strategies:

- Rate-limit new account creations per IP/email domain
- Require email verification before full access
- Log and monitor registration patterns for abuse

## Objectives

1. Register a new Shopify ID
2. Obtain credentials for login
3. Redirect to onboarding for next steps

## Instructions

### Step 1: Enter Registration Details

**Context**: Provide necessary information during the prompted registration.

Fill in the required fields such as email, password, and store name in the registration form.

> Submits the form to create the account. Expected output: Confirmation of account creation and redirect.

### Step 2: Verify Redirect

**Context**: Confirm the post-registration flow advances correctly.

Observe the automatic redirect after submission.

> Redirects to https://collabs.shopify.com/onboarding. Expected output: Onboarding page loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[shopify]]
- [[web]]

