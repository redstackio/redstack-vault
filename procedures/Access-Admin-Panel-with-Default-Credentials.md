---
id: proc-001
tags:
  - default-credentials
  - initial-access
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Default Accounts]]'
updated_at: '2025-12-14T03:46:25.982Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
---
# Access-Admin-Panel-with-Default-Credentials

## Summary

This procedure involves accessing a defunct admin panel on a target subdomain using default credentials like admin/admin, providing an initial foothold for further reconnaissance and exploitation in web vulnerability assessments.

## Description

In scenarios where legacy or unmaintained web applications are present, default credentials often remain unchanged, allowing unauthorized access. This procedure targets such panels to inspect backend configurations and identify linked vulnerabilities like SQL injection. The attack scenario assumes public exposure of the admin URL, common in government or enterprise subdomains. Expected outcomes include dashboard access, revealing PHP-based structures and potential database connections.

## Requirements

1. Publicly accessible subdomain (e.g., admin.target.gov)
2. Web browser or HTTP client for authentication
3. Knowledge of common default credentials (admin/admin)

## Defense

Defensive measures and detection strategies:

- Enforce credential rotation and removal of default accounts
- Implement web application firewalls (WAF) to block default login attempts
- Monitor access logs for suspicious IP logins to admin paths

## Objectives

1. Gain unauthorized entry to admin interface
2. Identify application tech stack (e.g., PHP)
3. Set stage for vulnerability probing

## Instructions

### Step 1: Identify Admin Panel URL

**Context**: Locate the admin panel through subdomain enumeration or direct guessing (e.g., /admin).

No specific command; use browser to navigate to http://subdomain.target.gov/admin.

> Enter username: admin, password: admin. Successful login grants dashboard access.

### Step 2: Verify Access

**Context**: Confirm privileges and inspect for forms or endpoints.

Observe the loaded page for PHP references or login forms.

> Expected: Admin dashboard without errors, indicating vulnerability to further attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Default Accounts]] Valid Accounts: Default Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[default-credentials]]
- [[web-access]]
