---
tags:
  - default-credentials
  - auth-bypass
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.635Z'
sub_techniques:
  - '[[T1078.004]]'
id: f81a3e53-acc3-4990-98e3-cc77f96fdf46
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access Spring Boot Admin with Default Credentials

## Summary

This procedure exploits default or unchanged credentials on an exposed Spring Boot Admin instance to gain unauthorized administrative access, resulting in the disclosure of application metrics, logs, and configurations.

## Description

Spring Boot Admin often ships with default credentials like 'admin/admin' that, if not modified, allow easy entry. Attackers attempt these after discovering the instance, bypassing authentication to view sensitive data such as environment variables, health statuses, and audit logs. This is common in misconfigured cloud or on-premises deployments.

## Requirements

1. Discovered exposed Spring Boot Admin endpoint
2. Web browser or HTTP client for login attempts
3. List of common default credentials (e.g., admin/admin, user/password)

## Defense

Defensive measures and detection strategies:

- Enforce credential changes and multi-factor authentication
- Use role-based access control (RBAC) for admin interfaces
- Log and alert on failed/successful logins from unknown IPs

## Objectives

1. Authenticate using default credentials
2. Access administrative functions
3. Extract sensitive information from the interface

## Instructions

### Step 1: Attempt Login with Defaults

**Context**: Navigate to the login page and try common default credentials to bypass authentication.

Open the Spring Boot Admin login URL (e.g., http://target:8080/login) in a browser and enter username 'admin' and password 'admin'.

> If login succeeds, you are redirected to the dashboard; otherwise, try variants like 'user/user'.

### Step 2: Explore and Extract Data

**Context**: Once logged in, navigate the interface to view and capture sensitive details.

Browse sections like Applications, Logs, and Environment to collect metrics, configurations, and logs.

> Export or screenshot data for analysis; look for secrets in env vars or logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used


## Tools Used


## Tags

- [[default-credentials]]
- [[auth-bypass]]
- [[information-disclosure]]
