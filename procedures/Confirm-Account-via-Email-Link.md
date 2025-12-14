---
id: proc-confirm-account-email
tags:
  - account-activation
  - email-confirmation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/visit-email-confirmation-link]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.101Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Account-via-Email-Link

## Summary

This procedure finalizes the account creation by activating the newly registered account using the email confirmation link, ensuring the malicious UUID is persisted in the application database.

## Description

After submitting the account creation request, the server emails a confirmation link containing an email_token. Visiting this link activates the account, storing the injected UUID. This step is crucial for the stored XSS to become active and executable upon rendering.

## Requirements

1. Receipt of confirmation email from the target application
2. Valid email_token from the link
3. Browser or curl access to the confirmation URL

## Defense

Defensive measures and detection strategies:

- Rate-limit confirmation attempts
- Expire tokens quickly
- Log and monitor unusual activation patterns

## Objectives

1. Activate the account with stored payload
2. Persist XSS in database
3. Prepare for payload execution

## Instructions

### Step 1: Retrieve Confirmation Link

**Context**: Check the email inbox for the activation link, typically in the format https://app.upserve.com/b/{brand_pretty_url}?email_token={token}.

### Step 2: Visit the Link

**Context**: Access the URL to confirm; can be done via browser or curl to automate.

**Command** ([[commands/visit-email-confirmation-link]]):

```bash
curl -X GET "https://app.upserve.com/b/test-brand?email_token=2aa7296c678e11e7ab2f0242ac110002" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36" \
  -H "Accept: text/html"
```

> Expect a success page or redirect; account is now active with malicious UUID stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/visit-email-confirmation-link]]

## Tools Used


## Tags

- account-activation
- email
