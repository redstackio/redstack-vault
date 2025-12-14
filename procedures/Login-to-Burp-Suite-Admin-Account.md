---
id: proc-burp-admin-login-001
tags:
  - authentication
  - admin-access
  - session-establishment
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.137Z'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Burp-Suite-Admin-Account

## Summary

This procedure establishes an authenticated admin session in Burp Suite Enterprise using valid credentials, simulating an initial compromise that sets the stage for session persistence exploitation.

## Description

In the context of testing session management flaws, this procedure involves accessing the Burp Suite Enterprise web interface and logging in with admin credentials. It creates an active browser session that can later be tested for persistence after password changes. The target environment is a Java-based web application hosting the admin console. Prerequisites include knowledge of admin credentials, obtained via prior compromise such as phishing or credential stuffing.

## Requirements

1. Valid admin username and password for Burp Suite Enterprise
2. Web browser with no existing sessions for the target
3. Network access to the Burp Suite Enterprise web interface (typically on port 8080 or configured port)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin logins to prevent credential-based compromises
- Monitor login events for anomalous IP addresses or unusual times
- Use session timeout policies to limit session duration

## Objectives

1. Gain initial access to the admin console
2. Establish a session token or cookie for persistence testing
3. Verify admin privileges are active

## Instructions

### Step 1: Navigate to Admin Dashboard

**Context**: Open the web browser and access the Burp Suite Enterprise login page to begin authentication.

No specific command; use browser navigation to the admin URL (e.g., http://burp-enterprise:8080/admin).

> Enter the admin username and password in the login form. Upon success, the dashboard should load, confirming session establishment.

### Step 2: Confirm Session Validity

**Context**: Perform a simple admin action to ensure the session is fully authenticated.

No specific command; attempt to view the user management section or run a basic query in the console.

> Successful execution shows admin features accessible without re-authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- admin-access
