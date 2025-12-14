---
tags:
  - auth
  - login
  - uber
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
techniques: []
updated_at: '2025-12-14T17:31:10.993Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c3fac81b-118b-4970-9087-b1636cef548e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Log-in-to-Uber-as-Rider

## Summary

This procedure authenticates a user to the Uber web application as a rider, establishing a session necessary to access protected profile features like notification settings.

## Description

In the context of exploiting authentication weaknesses, logging in as a rider provides initial access to generate the vulnerable URL token. The target environment is the Uber web platform (uber.com), requiring valid credentials. Expected outcome is a fully authenticated session allowing navigation to internal pages.

## Requirements

1. Valid Uber rider account email and password
2. Web browser with internet access
3. No VPN or proxy restrictions blocking uber.com

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all logins
- Monitor for unusual login locations or devices
- Use session timeouts and IP binding

## Objectives

1. Establish authenticated session
2. Enable access to profile sections
3. Prepare for URL token extraction

## Instructions

### Step 1: Navigate to Login Page

**Context**: Reach the authentication endpoint to begin the process.

Open a web browser and go to https://www.uber.com/ or directly to the login URL.

> The login page should display fields for email/phone and password.

### Step 2: Enter Credentials

**Context**: Submit authentication details to create a session.

Fill in the email and password fields, then click "Log in".

> Upon success, the browser redirects to the rider dashboard, and session cookies are set.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth]]
- [[login]]
- [[uber]]
