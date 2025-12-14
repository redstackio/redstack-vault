---
id: proc-omise-auth-001
tags:
  - authentication
  - web-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.242Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Authenticate to Omise Dashboard

## Summary

This procedure establishes authenticated access to the Omise dashboard, a prerequisite for accessing team management features vulnerable to race conditions.

## Description

In the context of exploiting web application vulnerabilities like race conditions in invitation systems, initial authentication is required to reach protected endpoints. This targets the Omise payment platform's dashboard at dashboard.omise.co, using standard login mechanisms. Expected outcomes include session establishment for subsequent request interception and manipulation.

## Requirements

1. Valid Omise account credentials with team invitation permissions
2. Web browser or proxy tool like Burp Suite for traffic control
3. Internet access to dashboard.omise.co on HTTPS port 443

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized logins
- Monitor login attempts for anomalies using web application firewalls (WAF)
- Log all authentication events for audit trails

## Objectives

1. Gain session access to the dashboard
2. Verify permissions for team features
3. Prepare for request interception

## Instructions

### Step 1: Navigate and Login

**Context**: Access the login page and submit credentials to establish a session.

No specific command; use browser:

Open https://dashboard.omise.co and enter username/password.

> Successful login redirects to the dashboard with session cookies set.

### Step 2: Verify Access

**Context**: Confirm ability to reach team invitation section.

Navigate to team settings.

> Dashboard loads without errors; team management visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- web-access
