---
id: proc-wordpress-auth-subscriber
tags:
  - wordpress
  - authentication
  - initial-access
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/wordpress-login-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:12.314Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-WordPress-Subscriber

## Summary

This procedure authenticates a subscriber user to a WordPress instance, obtaining session cookies for subsequent authenticated requests to admin endpoints.

## Description

In the context of exploiting vulnerabilities in WordPress Core Ajax handlers, initial authentication as a low-privilege subscriber is required. This step uses curl to POST login credentials to wp-login.php, storing cookies in a jar file for reuse. It targets outdated versions like 4.5.3 where subscribers can access certain admin-ajax actions. Prerequisites include known subscriber credentials and direct access to the login endpoint.

## Requirements

1. Valid subscriber credentials (e.g., username: subscriber, password: password)
2. Network access to $target/wp-login.php
3. curl installed on the attacker's system

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and multi-factor authentication for all users
- Monitor login attempts for unusual patterns or failures
- Use web application firewalls (WAF) to detect anomalous POST requests to login endpoints

## Objectives

1. Establish an authenticated session as a subscriber
2. Obtain session cookies for Ajax endpoint access
3. Enable exploitation of authenticated vulnerabilities

## Instructions

### Step 1: Prepare Cookie Jar

**Context**: Create a temporary file to store session cookies using mktemp (assumed in script context).

Set variables: $target (WordPress URL), $username=subscriber, $password=password, $cookiejar=$(mktemp).

### Step 2: Execute Login

**Context**: Send POST request to authenticate and capture cookies.

**Command** ([[commands/wordpress-login-curl]]):
```bash
curl --cookie-jar "$cookiejar" --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" "$target/wp-login.php" >/dev/null 2>&1
```

> This command submits credentials via POST, suppresses output, and saves cookies to $cookiejar. Expected output is a successful redirect or 302 response indicating login success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/wordpress-login-curl]]

## Tools Used

- [[tools/curl]]

## Tags

- wordpress
- authentication
