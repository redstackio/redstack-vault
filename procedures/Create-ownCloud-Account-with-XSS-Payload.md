---
id: proc-owncloud-xss-account-creation
tags:
  - xss
  - account-creation
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.729Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-ownCloud-Account-with-XSS-Payload

## Summary

This procedure registers a new ownCloud account using a username that embeds an XSS payload, exploiting the lack of input sanitization to prepare for self-injection in automated emails.

## Description

In the ownCloud platform, the account registration process does not sanitize user-supplied usernames, allowing arbitrary HTML and JavaScript to be stored. This payload is later inserted into welcome emails sent via a third-party service (HubSpot), resulting in self-XSS when viewed in a compatible mail client. The attack requires no privileges beyond public registration and targets only the attacker's own email session, limiting impact to potential local effects like cookie theft if the mail client executes JS.

## Requirements

1. Access to the ownCloud web registration endpoint (publicly accessible)
2. A valid email address for receiving the confirmation email
3. Web browser to submit the registration form

## Defense

Defensive measures and detection strategies:

- Implement server-side sanitization of usernames using HTML entity encoding or allowlisting
- Use email templating libraries that escape user inputs (e.g., via OWASP guidelines)
- Monitor for anomalous characters in registration logs

## Objectives

1. Inject XSS payload into username without rejection
2. Store payload for later use in email generation
3. Set up conditions for self-XSS observation

## Instructions

### Step 1: Prepare XSS Payload

**Context**: Craft a simple XSS payload that breaks out of HTML context and executes JavaScript, suitable for email injection.

No command required; manually construct the payload: "><img src="c" onerror=alert(1)><script>alert(1)</script>

> This payload uses an image tag with onerror to trigger alert(1), followed by a script tag for redundancy. Expected output: Payload string ready for use.

### Step 2: Submit Registration Form

**Context**: Use the ownCloud signup page to create the account, entering the payload as the username.

Navigate to the registration URL (e.g., https://your-owncloud-instance.com/register) and fill in:
- Username: "><img src="c" onerror=alert(1)><script>alert(1)</script>
- Email: your-test-email@example.com
- Password: any valid password

Submit the form.

> Expected output: Success message or redirect to login, with account created. If rejected, the sanitization is in place (attack fails).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[self-xss]]
- [[owncloud]]
