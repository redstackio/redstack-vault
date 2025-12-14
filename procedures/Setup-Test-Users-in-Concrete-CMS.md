---
tags:
  - user-setup
  - concrete-cms
  - admin-access
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:20.391Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b00362a5-2ca2-4920-aa0a-3e7945f4e11e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-Test-Users-in-Concrete-CMS

## Summary

This procedure sets up a test environment in Concrete CMS by creating admin-logged sessions and a secondary user account to simulate multi-user interactions for vulnerability testing, such as XSS exploitation.

## Description

In the context of testing stored XSS in Concrete CMS 8.3.1, this procedure involves logging in as an administrator, creating a new user with admin privileges, and establishing a separate private browsing session. This allows isolation of user contexts to demonstrate cross-user impact without interfering with the primary admin session. The target is a web-based CMS instance running on PHP, requiring direct network access and valid credentials.

## Requirements

1. Access to Concrete CMS 8.3.1 instance via web browser
2. Valid administrator credentials
3. Modern web browser supporting incognito/private mode (e.g., Firefox or Chrome)

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin accounts to limit unauthorized user creation
- Monitor admin dashboard logs for unusual user creation events
- Use web application firewalls (WAF) to detect anomalous login patterns

## Objectives

1. Establish isolated admin and test user sessions
2. Grant test user admin privileges for calendar access
3. Prepare for payload injection without session crossover

## Instructions

### Step 1: Admin Login

**Context**: Authenticate to the CMS as administrator to gain access to user management features.

In [[tools/Firefox]] or [[tools/Chrome]], navigate to the Concrete CMS login page and enter admin credentials.

**Expected Output**: Successful redirection to the dashboard.

### Step 2: Create Test User

**Context**: Add a new user account and assign it to the Administrators group to enable calendar feature access.

From the dashboard, go to user management, create a new account (e.g., username: user2, with a password), and add it to the Administrators group.

**Expected Output**: User created and visible in the user list with admin role.

### Step 3: Setup Separate Session

**Context**: Launch a private browsing window to log in as the test user, simulating a distinct user context.

Open an incognito/private window in the browser and log in using the test user's credentials.

**Expected Output**: Dashboard loads in the private session as user2.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- user-setup
- concrete-cms
