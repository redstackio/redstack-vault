---
tags:
  - username-enumeration
  - information-disclosure
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:44.540Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 18db7571-c277-454d-aade-75b33dd1a304
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Test-Non-Existent-Username-for-Enumeration

## Summary

This procedure tests a fabricated username against the Nextcloud login to capture the error message for non-existent users, establishing a baseline for differentiation.

## Description

Username enumeration relies on inconsistent error handling in the Nextcloud admin panel. By submitting a non-existent username like 'charlietango', the application returns a generic 'Invalid Username' message. This is performed in a web browser on a PHP-based Nextcloud environment. Prerequisites include access to the login page. The outcome confirms the leak pattern without revealing real users.

## Requirements

1. Access to the login page from the previous procedure
2. A list of common or random usernames to test as non-existent
3. Web browser

## Defense

Defensive measures and detection strategies:

- Standardize error messages to 'Invalid credentials' for all failures
- Enable rate limiting on login attempts to prevent enumeration
- Monitor logs for repeated failed logins with varied usernames

## Objectives

1. Observe the error for invalid usernames
2. Baseline the response for comparison
3. Avoid triggering account lockouts on real users

## Instructions

### Step 1: Submit Non-Existent Credentials

**Context**: Enter and submit a test username that does not exist to capture the specific error.

No command required; perform manually.

In the login form, input username 'charlietango' and password 'charlietango', then submit.

> Expected: 'Invalid Username' error. This indicates the system distinguishes non-existent users without referencing the input.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[username-enumeration]]
- [[information-disclosure]]
