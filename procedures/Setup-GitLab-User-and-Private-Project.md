---
id: proc-uuid-1
tags:
  - gitlab
  - setup
  - user-creation
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
updated_at: '2025-12-14T17:32:29.257Z'
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
# Setup-GitLab-User-and-Private-Project

## Summary

This procedure establishes a test environment in GitLab by creating a user account and a private project, providing the foundation for demonstrating access control bypass.

## Description

In a self-hosted GitLab instance (e.g., version 14.1.0), create a regular user account and log in to generate a private project. This simulates a legitimate user setup before exploiting the password expiration flaw. The project ID is crucial for later API testing. No special privileges are needed beyond standard user access.

## Requirements

1. Access to GitLab web interface at https://gitlab.domain.com
2. Valid email for user registration
3. Browser for navigation

## Defense

Defensive measures and detection strategies:

- Monitor user registrations via GitLab audit logs
- Enforce strong password policies during setup
- Use role-based access to limit project creation

## Objectives

1. Create and verify a test user account
2. Establish a private project as the access target
3. Record project ID for exploitation

## Instructions

### Step 1: Create and Log In as User

**Context**: Register a new user to simulate a legitimate account.

Navigate to https://gitlab.domain.com/users/sign_up and create user 'user01' with a password. Log in successfully.

> Successful login redirects to the dashboard, confirming access.

### Step 2: Create Private Project

**Context**: Set up a private repository to test unauthorized access.

Go to https://gitlab.domain.com/projects/new#blank_project, name the project (e.g., 'test-private'), set visibility to Private, and create it. Note the project ID from the URL (e.g., /projects/123).

> Project creation succeeds, and ID is visible in the browser address bar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- user-setup
- project-creation
