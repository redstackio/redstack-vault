---
tags:
  - auth-bypass
  - verification
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
updated_at: '2025-12-14T17:30:35.278Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 80486499-44fa-4ebe-a9fd-7f72141a7d76
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Email-Using-Leaked-Token

## Summary

This procedure uses the extracted confirmation token to directly verify an email address on Shopify without needing to access or interact with the target email inbox.

## Description

By navigating to the confirmation endpoint with the leaked token, the attacker bypasses the intended verification flow. This exploits the lack of additional checks on token usage, allowing unauthorized email changes. The target environment is the web-based Shopify accounts portal, with outcomes including successful email update and potential for further compromise like account takeover or impersonation.

## Requirements

1. Extracted confirmation token from previous step
2. Active browser session (though not strictly required)
3. Internet access to Shopify endpoints

## Defense

Defensive measures and detection strategies:

- Enforce token single-use and invalidate after first verification
- Require additional factors like CAPTCHA on resend or confirmation
- Audit logs for direct token endpoint accesses without email events

## Objectives

1. Construct and access the confirmation URL
2. Achieve email verification bypass
3. Complete unauthorized email change

## Instructions

### Step 1: Construct Confirmation URL

**Context**: Modify the resend link to target the verification endpoint.

Take the extracted token and form: https://accounts.shopify.com/email-change/<TOKEN>/

> Example: https://accounts.shopify.com/email-change/abc123def456/

### Step 2: Navigate to Endpoint

**Context**: Submit the token directly to the server for processing.

Enter the URL in the browser address bar and load the page.

> The server validates the token and confirms the email without inbox access.

### Step 3: Validate Change

**Context**: Confirm the impact on the account.

Return to the account page to check if the email has been updated to the arbitrary address.

> Success: Email field now shows the new, unowned address as verified.

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
- verification
- shopify
