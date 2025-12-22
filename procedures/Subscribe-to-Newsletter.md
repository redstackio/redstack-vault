---
tags:
  - web
  - subscription
  - testing
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
updated_at: '2025-12-14T17:25:30.040Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d1d4448-c952-45bd-b39f-fb9a4a6d4f51
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Subscribe-to-Newsletter

## Summary

This procedure subscribes a test email to the Nextcloud newsletter, creating a valid entry for subsequent unsubscription testing and validating the system's confirmation mechanisms.

## Description

To test the unsubscribe IDOR, first establish a legitimate subscription using a controlled email. The process involves filling a form with email confirmation, solving reCAPTCHA, and clicking a verification link in the received email from newsletter@nextcloud.com. This step confirms the email is now in the subscribed list, setting up the environment for exploitation without alerting the system to anomalous activity.

## Requirements

1. Valid email address for testing
2. Ability to receive and access emails
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Enforce reCAPTCHA on all subscription forms to prevent automation
- Log subscription attempts and flag rapid or suspicious patterns

## Objectives

1. Add email to newsletter list
2. Receive and confirm subscription
3. Prepare for unsubscription testing

## Instructions

### Step 1: Fill Subscription Form

**Context**: Enter details to initiate subscription.

Visit https://newsletter.nextcloud.com/?p=subscribe&id=1, enter your email twice, solve reCAPTCHA, and submit.

> Expected output: Redirect or message indicating subscription pending confirmation.

### Step 2: Confirm via Email

**Context**: Verify the subscription to activate it.

Check inbox for email from newsletter@nextcloud.com and click the confirmation link.

> Expected output: Confirmation of active subscription.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- subscription
