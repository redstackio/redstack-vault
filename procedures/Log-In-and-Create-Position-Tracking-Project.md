---
id: proc-semrush-login-project
tags:
  - authentication
  - initial-access
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
updated_at: '2025-12-13T23:52:39.487Z'
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
# Log-In-and-Create-Position-Tracking-Project

## Summary

This procedure establishes authenticated access to the SEMrush platform and sets up a new Position Tracking project, serving as the entry point for exploiting vulnerabilities in the tracking features.

## Description

In the context of testing SEMrush for stored XSS, logging in with valid credentials is required to access protected sections like Position Tracking. Creating a project simulates legitimate usage while positioning the attacker to reach injectable fields. This step assumes the target is the SEMrush web application and requires no prior network compromise, only account credentials. Expected outcomes include a persistent session for follow-on actions.

## Requirements

1. Valid SEMrush account credentials (email and password)
2. Web browser (e.g., Chrome or Firefox)
3. Network access to semrush.com over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized logins
- Monitor login attempts for anomalies, such as unusual IP addresses or failed authentications
- Use session timeouts and IP binding to limit session persistence

## Objectives

1. Achieve authenticated access to the SEMrush dashboard
2. Create a new Position Tracking project to enable access to vulnerable interfaces
3. Establish a session for injecting payloads in subsequent steps

## Instructions

### Step 1: Access and Authenticate

**Context**: Navigate to the login page and enter credentials to start a session.

No specific command; use the web interface:

- Open a browser and go to https://www.semrush.com
- Click 'Log In' and enter your email and password
- Submit the form to authenticate

> Successful login redirects to the dashboard, showing account details and project options.

### Step 2: Initiate Project Creation

**Context**: From the dashboard, set up a new project targeting the Position Tracking module.

No specific command; use the UI:

- On the dashboard, select 'Position Tracking' from the tools menu
- Click 'Create Project' or 'New Project'
- Configure basic settings (e.g., target domain, location) and save

> Project creation confirmation appears, with the project listed for further configuration.

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
- web-access
