---
id: proc-bruteforce-admin-001
tags:
  - brute-force
  - credential-access
  - rate-limit-bypass
type: procedure
tools:
  - '[[tools/Simple-Bruteforce-Tool]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:25:28.922Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Brute-Force-Admin-Login-with-Leaked-Usernames

## Summary

This procedure uses usernames leaked via IDOR to perform brute force attacks on the DoD chat app's admin panel login, exploiting the absence of rate limiting to guess passwords and gain unauthorized access.

## Description

Following username leakage, attackers can target the admin login endpoint (e.g., /admin/login) with a wordlist of common passwords. The lack of rate limiting allows rapid attempts without lockouts, potentially compromising the admin panel in a high-security environment. This chains directly from IDOR exploitation.

## Requirements

1. List of leaked usernames from prior IDOR step
2. Wordlist of common passwords
3. Brute force tool capable of HTTP POST requests

## Defense

Defensive measures and detection strategies:

- Implement account lockouts and rate limiting on login attempts (e.g., 5 fails per minute)
- Deploy CAPTCHA or MFA for admin logins
- Monitor login failure logs for patterns indicating brute force

## Objectives

1. Guess valid credential combinations using leaked usernames
2. Achieve unauthorized admin panel access
3. Demonstrate impact of combined IDOR and weak credential protection

## Instructions

### Step 1: Prepare Username and Password Lists

**Context**: Compile inputs for brute force from leaked data.

Create files: leaked_usernames.txt with extracted names, common_passwords.txt with guesses like 'admin', 'password123'.

> Ensure lists are formatted for tool input (one per line).

### Step 2: Launch Brute Force Attack

**Context**: Target the admin login endpoint with the tool.

Use [[tools/Simple-Bruteforce-Tool]] to automate attempts:

No specific command; configure tool to POST to /admin/login with username/password payloads.

> Tool iterates combinations until success.

### Step 3: Validate Access

**Context**: Confirm successful brute force with admin dashboard access.

Upon valid hit, note the credentials and access /admin.

> Success if dashboard loads without further auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Password Guessing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Simple-Bruteforce-Tool]]

## Tags

- brute-force
- admin-access
