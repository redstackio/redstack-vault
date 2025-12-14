---
tags:
  - idor
  - testing
  - multi-target
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:30.036Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6d82d087-3315-4964-a8cd-9cbfdf93cc00
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Unsubscription-with-Multiple-Emails

## Summary

This procedure validates the IDOR by attempting unsubscriptions on various emails, confirming the lack of verification mechanisms like CAPTCHA or prior confirmation.

## Description

Repeating the unsubscription process with different emails demonstrates the vulnerability's breadth: no reCAPTCHA, no double email entry, and no check for prior subscription status. This allows attackers with email lists to systematically disrupt user subscriptions, amplifying the abuse potential in real-world scenarios like spam campaigns or targeted harassment.

## Requirements

1. List of test email addresses
2. Access to the unsubscribe endpoint
3. Time to manually submit multiple requests

## Defense

Defensive measures and detection strategies:

- Add client-side and server-side checks for subscription ownership
- Monitor for repeated unsubscriptions from the same IP
- Use anomaly detection on email unsubscription volumes

## Objectives

1. Confirm arbitrary email targeting
2. Verify absence of protections
3. Assess scalability for mass attacks

## Instructions

### Step 1: Prepare Test Emails

**Context**: Gather emails to test, including subscribed and unsubscribed ones.

Compile a list of 5-10 emails for manual testing.

> Ensure variety to test edge cases.

### Step 2: Execute Multiple Unsubscriptions

**Context**: Submit each email via the form.

For each email, visit https://newsletter.nextcloud.com/?p=unsubscribe&id=1, enter the email, and submit.

> Expected output: Consistent success messages without barriers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- testing
