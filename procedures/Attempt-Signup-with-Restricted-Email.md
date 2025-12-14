---
id: proc-attempt-signup-restricted
tags:
  - saml
  - signup
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hackerone-signup-standard]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:58.367Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Attempt Signup with Restricted Email

## Summary

This procedure initiates a user signup on HackerOne using a restricted domain email (e.g., @hackerone.com) to trigger and observe the SAML SSO redirect, confirming domain enforcement is active.

## Description

In the context of testing SAML domain restrictions, this step involves submitting a standard signup form with a prohibited email domain. The target environment is HackerOne's web signup endpoint, expecting a redirect to SSO for restricted domains. Prerequisites include public access to hackerone.com. Successful execution reveals the enforcement mechanism without creating an account.

## Requirements

1. Web browser or HTTP client (e.g., curl)
2. Knowledge of restricted domains (e.g., @hackerone.com)
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Monitor signup attempts for restricted domains and log redirects to SSO
- Implement rate limiting on signup endpoints to prevent probing

## Objectives

1. Confirm SAML domain enforcement triggers redirect
2. Gather baseline response for modification in subsequent steps
3. Identify the exact redirect path for bypass validation

## Instructions

### Step 1: Submit Signup Form

**Context**: Fill and submit the HackerOne signup form to observe the restricted domain behavior.

**Command** ([[commands/hackerone-signup-standard]]):

```bash
curl -X POST https://hackerone.com/users \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'user[name]=Test User&user[username]=testuser&user[email]=test@hackerone.com&user[password]=password123&user[password_confirmation]=password123'
```

> This command simulates the signup POST request. Expected output includes a JSON response with {"redirect_path":"/users/saml/sign_in?email=test%40hackerone.com"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/hackerone-signup-standard]]

## Tools Used


## Tags

- saml
- signup
- recon
