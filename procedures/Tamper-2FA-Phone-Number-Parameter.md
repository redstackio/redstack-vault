---
tags:
  - parameter-tampering
  - 2fa
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.377Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 624fd52c-d720-434a-ac56-c2658084032e
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Tamper 2FA Phone Number Parameter

## Summary

This procedure intercepts the 2FA activation request and modifies the phone number parameter to the victim's, exploiting client-side trust and lack of server validation to hijack OTP delivery.

## Description

During Shopify's 2FA setup, the HTTP POST request includes a phone number parameter without ownership verification. Using a proxy, the attacker replaces their entered number with the victim's, causing subsequent OTPs to target the victim. This enables association of the victim's phone with the attacker's session, setting up rate limit exhaustion. Tested via Burp Suite on the /account/two_factor endpoint.

## Requirements

1. Active Shopify account at 2FA setup stage
2. Burp Suite proxy active
3. Victim's phone number known
4. Browser traffic routed through proxy

## Defense

Defensive measures and detection strategies:

- Implement server-side phone number verification (e.g., via silent SMS challenge)
- Validate phone numbers against account ownership
- Log and rate-limit parameter changes in auth requests

## Objectives

1. Intercept and alter 2FA setup request
2. Associate victim's phone without authentication
3. Enable targeted OTP disruption

## Instructions

### Step 1: Enter Dummy Phone and Intercept Request

**Context**: Input a placeholder to capture the request structure.

No command; UI and proxy action:

- In 2FA form, enter attacker's phone (e.g., +1-555-123-4567)
- Submit form; Burp Suite intercepts the POST request

> Expected: Request shows parameters like phone=%2B1-555-123-4567 in body.

### Step 2: Modify and Forward Request

**Context**: Replace phone parameter to victim's number.

In Burp Repeater or Proxy:

- Edit phone parameter to victim's (e.g., +1-555-987-6543)
- Forward the request to server

> Expected: Server processes without error, 2FA setup completes for tampered number.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- parameter-tampering
- 2fa
