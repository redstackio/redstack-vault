---
id: proc-wpscan-bruteforce-login
tags:
  - wordpress
  - brute-force
  - credential-access
type: procedure
tools:
  - '[[tools/WPScan]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/wpscan-bruteforce-password]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:28:36.648Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-WordPress-Admin-Login-with-WPScan

## Summary

This procedure employs WPScan to brute force passwords against a known WordPress admin username (e.g., 'frank'), targeting the login form or XML-RPC endpoint to obtain unauthorized dashboard access.

## Description

Attackers use enumerated usernames to focus brute force efforts, reducing guess space. WPScan supports dictionary attacks with wordlists, optionally via XML-RPC for efficiency. Target environment: Exposed WordPress /wp-admin without strong protections. Outcomes: Cracked credentials if passwords are weak, leading to admin privileges.

## Requirements

1. Known valid username from prior enumeration
2. Password wordlist (e.g., rockyou.txt with common WP passwords)
3. WPScan with optional WPScan API key for detection avoidance

## Defense

Defensive measures and detection strategies:

- Enforce strong, unique passwords and multi-factor authentication (MFA)
- Disable XML-RPC if unused and implement login attempt locking
- Log and alert on repeated failed logins from WPScan-like requests

## Objectives

1. Gain initial admin access to WordPress
2. Test credential strength on exposed logins
3. Prepare for post-authentication exploitation

## Instructions

### Step 1: Prepare and Launch Brute Force

**Context**: Use the enumerated username and a wordlist to attempt logins systematically.

**Command** ([[commands/wpscan-bruteforce-password]]):
```bash
wpscan --url https://nextcloud.com -U frank -P /usr/share/wordlists/rockyou.txt --password-attack xmlrpc
```

> This runs a dictionary attack via XML-RPC, stopping on success. Output includes progress and successful creds, e.g., "Password found: weakpass". Monitor for lockouts.

### Step 2: Validate Login Success

**Context**: Test the cracked credentials manually to confirm access.

**Command** ([[commands/wpscan-bruteforce-password]]):
```bash
wpscan --url https://nextcloud.com --auth-type login --username frank --password weakpass
```

> If successful, WPScan confirms dashboard access. Expected: No errors, site info retrieved.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Spraying]] Password Spraying (adapted for targeted dict attack)

## Commands Used

- [[commands/wpscan-bruteforce-password]]

## Tools Used

- [[tools/WPScan]]

## Tags

- [[brute-force]]
- [[wordpress]]
- [[credential-access]]
