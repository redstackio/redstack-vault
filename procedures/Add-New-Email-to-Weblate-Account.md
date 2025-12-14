---
tags:
  - auth-bypass
  - email-add
  - weblate
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-add-weblate-email]]'
verified: false
platforms:
  - Web
  - Django
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.301Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 83ca6c6b-b2e3-4fad-acfd-905ee93bf7f9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Add-New-Email-to-Weblate-Account

## Summary

This procedure adds a new email address to a Weblate account without requiring the current password, exploiting a design flaw in the /accounts/email/ endpoint. It enables attackers with temporary session access to prepare for account takeover by associating a controlled email.

## Description

In Weblate, the email addition process uses a POST request to /accounts/email/ that only requires a CSRF token and the new email, bypassing password authentication. This differs from password changes which enforce current password verification. The attacker must have a valid session cookie. Upon success, a verification email is sent to the new address, allowing further manipulation.

## Requirements

1. Valid session cookie for the target Weblate account
2. Attacker's controlled email address (e.g., user1+hackerone@example.com)
3. CSRF token extracted from the session or login page
4. Network access to the Weblate instance

## Defense

Defensive measures and detection strategies:

- Require current password for any email modifications
- Implement multi-factor authentication (MFA) for account changes
- Monitor for rapid email additions from session anomalies
- Log and alert on email verification events without password checks

## Objectives

1. Associate controlled email with victim's account
2. Trigger verification process for the new email
3. Prepare for primary email switch and password reset

## Instructions

### Step 1: Prepare Session and CSRF

**Context**: Obtain the session cookie and CSRF token by logging into the account or hijacking the session.

Inspect the login response or profile page for the CSRF token.

### Step 2: Submit Email Addition Request

**Context**: Send the POST request to add the email, bypassing password auth.

**Command** ([[commands/curl-add-weblate-email]]):
```bash
curl -X POST 'https://target.weblate.org/accounts/email/' \
  -H 'Cookie: sessionid=your_session_cookie' \
  -H 'X-CSRFToken: SLhsGgqa4B8Y0DOFLPNQEbu9MyV64vCewoi8mtWTBwc5GSIbxquZBx8lJ6IZyvkf' \
  -d 'csrfmiddlewaretoken=SLhsGgqa4B8Y0DOFLPNQEbu9MyV64vCewoi8mtWTBwc5GSIbxquZBx8lJ6IZyvkf&email=user1%2Bhackerone%40example.com&content='
```

> This command adds the email and sends a verification link. Expected output: HTTP 302 redirect or success message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/curl-add-weblate-email]]

## Tools Used


## Tags

- auth-bypass
- email-add
- weblate
