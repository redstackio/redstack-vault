---
id: 992d10de-acec-46f3-bfa2-ac06fb20c709
name: Account-Takeover-via-Password-Reset-and-IDOR-on-API-Parameters
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:53.859187+00:00'
updated_at: '2023-04-06T03:55:53.870380+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Account Takeover]]'
  - '[[tags/IDOR on API Parameters]]'
  - '[[tags/Password Reset Feature]]'
commands:
  - '[[commands/curl-post-changepass-request]]'
platforms:
  - Web
tools: []
validated: true
---

# Account-Takeover-via-Password-Reset-and-IDOR-on-API-Parameters

## Summary

This procedure exploits an insecure password reset feature combined with an Insecure Direct Object Reference (IDOR) vulnerability in an API endpoint to perform an account takeover. By sending a crafted POST request to the change password API without proper user validation, an attacker can reset the password of any target account using only the victim's email or user ID, gaining unauthorized access.

## Description

The attack targets web applications where the password reset functionality exposes an API endpoint, such as /api/changepass, that accepts email or user ID parameters without verifying the requester's ownership. This IDOR flaw allows arbitrary password changes. The procedure assumes the attacker has identified the victim's email through reconnaissance (e.g., via public sources or prior enumeration). Once executed, the attacker can log in with the new password to access sensitive data, perform actions on behalf of the victim, or escalate further. This is common in poorly secured SaaS platforms or custom web apps lacking rate limiting, CAPTCHA, or token-based validation on reset flows. Expected outcomes include full account control, potentially leading to data theft or lateral movement.

## Requirements

1. Knowledge of the victim's email address or user ID (obtained via reconnaissance or social engineering).
2. Network access to the target's web application API endpoint (e.g., no firewall blocking).
3. Tools like curl or a proxy (e.g., Burp Suite) for sending HTTP requests.
4. No authentication required for the initial reset request due to the vulnerability.

## Defense

- Implement server-side validation to ensure only the account owner can initiate password resets, using secure tokens or one-time links sent via email.
- Enforce multi-factor authentication (MFA) and rate limiting on reset endpoints to prevent brute-force or unauthorized attempts.
- Monitor API logs for anomalous requests, such as password changes from unfamiliar IPs or targeting multiple accounts.
- Use Web Application Firewalls (WAFs) to detect IDOR patterns and require CAPTCHA for sensitive actions.

## Objectives

1. Change the victim's password without authorization to gain login access.
2. Access the victim's account to exfiltrate data or perform unauthorized actions.
3. Demonstrate the impact of IDOR in password management flows for remediation.

## Instructions

### Step 1: Identify Victim's Email or User ID

**Context**: Gather the target's identifier to include in the API request. This step ensures the request targets the correct account without needing prior authentication.

Use reconnaissance techniques (e.g., OSINT or prior enumeration) to obtain the email. No specific command is needed here, but verify the email format is valid for the target application.

> Expected: Valid email like "victim@example.com" confirmed via public sources or app enumeration.

### Step 2: Craft and Send the Password Change Request

**Context**: Exploit the IDOR by sending a POST request to the /api/changepass endpoint with the victim's email and a new password. The lack of validation allows the change to succeed.

**Command** ([[commands/curl-post-changepass-request]]):

```bash
curl -X POST https://target.com/api/changepass \
  -H "Content-Type: application/json" \
  -d '{"email":"$_VICTIM_EMAIL","password":"$_NEW_PASSWORD"}'
```

> This command sends the JSON payload to the API. Replace placeholders with actual values. If the endpoint uses form data instead of JSON, adjust the Content-Type to application/x-www-form-urlencoded and format accordingly (e.g., email=$_VICTIM_EMAIL&password=$_NEW_PASSWORD). Expected output is a success response (e.g., HTTP 200 with message like "Password updated successfully"), indicating the change was applied without errors.

### Step 3: Verify Account Access

**Context**: Test the takeover by attempting to log in with the new credentials to confirm control.

Use the application's login endpoint or UI to authenticate with the victim's email and the new password set in Step 2.

> Expected: Successful login response or dashboard access, confirming the account takeover. If failed, check for additional validations like email confirmation links.
