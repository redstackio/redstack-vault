---
tags:
  - password-brute-force
  - credential-access
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
updated_at: '2025-12-14T17:33:12.174Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Password Guessing]]'
id: abe15eb6-6aee-4417-8cf8-83ee85e42a54
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-Passwords-for-Valid-Accounts

## Summary

This procedure uses a list of valid usernames to brute-force passwords against the login API, exploiting insufficient per-user rate limits to guess weak credentials and achieve authentication.

## Description

With valid usernames identified, attackers import them as payloads alongside a password wordlist (e.g., common or simple 9-character passwords) into an automation tool. POST requests are sent to https://api.outpost.co/api/v1/login testing combinations until a successful response (e.g., no error, session token issued). The weak protections allow repeated attempts per user without effective blocking, leading to account compromise. This is effective against web apps with poor password policies.

## Requirements

1. List of valid usernames from prior enumeration
2. Password wordlist (e.g., rockyou.txt or custom simple passwords)
3. Automation tool for combinatorial requests (e.g., Burp Intruder, Hydra)
4. Logging for success detection

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and account lockouts after 5-10 failed attempts
- Implement progressive rate limiting per username/IP
- Monitor for brute-force patterns via SIEM
- Require MFA for all logins

## Objectives

1. Guess correct passwords for valid usernames
2. Obtain authentication tokens or sessions
3. Enable targeted account access

## Instructions

### Step 1: Prepare Payloads

**Context**: Load valid usernames and password list into the brute-forcing tool.

In Burp Intruder, set position for username from valid list and password from wordlist in the POST body.

> Expected: Configured attack with combinatorial testing.

### Step 2: Execute Brute-Force

**Context**: Launch requests to test combinations until success.

Start the attack on https://api.outpost.co/api/v1/login; monitor for responses without 'Password does not match username'.

> Expected: Successful hit with auth response (e.g., 200 OK, redirect, or token).

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

- [[password-brute-force]]
- [[credential-access]]
