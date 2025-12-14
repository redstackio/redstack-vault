---
tags:
  - initial-access
  - login
  - acronis
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
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
updated_at: '2025-12-13T23:56:03.491Z'
sub_techniques: []
id: 22a9a03f-1490-4f58-90c7-cd7f8aaa4276
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Acronis Cloud Console

## Summary

This procedure outlines logging into the Acronis cloud console to gain access to the vulnerable backup scanning features, serving as the initial access point for XSS exploitation.

## Description

In the context of exploiting a stored XSS vulnerability, authenticated access to the Acronis cloud console is required. The procedure involves navigating to the console URL and using valid credentials to authenticate, allowing subsequent navigation to the plans section. Expected outcomes include full UI access, enabling payload injection without additional privileges.

## Requirements

1. Valid Acronis account credentials
2. Web browser like Mozilla Firefox
3. Internet access to https://mc-beta-cloud.acronis.com/ui/

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for console logins
- Monitor login attempts from unusual IPs
- Use web application firewalls (WAF) to detect anomalous access patterns

## Objectives

1. Establish authenticated session in the console
2. Access the dashboard for further navigation
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Navigate to Console

**Context**: Open the browser and direct to the Acronis login page to initiate access.

No specific command; use browser navigation to https://mc-beta-cloud.acronis.com/ui/.

> Enter credentials in the login form and submit.

### Step 2: Authenticate

**Context**: Provide username and password to gain entry.

Submit the login form.

> Successful login redirects to the main UI dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- initial-access
- web-login
