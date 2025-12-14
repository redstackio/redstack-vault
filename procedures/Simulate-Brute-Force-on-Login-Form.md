---
id: proc-uuid-002
tags:
  - brute-force
  - credential-access
  - web-attack
type: procedure
tools:
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:27:03.590Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Simulate-Brute-Force-on-Login-Form

## Summary

This procedure simulates brute force attacks on a web login form lacking CSRF protection, using automated tools to send multiple credential combinations and test for validation weaknesses, though CSRF absence primarily aids in cross-site forgery rather than direct brute forcing.

## Description

Targeted at forms like Nextcloud's login.php, this involves capturing a legitimate POST request and replaying it with payload variations. While CSRF tokens do not prevent brute force (as they validate origin, not rate), their absence simplifies automated submissions from external tools. This tests overall form resilience in a PHP-based web environment, potentially revealing if other defenses like rate limiting are in place.

## Requirements

1. Proxy tool like Burp Suite with Intruder module
2. Captured login request from the target endpoint
3. Payload lists for usernames (e.g., emails) and passwords
4. Network access to the login URL

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting on login attempts per IP
- Implement CAPTCHA after failed logins
- Log and alert on high-volume POST requests to authentication endpoints
- Use account lockouts after multiple failures

## Objectives

1. Send multiple login attempts without CSRF interruptions
2. Observe response patterns for successful/failed authentications
3. Evaluate if form allows unrestricted external submissions

## Instructions

### Step 1: Capture Baseline Request

**Context**: Intercept a sample login POST using a proxy to establish the request format.

Configure Burp Suite proxy and submit a test login.

> The captured request will show POST /login.php with parameters like member_username=example@email.com&member_password=test, without CSRF headers.

### Step 2: Configure Brute Force Payloads

**Context**: Set up the Intruder to vary credentials while handling any dynamic elements.

In Burp Intruder, mark §username§ and §password§ positions, load payload sets (e.g., common emails and passwords), and use an extender like Custom Logger for token management if needed.

> Launch the attack; monitor for 200 OK responses indicating potential successes or 403/ rate limit errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Brute Force]]

### Sub-Techniques

- [[Password Guessing]]

## Commands Used


## Tools Used

- [[tools/Burp-Intruder]]

## Tags

- [[brute-force]]
- [[credential-attack]]
