---
tags:
  - phishing
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: medium
detection_risk: high
sub_techniques: []
id: 4c3075cc-d860-4c6b-84a3-7d494c7586f0
created_at: '2025-12-11T03:47:56.758Z'
updated_at: '2025-12-11T03:47:56.758Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1189]]'
---
# Induce Victim Login via Malicious Link

## Summary

This procedure involves tricking the victim into following a login link from the malicious site and entering their PayPal credentials, triggering the security challenge.

## Description

The victim authenticates but encounters a CAPTCHA, setting the stage for the attacker to use the exposed token to complete it.

## Requirements

1. Malicious site with embedded PayPal login link.

2. Social engineering to entice click.

3. Victim with PayPal account.

## Defense

Defensive measures and detection strategies:

- Educate users on phishing risks.

- Implement referrer checks or token binding to origin.

## Objectives

1. Get victim to initiate login.

2. Trigger security challenge.

3. Prepare for replay attack.

## Instructions

### Step 1: Embed Login Link

**Context**: Place a deceptive link on the malicious site.

```html
<a href="https://www.paypal.com/signin">Login to PayPal</a>
```

> Expected: Victim clicks and enters credentials.

### Step 2: Monitor for Authentication Attempt

**Context**: Wait for victim to encounter CAPTCHA.

No specific command; monitor via site interactions or logs.

> Expected: Confirmation of login attempt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #phishing
- #social-engineering
