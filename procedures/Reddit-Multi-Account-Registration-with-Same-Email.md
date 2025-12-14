---
tags:
  - registration
  - email-reuse
  - reddit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.312Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d1671a21-1b04-4948-b66f-4465eb35c722
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Reddit-Multi-Account-Registration-with-Same-Email

## Summary

This procedure exploits Reddit's lack of unique email enforcement during registration, allowing an attacker to create multiple accounts linked to the same email address, setting the stage for enumeration and takeover.

## Description

In the attack scenario, the attacker first registers their own account with a controlled email, verifies it, then simulates or waits for a victim to register using the same email (via social engineering or direct control). The attacker verifies the victim's registration as well. This ties both accounts to the single email inbox, which the attacker controls. The target environment is Reddit's web registration system, requiring only a browser and email access. Expected outcomes include multiple verified accounts per email, enabling subsequent phases.

## Requirements

1. Web browser with internet access
2. Control over an email address (e.g., Gmail account)
3. No prior Reddit account or credentials needed

## Defense

Defensive measures and detection strategies:

- Enforce unique email addresses per account during registration with database constraints
- Implement rate limiting on registrations and verifications per email
- Monitor for multiple verifications from the same IP or patterns of reuse
- Use CAPTCHA or additional authentication for registrations

## Objectives

1. Establish multiple accounts tied to one email for enumeration
2. Gain verification control over victim registrations
3. Prepare for username discovery without alerting the victim

## Instructions

### Step 1: Attacker Account Registration

**Context**: Initiate the first account to test and link the email.

**Action**:
Navigate to `https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2F`, enter email `account@gmail.com`, username `attacker1`, set a password, and submit.

> This creates the account and triggers an email verification. Successful registration shows a confirmation page.

### Step 2: Verify Attacker Account

**Context**: Confirm the account to enable logins and further actions.

**Action**:
Check the email inbox, open the verification email from Reddit, and click the link.

> Verification completes, allowing login. Look for a success message on Reddit.

### Step 3: Log Out

**Context**: Avoid session conflicts for next registration.

**Action**:
Click the avatar and select 'Log Out'.

> Returns to login page, confirming no active session.

### Step 4: Victim Account Registration

**Context**: Register the second account using the same email.

**Action**:
Repeat navigation to registration page, use same email `account@gmail.com`, username `user1`, set password, submit.

> Reddit accepts despite reuse, sending another verification email.

### Step 5: Verify Victim Account

**Context**: Secure the victim account under attacker email control.

**Action**:
Check inbox for new verification email and click link for `user1`.

> Account verified; both now linked.

### Step 6: Log Out Again

**Context**: Clean up session.

**Action**:
Log out via menu.

> Prepares for enumeration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- registration
- email-reuse
- reddit
