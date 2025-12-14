---
id: proc-uuid-2
tags:
  - brute-force
  - authentication
  - wordpress
type: procedure
tools:
  - '[[tools/Wfuzz]]'
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/wfuzz-brute-force-wp-admin]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:28:59.229Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Spraying]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-WordPress-Admin-Credentials

## Summary

This procedure demonstrates brute forcing WordPress admin credentials by exploiting the lack of rate limiting or account lockouts on the wp-admin authorization form, using tools like Wfuzz to rapidly test password wordlists and gain full administrative access.

## Description

WordPress sites without protections on /wp-admin allow attackers to perform unlimited login attempts, often via Basic Authentication. This procedure targets the 'admin' user with common passwords, sending requests at high speed. In the scenario, tools like Wfuzz or Burp Intruder fuzz the password field, potentially compromising the site in seconds to minutes. Prerequisites include tool installation and a wordlist like SecLists' 10k common passwords.

## Requirements

1. Installed fuzzing tool (Wfuzz or Burp Suite)
2. Password wordlist (e.g., /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt)
3. Target URL accessible (e.g., https://target.com/wp-admin)
4. Knowledge of default username (often 'admin')

## Defense

Defensive measures and detection strategies:

- Deploy rate limiting (e.g., via .htaccess or plugins like Limit Login Attempts)
- Use strong, unique passwords and enable account lockout after 5 failed attempts
- Log and alert on anomalous login traffic using tools like Fail2Ban
- Monitor for tools like Wfuzz via user-agent or request patterns

## Objectives

1. Test thousands of passwords without triggering defenses
2. Identify valid credentials for admin access
3. Achieve unauthorized entry to the WordPress backend for further exploitation

## Instructions

### Step 1: Prepare Wordlist and Target

**Context**: Ensure the wordlist is available and configure the target URL with the known username.

**Instructions**: Download or verify the SecLists wordlist path.

### Step 2: Execute Brute Force with Wfuzz

**Context**: Use Wfuzz to fuzz the Basic Auth password field, replacing FUZZ with wordlist entries.

**Command** ([[commands/wfuzz-brute-force-wp-admin]]):
```bash
wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -u https://my.stripo.email/wp-admin -d "Authorization: Basic admin:FUZZ"
```

> This command enables colored output (-c), uses the wordlist (-w), targets the URL (-u), and injects FUZZ into the Basic Auth header (-d). Expected output shows request counts, response codes, and times; success indicated by a 200 response or dashboard redirect instead of 401.

### Step 3: Validate with Burp Intruder

**Context**: For more control, capture a login request in Burp and use Intruder to automate fuzzing.

**Instructions**: Intercept a request to wp-admin, mark the password as §payload§, load the wordlist, and start the attack. Analyze positions for response length changes signaling success.

**Expected Output**: Table of attempts with varying response sizes; shorter or different responses indicate valid credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques

- [[Password Spraying]]

## Commands Used

- [[commands/wfuzz-brute-force-wp-admin]]

## Tools Used

- [[tools/Wfuzz]]
- [[tools/Burp-Intruder]]

## Tags

- [[brute-force]]
- [[authentication]]
- [[wordpress]]
