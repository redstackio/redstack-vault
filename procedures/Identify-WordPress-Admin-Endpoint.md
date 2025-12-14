---
id: proc-uuid-1
name: Identify-WordPress-Admin-Endpoint
tags:
  - reconnaissance
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:36.591Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-WordPress-Admin-Endpoint

## Summary

This procedure involves locating the WordPress admin login endpoint on a target website and verifying the absence of rate-limiting, setting the stage for further exploitation.

## Description

In scenarios where a website uses WordPress, the admin panel is typically accessible at /wp-login.php. Attackers observe login behavior to confirm unlimited attempts are allowed, which is critical for brute force attacks. This was observed on sites like Nextcloud's WordPress instance, where no restrictions prevented repeated logins.

## Requirements

1. Web browser for manual access
2. Publicly accessible target URL
3. Basic knowledge of WordPress structure

## Defense

Defensive measures and detection strategies:

- Implement rate-limiting on login endpoints using plugins like Limit Login Attempts
- Monitor login attempt logs for anomalies
- Use CAPTCHA or two-factor authentication on admin panels

## Objectives

1. Confirm existence of admin login endpoint
2. Verify lack of protections against brute force
3. Prepare for username enumeration

## Instructions

### Step 1: Access the Login Endpoint

**Context**: Navigate to the standard WordPress admin URL to inspect the login form.

No specific command; use a browser to visit https://target.com/wp-login.php and submit a few invalid logins to test for rate limits.

> Attempt logins with dummy credentials multiple times. If no lockout occurs after 5-10 tries, rate-limiting is absent.

### Step 2: Observe Login Behavior

**Context**: Test for restrictions by simulating failed attempts.

Manually enter incorrect username/password pairs repeatedly.

> Successful observation: No CAPTCHA, IP bans, or delay messages appear, confirming exploitability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[Reconnaissance]]
- [[wordpress]]
