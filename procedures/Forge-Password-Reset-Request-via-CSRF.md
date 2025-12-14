---
tags:
  - csrf
  - exploit
  - web
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: af9ca32b-e4ca-45e9-8193-0dc4593033a6
created_at: '2025-12-14T17:27:23.429Z'
updated_at: '2025-12-14T17:27:23.429Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Forge-Password-Reset-Request-via-CSRF

## Summary

This procedure exploits a CSRF vulnerability in the password reset functionality by creating a malicious webpage that forges a request on behalf of the victim, forcing an unintended password reset and potentially leading to account compromise.

## Description

CSRF attacks trick authenticated users into submitting malicious requests to a vulnerable endpoint. In RelateIQ, the password reset lacks token validation, allowing an attacker to craft an HTML page with an auto-submitting form targeting the reset endpoint. When the victim visits the page (e.g., via a phishing link), their browser sends the request using their session cookies, initiating a reset. The attacker can then attempt to intercept the new password setup link or predict it. This requires social engineering to lure the victim and assumes the victim is logged in or has session affinity. Outcomes include unauthorized access if the attacker controls the subsequent setup.

## Requirements

1. Knowledge of the vulnerable endpoint from prior inspection
2. Victim's email address
3. Hosting for the malicious HTML page (e.g., attacker-controlled server)
4. Ability to deliver the POC link to the victim (e.g., email or chat)

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all POST requests and validate them
- Use SameSite cookies to prevent cross-site submission
- Log and alert on password resets from suspicious user agents or referrers
- Educate users on phishing and unexpected reset emails

## Objectives

1. Force a password reset via forged cross-origin request
2. Trigger delivery of a new password setup link to the victim
3. Enable potential interception or takeover of the account

## Instructions

### Step 1: Craft Malicious HTML Page

**Context**: Create a simple webpage that auto-submits a form to the password reset endpoint.

Use a text editor to build an HTML file with a hidden form targeting the RelateIQ endpoint (e.g., POST to `/reset-password` with victim's email in the body). Include JavaScript to submit on load:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://relateiq.com/reset-password" method="POST">
    <input type="hidden" name="email" value="victim@example.com">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

> Host this on an external domain (e.g., attacker.com/poc.html) to ensure cross-origin.

### Step 2: Deliver to Victim

**Context**: Trick the victim into visiting the page while they have an active session with RelateIQ.

Send a phishing email or message with a link to the hosted HTML page, disguised as a legitimate resource (e.g., "Click here to view your update"). Ensure the victim is authenticated to RelateIQ for session cookies to be included.

> Expected output: Victim's browser loads the page and submits the form invisibly.

### Step 3: Monitor and Intercept

**Context**: Observe the effects and attempt to gain access.

Check the victim's email for the password reset notification. If accessible (e.g., via prior compromise), use the link to set a known password. Alternatively, predict or brute-force the setup if tokens are weak.

> Expected output: Successful reset confirmation; attacker can now login with new credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[web]]
- [[account-takeover]]
