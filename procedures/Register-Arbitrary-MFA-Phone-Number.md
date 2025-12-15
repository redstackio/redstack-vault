---
id: proc-mfa-phone-reg-001
tags:
  - mfa
  - authentication
  - access-control
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/curl-mfa-register]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:24:47.680Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Register Arbitrary MFA Phone Number

## Summary

This procedure exploits a lack of verification in the MFA phone number registration feature, allowing a user with account access to bind any arbitrary phone number to their MFA settings without confirming the current MFA code. It is primarily used in scenarios where an attacker has initial credential access and seeks to weaken or redirect MFA for persistence or full takeover.

## Description

In vulnerable web applications like the reported Superhuman/Grammarly system, the MFA registration endpoint fails to enforce checks for the active MFA method (e.g., current TOTP or SMS code) when adding a new phone number. An attacker logs in with stolen credentials, navigates to account settings, and submits a new phone number. The system accepts it without additional authentication, potentially allowing the attacker to receive future MFA codes on their device. This was discovered through manual testing of the feature, with low severity as no users were impacted, but it could enable account hijacking if combined with phishing or credential theft. Expected outcomes include successful phone association and control over 2FA flows.

## Requirements

1. Valid login credentials or session token for the target account
2. Access to a web browser or API testing tool (e.g., curl or Postman)
3. Knowledge of the target's MFA settings page URL (e.g., /settings/mfa)

## Defense

Defensive measures and detection strategies:

- Enforce current MFA verification for any changes to authentication settings
- Implement rate limiting on MFA registration attempts
- Log and monitor all MFA modifications, alerting on suspicious phone number changes (e.g., international or rapid swaps)
- Use device binding or additional context checks (e.g., IP geolocation) for MFA updates

## Objectives

1. Bind attacker-controlled phone number to victim account MFA
2. Bypass existing MFA protections during registration
3. Enable persistent access via redirected 2FA codes

## Instructions

### Step 1: Gain Initial Account Access

**Context**: Obtain a valid session to the target account, as the vulnerability requires registered user privileges.

Log in using known credentials via the web interface.

**Expected Output**: Active session with access to account settings.

### Step 2: Navigate to MFA Settings

**Context**: Locate the phone number registration feature within the account dashboard.

Browse to the MFA or security settings page (e.g., https://app.target.com/settings/mfa).

**Expected Output**: Form or interface for adding/verifying phone numbers.

### Step 3: Submit Arbitrary Phone Number

**Context**: Exploit the missing verification by submitting a new phone without current MFA input.

Use the form to enter an arbitrary phone number (e.g., +1-555-123-4567) and submit. If API-based, execute [[commands/curl-mfa-register]] to test:

```bash
curl -X POST https://api.target.com/mfa/register-phone \
  -H "Cookie: session=<valid_session_cookie>" \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "+15551234567"}' \
  --insecure
```

> This command sends a POST request to the registration endpoint with the arbitrary phone number, bypassing any current MFA check. Expected output: HTTP 200 with success message like {"message": "Phone registered successfully"}. If using a browser, inspect the network tab to confirm no additional auth parameters are required.

### Step 4: Verify Registration

**Context**: Confirm the phone is now associated and functional for MFA.

Attempt a logout and re-login, requesting an SMS code to the new number.

**Expected Output**: MFA code received on the attacker's phone.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-mfa-register]]

## Tools Used


## Tags

- mfa
- authentication
- access-control
