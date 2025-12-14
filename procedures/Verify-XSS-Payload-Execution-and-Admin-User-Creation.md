---
id: uuid-verify-execution
tags:
  - xss
  - verification
  - wordpress
  - compromise-check
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.405Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify XSS Payload Execution and Admin User Creation

## Summary

This procedure validates the success of the XSS payload by monitoring network traffic and checking the WordPress admin panel for the new unauthorized user.

## Description

After payload delivery, inspect browser developer tools for AJAX requests to confirm nonce fetch and user creation POST. Access the WordPress dashboard to verify the attacker's admin account. This step ensures the chain's impact, highlighting full compromise in WordPress environments via XSS.

## Requirements

1. Browser with logged-in admin session
2. Access to WordPress admin panel
3. Developer tools enabled

## Defense

Defensive measures and detection strategies:

- Enable logging for admin actions and review for anomalous user creations
- Use intrusion detection systems to flag unexpected AJAX calls to admin endpoints
- Regularly audit user accounts for unauthorized additions

## Objectives

1. Confirm AJAX requests succeeded
2. Validate new admin user in database
3. Assess overall site compromise

## Instructions

### Step 1: Monitor Network Traffic

**Context**: Load the malicious URL and watch for requests.

Open DevTools (F12 > Network tab), visit the crafted URL while logged in, and filter for /wp-admin/user-new.php.

Look for: GET request followed by POST with form data including user_login=attacker.

> 200 OK on POST indicates successful creation.

### Step 2: Check WordPress Users

**Context**: Log into /wp-admin and inspect users.

Navigate to Users > All Users in WordPress dashboard.

Search for 'attacker' or check recent additions; attempt login with attacker@site.com / attacker.

> New admin user confirms compromise.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[verification]]
- [[wordpress]]
- [[compromise-check]]
