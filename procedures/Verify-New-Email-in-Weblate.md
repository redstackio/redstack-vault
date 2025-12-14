---
tags:
  - email-verify
  - weblate
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-weblate-email]]'
verified: false
platforms:
  - Web
  - Django
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.300Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5ef2db01-6852-477e-8bbc-9d8abce3e81b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Verify-New-Email-in-Weblate

## Summary

This procedure verifies the newly added email in Weblate using the provided verification link, enabling it for use in further account manipulation without additional authentication.

## Description

After adding the email, Weblate sends a verification link with parameters like verification_code and id. Accessing this GET endpoint /accounts/complete/email/ with the active session confirms the email, making it usable for primary changes. This step requires the session cookie but no password.

## Requirements

1. Verification link from the added email (code, id, type)
2. Active session cookie for the account
3. Access to the controlled email inbox

## Defense

Defensive measures and detection strategies:

- Limit email verifications per session or time window
- Require re-authentication for verification links
- Audit logs for verification accesses from unusual IPs

## Objectives

1. Enable the controlled email for account use
2. Confirm addition success
3. Enable primary email switch

## Instructions

### Step 1: Retrieve Verification Link

**Context**: Check the controlled email for the verification URL.

Extract parameters: verification_code=51554eb9e31b44d6a48f8b41acda9a43, id=uy7kg0n6l8nhmihjvcgwzg3dpama80gn, type=reset.

### Step 2: Access Verification Endpoint

**Context**: Send GET request with session to verify.

**Command** ([[commands/curl-verify-weblate-email]]):
```bash
curl -X GET 'https://target.weblate.org/accounts/complete/email/?verification_code=51554eb9e31b44d6a48f8b41acda9a43&id=uy7kg0n6l8nhmihjvcgwzg3dpama80gn&type=reset' \
  -H 'Cookie: sessionid=your_session_cookie'
```

> Expected output: Success page or redirect confirming verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/curl-verify-weblate-email]]

## Tools Used


## Tags

- email-verify
- weblate
