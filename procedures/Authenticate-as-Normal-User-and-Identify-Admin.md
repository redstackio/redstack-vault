---
tags:
  - nosql-injection
  - account-discovery
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
  - '[[tools/post_auth_nosqli.py]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/install-python-dependencies]]'
  - '[[commands/python3-post-auth-nosqli]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:46:14.840Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 664bde18-20b4-42ea-95a3-c158df3be4cc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Authenticate-as-Normal-User-and-Identify-Admin

## Summary

This procedure authenticates a low-privilege user to the Rocket.Chat API and uses blind NoSQL injection to identify admin users by querying their roles.

## Description

In a post-authentication scenario, the users.list endpoint processes user-supplied JSON queries without sanitization, allowing MongoDB $where operators. This step leverages that to find users with 'admin' roles, extracting usernames and IDs for targeting. It requires valid user credentials and targets vulnerable Rocket.Chat instances like version 3.12.1. Outcomes include a list of admin identifiers for further exploitation.

## Requirements

1. Valid attacker account credentials in Rocket.Chat
2. Network access to the API endpoint (e.g., http://target:3000/api/v1/users.list)
3. Python3 with requests library installed
4. Target running a vulnerable version with MongoDB backend

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all query parameters in API endpoints, disallowing $where and similar operators
- Implement query allowlisting and input validation for MongoDB find() calls
- Monitor API logs for anomalous query patterns involving JavaScript operators
- Use web application firewalls (WAF) to block injection attempts

## Objectives

1. Establish authenticated session as a normal user
2. Discover admin accounts via injection
3. Prepare for targeted data leakage

## Instructions

### Step 1: Install Dependencies

**Context**: Set up the Python environment for API interactions and injection logic.

**Command** ([[commands/install-python-dependencies]]):
```bash
pip3 install requests bcrypt
```

> This installs the requests library for HTTP calls and bcrypt for potential hashing needs. Expected output: Successful installation messages for both packages.

### Step 2: Run Exploit Script for Authentication and Admin Query

**Context**: Authenticate and execute the initial NoSQL query {"$where":"this.roles.includes('admin')"} to list admins.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> The script handles login and sends the injection payload via POST to /api/v1/users.list. Expected output: Admin usernames and IDs printed, confirming discovery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/install-python-dependencies]]
- [[commands/python3-post-auth-nosqli]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/post_auth_nosqli.py]]

## Tags

- nosql-injection
- account-discovery
