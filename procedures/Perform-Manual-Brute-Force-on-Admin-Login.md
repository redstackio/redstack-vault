---
id: proc-uuid-3
name: Perform-Manual-Brute-Force-on-Admin-Login
tags:
  - brute-force
  - credential-access
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:28:36.585Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Perform-Manual-Brute-Force-on-Admin-Login

## Summary

This procedure demonstrates manually brute-forcing the WordPress admin password using a known username, exploiting the absence of rate-limiting to gain unauthorized access.

## Description

With a valid username like 'frank', attackers submit repeated password guesses to /wp-login.php. The lack of limits allows trial-and-error until success, potentially granting full admin control over the site, as seen in the Nextcloud WordPress vulnerability.

## Requirements

1. Known valid username from enumeration
2. List of common passwords (e.g., password, 123456, admin)
3. Web browser for form submissions

## Defense

Defensive measures and detection strategies:

- Enable rate-limiting (e.g., 5 attempts per IP per hour)
- Use strong password policies and enforce MFA
- Monitor failed login attempts in access logs

## Objectives

1. Guess the admin password
2. Achieve login to wp-admin
3. Obtain administrative privileges

## Instructions

### Step 1: Prepare Password List

**Context**: Compile common passwords to test.

Manually list guesses like 'password', 'frank123', 'admin'.

> Focus on weak or default passwords common in WordPress installs.

### Step 2: Submit Guesses on Login Form

**Context**: Use the login form to attempt credentials repeatedly.

At https://target.com/wp-login.php, enter username 'frank' and a password guess, submit, and repeat without interruption.

> On failure, refresh and try the next. Success redirects to the dashboard upon correct password.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

-

## Tools Used

-

## Tags

- [[brute-force]]
- [[credential-access]]
- [[wordpress]]
