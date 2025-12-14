---
id: proc-induce-victim-access-mobilevikings
tags:
  - phishing
  - social-engineering
  - xss
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
  - '[[Phishing]]'
updated_at: '2025-12-14T03:15:35.691Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Induce-Victim-to-Access-Authorization-Overview

## Summary

This procedure involves social engineering to get the victim to load the authorization overview page, where the malicious request is visible but the XSS is not yet triggered.

## Description

Victims must actively view their authorizations at https://mobilevikings.be/en/account/authorization/overview/ to expose the tainted data. Phishing emails or messages can lure them to this page, mimicking legitimate notifications.

## Requirements

1. Victim's contact information (email/phone)
2. Knowledge of the pending authorization
3. Ability to send deceptive communications

## Defense

Defensive measures and detection strategies:

- User education on phishing
- Email filtering for spoofed notifications
- Two-factor authentication for sensitive actions

## Objectives

1. Direct victim to the specific URL
2. Ensure page load without suspicion
3. Position for the next trigger step

## Instructions

### Step 1: Craft Phishing Message

**Context**: Create a convincing lure referencing the authorization request.

Compose an email: "You have a new authorization request from [attacker alias]. Please review at https://mobilevikings.be/en/account/authorization/overview/."

### Step 2: Deliver to Victim

**Context**: Send via email or in-app notification spoofing.

Transmit the message to the victim's registered email.

### Step 3: Monitor Engagement

**Context**: Wait for victim to access the page.

Use follow-up messages or external tracking if the payload includes beacons.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- phishing
- social-engineering
