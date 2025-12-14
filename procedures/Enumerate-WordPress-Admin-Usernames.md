---
id: proc-uuid-2
name: Enumerate-WordPress-Admin-Usernames
tags:
  - username-enumeration
  - wordpress
  - discovery
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
updated_at: '2025-12-14T17:28:36.588Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1087.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-WordPress-Admin-Usernames

## Summary

This procedure exploits the WordPress lost password feature to enumerate valid admin usernames by differentiating error messages, enabling targeted brute force attacks.

## Description

WordPress's /wp-login.php?action=lostpassword endpoint reveals valid usernames through distinct responses: 'Wrong username' for invalid ones versus a message about sending a confirmation link for valid ones. This was used to identify 'frank' as an admin on Nextcloud's site. Additional scanning of WordPress metadata can aid discovery.

## Requirements

1. Access to the lost password endpoint
2. List of potential usernames (e.g., common ones like admin, frank)
3. Web browser or scripting tool for automation

## Defense

Defensive measures and detection strategies:

- Customize error messages to be uniform (e.g., always say 'Invalid request')
- Disable or secure the lost password feature
- Log and monitor requests to /wp-login.php?action=lostpassword

## Objectives

1. Identify valid admin usernames
2. Reduce brute force search space
3. Facilitate credential guessing

## Instructions

### Step 1: Access Lost Password Form

**Context**: Navigate to the lost password endpoint to begin testing.

Use a browser to visit https://target.com/wp-login.php?action=lostpassword.

> The form prompts for a username or email.

### Step 2: Test Usernames for Validity

**Context**: Submit usernames and analyze responses.

Enter a username like 'invaliduser'; expect 'Wrong username'. Then try 'frank'; expect 'Check your email for the confirmation link'.

> Repeat for a list of guesses. Valid usernames confirm the account exists without sending emails if mail is disabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- [[T1087.001]] Local Account

## Commands Used

-

## Tools Used

-

## Tags

- [[username-enumeration]]
- [[wordpress]]
- [[Discovery]]
