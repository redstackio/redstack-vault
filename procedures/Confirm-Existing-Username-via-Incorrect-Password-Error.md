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
updated_at: '2025-12-14T17:28:44.535Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: fb049d5a-4dfb-4401-9583-a793846337b1
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Confirm-Existing-Username-via-Incorrect-Password-Error

## Summary

This procedure validates a suspected existing username by submitting it with an incorrect password, observing a username-specific error message that confirms its presence.

## Description

Building on baseline testing, this targets known or guessed usernames (e.g., 'frank') in the Nextcloud login. The PHP backend returns a detailed error like 'The password you entered for username frank is incorrect', leaking existence. Performed manually in a browser on a web platform. Prerequisites: Prior access to login and baseline error knowledge. Outcome: Positive identification of valid accounts for escalation.

## Requirements

1. Baseline error from non-existent test
2. Suspected valid usernames (e.g., from common names or prior intel)
3. Continued access to the login form

## Defense

Defensive measures and detection strategies:

- Return uniform error messages without username inclusion
- Implement CAPTCHA after failed attempts
- Audit application logs for enumeration patterns and patch the disclosure

## Objectives

1. Confirm valid username existence
2. Differentiate from invalid errors
3. Gather intel for brute-force or reset attacks

## Instructions

### Step 1: Submit Existing Username with Wrong Password

**Context**: Test a potential real username to trigger the confirmatory error.

No command required; perform manually.

Enter username 'frank' and password 'charlietango', then submit the form.

> Expected: 'The password you entered for username frank is incorrect'. This echoes the username, proving it exists.

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
- [[nextcloud]]
