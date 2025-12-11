---
tags:
  - phishing
  - login-induction
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
id: 3cb642af-231a-4715-aea7-88fb6b44f6d9
created_at: '2025-12-11T06:10:40.526Z'
updated_at: '2025-12-11T06:10:40.526Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Induce Victim Login and Security Challenge

## Summary

This procedure induces the victim to follow a login link from the malicious site and enter their PayPal credentials, triggering the security challenge.

## Description

After token leak, the victim is directed to log in, queuing an authentication request that awaits CAPTCHA completion, which the attacker will handle using the leaked token.

## Requirements

1. Victim has visited the malicious site.
2. Login link embedded in the malicious page.
3. Victim's willingness to log in (via phishing).

## Defense

Defensive measures and detection strategies:

- Educate users on phishing risks.
- Implement multi-factor authentication beyond CAPTCHA.

## Objectives

1. Trigger security challenge on PayPal.
2. Queue authentication request for replay.
3. Set stage for credential exposure.

## Instructions

### Step 1: Present Login Link

**Context**: Embed a link to PayPal login in the malicious site.

Add to HTML:

```html
<a href="https://www.paypal.com/signin">Login to PayPal</a>
```

> Victim clicks and proceeds to enter credentials.

### Step 2: Victim Enters Credentials

**Context**: Victim submits login form, triggering challenge.

Ensure the site encourages login; monitor for challenge activation.

> Authentication is queued pending CAPTCHA solve.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[Phishing]]
- [[login-induction]]
