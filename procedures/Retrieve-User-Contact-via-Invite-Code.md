---
id: proc-uber-invite-disclosure
tags:
  - information-disclosure
  - privacy-leak
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-uber-join]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:52.056Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-User-Contact-via-Invite-Code

## Summary

This procedure exploits an information disclosure vulnerability in Uber's invite system by accessing the public join endpoint with an invite code, revealing the associated user's email and/or phone number without authentication. It demonstrates a privacy risk in unauthenticated endpoints handling personal data.

## Description

The Uber invite system allows users to share invite codes for sign-ups. The endpoint at www.uber.com/a/join?invite_code= exposes the inviter's contact information in the response, due to missing access controls. This can be used to harvest personal data from multiple invite codes, potentially for spam, phishing, or doxxing. The attack requires only a valid invite code and basic HTTP access, making it accessible to low-skill attackers. Expected outcomes include direct retrieval of PII, with impacts on user privacy and compliance (e.g., GDPR).

## Requirements

1. Valid Uber invite code (e.g., from public shares, emails, or social media)
2. Internet access and HTTP client (curl or browser)
3. No special privileges or credentials needed

## Defense

Defensive measures and detection strategies:

- Implement authentication or rate-limiting on invite endpoints
- Sanitize responses to remove PII from public views
- Monitor for anomalous access patterns to join endpoints (e.g., high-volume requests with varying invite codes)
- Use CAPTCHA or token validation for invite usage

## Objectives

1. Disclose email and phone numbers linked to invite codes
2. Assess privacy risks in public web endpoints
3. Enable enumeration of user contacts for further attacks

## Instructions

### Step 1: Obtain Invite Code

**Context**: Source a valid invite code to target the endpoint. Invite codes are often shared publicly or via referrals.

No command needed; manually collect from sources like forums, emails, or Uber referral links.

### Step 2: Query the Join Endpoint

**Context**: Send an HTTP GET request to the join URL with the invite code parameter to trigger the disclosure.

**Command** ([[commands/curl-access-uber-join]]):
```bash
curl "https://www.uber.com/a/join?invite_code=EXAMPLE_INVITE_CODE" -o response.html
```

> This command fetches the join page and saves it to a file. Inspect the HTML for elements containing the user's email (e.g., in meta tags or form fields) or phone number. Successful execution reveals contact info without login.

### Step 3: Parse and Extract Data

**Context**: Review the response for disclosed information.

Use grep or browser inspection:

```bash
grep -i "email\|phone" response.html
```

> Expected output includes lines like "inviter@example.com" or "+1-123-456-7890".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-uber-join]]

## Tools Used


## Tags

- information-disclosure
- privacy-leak
- web-vulnerability
