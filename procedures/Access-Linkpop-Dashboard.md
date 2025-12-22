---
id: proc-linkpop-access-001
tags:
  - authentication
  - web-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:44.436Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Access-Linkpop-Dashboard

## Summary

This procedure outlines logging into the Linkpop dashboard to gain access for template creation, serving as the initial entry point for exploiting stored XSS vulnerabilities.

## Description

In the context of attacking Linkpop's Shopify-integrated platform, authenticated access to the admin dashboard is required to create templates where XSS payloads can be injected. This step assumes possession of valid credentials and focuses on navigating to the vulnerable interface at https://linkpop.com/dashboard/admin. Expected outcomes include a fully loaded dashboard ready for further actions like template manipulation.

## Requirements

1. Valid Linkpop account credentials (email and password)
2. Web browser with internet access
3. No proxy interference unless intentionally set up

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for dashboard logins
- Monitor login attempts from unusual IP addresses or locations
- Use web application firewalls (WAF) to detect anomalous access patterns

## Objectives

1. Establish authenticated session in the Linkpop dashboard
2. Verify access to template creation features
3. Prepare for payload injection without alerting defenses

## Instructions

### Step 1: Navigate to Login Page

**Context**: Reach the authentication endpoint to begin the login process.

Open a web browser and visit https://www.linkpop.com/.

> This loads the main site; look for the login option to proceed.

### Step 2: Authenticate

**Context**: Submit credentials to gain dashboard access.

Enter valid email and password, then submit the login form to redirect to https://linkpop.com/dashboard/admin.

> Successful login results in a dashboard view with options for creating pages or templates.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- web-access
