---
id: proc-wordpress-auth-subscriber
tags:
  - wordpress
  - authentication
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
updated_at: '2025-12-14T17:31:11.384Z'
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
# wordpress-authenticate-subscriber

## Summary

This procedure authenticates to a WordPress site as a low-privilege subscriber user, obtaining session cookies for subsequent authenticated requests to exploit vulnerabilities in Ajax handlers.

## Description

In the context of exploiting WordPress 4.5.3, this step logs in via the standard wp-login.php endpoint using curl to simulate a browser login. It captures cookies in a temporary jar file for reuse. This enables access to authenticated endpoints like admin-ajax.php without admin privileges, as subscribers can trigger the vulnerable update-plugin action. Prerequisites include valid subscriber credentials and network access to the login page.

## Requirements

1. Valid WordPress subscriber username and password
2. Target URL accessible via HTTP/HTTPS
3. curl installed on the attacker's system

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and multi-factor authentication for all users
- Monitor login attempts for anomalies (e.g., unusual IP or frequency)
- Use web application firewalls (WAF) to detect automated login probes

## Objectives

1. Establish authenticated session with minimal privileges
2. Capture session cookies for request chaining
3. Enable access to protected Ajax endpoints

## Instructions

### Step 1: Prepare Temporary Cookie Jar

**Context**: Create a temporary file to store session cookies securely.

**Command** ([[commands/wordpress-login-curl]]):
```bash
cookiejar=$(mktemp)
```

> This generates a unique temporary file path for the cookie jar.

### Step 2: Perform Login Request

**Context**: Send POST data to wp-login.php to authenticate and save cookies.

**Command** ([[commands/wordpress-login-curl]]):
```bash
curl --cookie-jar "$cookiejar" --data "log=$username&pwd=$password&wp-submit=Log+In&redirect_to=%2f&testcookie=1" "$target/wp-login.php" >/dev/null 2>&1
```

> Submits login form parameters; suppresses output. Successful login populates the cookie jar with session tokens.

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
