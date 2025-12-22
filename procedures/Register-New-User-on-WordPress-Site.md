---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - wordpress
  - registration
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/wp-register-user]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:32:48.300Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Register-New-User-on-WordPress-Site

## Summary

This procedure registers a new low-privilege user on a WordPress site where user registrations are enabled, providing initial access for further exploitation such as privilege escalation.

## Description

WordPress sites with open registrations allow unauthenticated users to create accounts via the REST API or registration forms. This step establishes a foothold by creating an account with subscriber-level permissions, which can then be escalated. The target environment is a standard WordPress installation (version 5.x+), and success depends on the 'Anyone can register' setting being enabled in the site's general settings.

## Requirements

1. HTTP access to the WordPress site
2. Registrations enabled (check via /wp-admin/options-general.php)
3. No CAPTCHA or additional validation on registration

## Defense

Defensive measures and detection strategies:

- Disable open registrations or require admin approval
- Implement CAPTCHA on registration forms
- Monitor for unusual registration spikes via logs

## Objectives

1. Create a valid user account
2. Obtain login credentials for the new user
3. Establish initial authenticated access

## Instructions

### Step 1: Send Registration Request

**Context**: Use the WordPress REST API to POST user creation data to the /wp/v2/users endpoint.

**Command** ([[commands/wp-register-user]]):
```bash
curl -X POST https://target.com/wp-json/wp/v2/users -d '{"username":"attacker","email":"attacker@example.com","password":"weakpass123"}' -H 'Content-Type: application/json'
```

> This command sends a JSON payload to register the user. Expected output is a 201 response with user details including ID and capabilities.

### Step 2: Verify Registration

**Context**: Log in with the new credentials to confirm access.

**Command** ([[commands/wp-login-user]]):
```bash
curl -c cookies.txt -d 'log=attacker&pwd=weakpass123' https://target.com/wp-login.php
```

> Successful login returns a session cookie. Check for 302 redirect to dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques

-

## Commands Used

- [[commands/wp-register-user]]
- [[commands/wp-login-user]]

## Tools Used

-

## Tags

- [[wordpress]]
- [[registration]]
