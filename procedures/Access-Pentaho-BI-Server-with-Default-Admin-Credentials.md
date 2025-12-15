---
tags:
  - default-credentials
  - auth-bypass
  - pentaho
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
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:23:54.333Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 58b3dc76-11a7-43c9-b3e8-1753fe23dcc9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
---
# Access-Pentaho-BI-Server-with-Default-Admin-Credentials

## Summary

This procedure exploits unchanged default credentials in Pentaho BI Server to gain unauthorized administrative access, allowing full control over server functions including report management.

## Description

Pentaho BI Server, when exposed publicly without credential changes, permits login with the default admin/password combination. This grants access to the web interface at https://target:8888/pentaho, enabling subsequent exploitation like report uploads. The attack targets reconnaissance-identified instances and assumes no additional authentication layers.

## Requirements

1. Network access to the target server on port 8888
2. Web browser or HTTP client for authentication
3. Knowledge of default credentials (admin/password)

## Defense

Defensive measures and detection strategies:

- Change default credentials immediately upon deployment
- Implement multi-factor authentication (MFA) on login endpoints
- Monitor login attempts for failures or suspicious IP origins
- Use web application firewalls (WAF) to block default credential usage

## Objectives

1. Authenticate to the Pentaho BI Server dashboard
2. Obtain administrative privileges for report handling
3. Enable further exploitation like malicious uploads

## Instructions

### Step 1: Navigate to Login Endpoint

**Context**: Locate and access the Pentaho login page to attempt authentication.

Open a web browser and navigate to https://target:8888/pentaho. The login form will appear.

### Step 2: Authenticate with Defaults

**Context**: Submit the default credentials to bypass authentication.

Enter username: admin and password: password in the login form and submit.

> Upon success, the dashboard loads, confirming access. Failure indicates credentials may have been changed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Default Accounts]] Default Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[default-credentials]]
- [[auth-bypass]]
- [[pentaho]]
