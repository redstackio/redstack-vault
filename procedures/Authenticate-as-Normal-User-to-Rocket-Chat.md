---
tags:
  - authentication
  - initial-access
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
  - '[[tools/Python3]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/python3-post-auth-nosqli-py]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:20.462Z'
sub_techniques: []
id: ee63b6f7-7d94-42c0-8d5f-94f33a5e21b8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Normal-User-to-Rocket-Chat

## Summary

This procedure establishes authenticated access to the Rocket.Chat API as a low-privilege user, enabling reach to vulnerable endpoints like users.list for subsequent exploitation.

## Description

In the context of exploiting post-authentication vulnerabilities in Rocket.Chat, authentication is required to access API endpoints. A non-admin user is created via the web interface, then used to authenticate in the exploit script, providing a session token for API calls. This step assumes no prior access and targets self-hosted instances.

## Requirements

1. Access to Rocket.Chat registration page (http://target:3000)
2. Valid username and password for a new user
3. Python environment with requests library

## Defense

- Enforce strong user registration validation and rate limiting
- Monitor for unusual API authentication patterns from new users

## Objectives

1. Obtain API authentication token
2. Confirm access to protected endpoints
3. Set up for injection exploitation

## Instructions

### Step 1: Create Non-Admin User

**Context**: Register a standard user account to gain initial access.

**Command** ([[commands/create-user-via-interface]]):
No direct command; use web UI to create user 'attacker' with password 'attacker'.

> Expected: User account created successfully.

### Step 2: Authenticate in Exploit Script

**Context**: Pass credentials to the script for API login.

**Command** ([[commands/python3-post-auth-nosqli-py]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> The script handles login, stores token, and proceeds to injection. Expected: Auth token in session, API calls succeed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/python3-post-auth-nosqli-py]]

## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- authentication
- rocket-chat
