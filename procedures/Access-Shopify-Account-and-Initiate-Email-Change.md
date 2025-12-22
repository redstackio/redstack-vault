---
tags:
  - auth-bypass
  - shopify
  - email-change
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
updated_at: '2025-12-14T17:30:35.285Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: aac3cfc7-4d1f-4701-be5a-7dd1fc04a396
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Account-and-Initiate-Email-Change

## Summary

This procedure outlines logging into a Shopify account and initiating the email change process to trigger the generation of a vulnerable resend link containing a leaked confirmation token.

## Description

In the context of exploiting the Shopify email verification bypass, this step requires authenticated access to the account settings page. By starting the email change with an arbitrary address, the system generates a verification flow where the token is exposed client-side. This is a prerequisite for token extraction and sets up the vulnerability exploitation. Expected outcome is the display of the verification interface without actual email sending being necessary for the attack.

## Requirements

1. Valid Shopify account credentials
2. Web browser with JavaScript enabled
3. Internet access to https://accounts.shopify.com

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on email change attempts
- Monitor for unusual email change initiations from authenticated sessions
- Use token binding to sessions to prevent reuse outside the original context

## Objectives

1. Gain authenticated access to account settings
2. Trigger email change flow for token generation
3. Position for token leakage observation

## Instructions

### Step 1: Log In to Account Page

**Context**: Authenticate to access the protected account settings where email management is available.

Navigate to https://accounts.shopify.com/account and enter valid credentials to log in.

> Upon successful login, the account dashboard loads, displaying current email and change options.

### Step 2: Initiate Email Change

**Context**: Start the email modification process to invoke the vulnerable verification mechanism.

Locate the email field on the account page and click the 'Change' button.

> This opens the input field for a new email address.

### Step 3: Submit Arbitrary Email

**Context**: Enter a non-owned email to simulate the attack without real impact on the attacker's inbox.

Input an arbitrary email, e.g., victim@example.com, and submit.

> A verification message appears: 'Verification email sent. We sent you an email to verify that you own "victim@example.com". We'll change your email once you verify that you own it.' with resend and cancel options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- shopify
- email-change
