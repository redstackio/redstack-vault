---
id: proc-auth-searchgov
tags:
  - authentication
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Fiddler]]'
  - '[[tools/ZAP]]'
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
updated_at: '2025-12-14T03:53:38.679Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Access-Help-Docs-Endpoint

## Summary

This procedure outlines logging into Search.gov and navigating to the vulnerable /help_docs endpoint in the help manual, establishing an authenticated session for subsequent SSRF exploitation.

## Description

The attack begins with authentication to Search.gov using valid credentials, followed by navigation to the help manual section. This exposes the /help_docs endpoint, which fetches external documentation but is vulnerable to SSRF via the 'url' parameter. Prerequisites include a registered account; the procedure assumes external network access and uses proxy tools for request inspection.

## Requirements

1. Valid Search.gov login credentials
2. Proxy tool configured (e.g., Burp Suite) to intercept traffic
3. Browser or curl for initial navigation

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for accounts
- Monitor login attempts and session creations for anomalies
- Use web application firewalls (WAF) to detect unusual navigation patterns

## Objectives

1. Establish authenticated session with necessary cookies
2. Reach the /help_docs endpoint without triggering alerts
3. Prepare for parameter manipulation in subsequent steps

## Instructions

### Step 1: Login to Search.gov

**Context**: Create an authenticated session by logging in with credentials.

No specific command; use browser to visit https://search.usa.gov and log in, capturing cookies via proxy.

> Expected: Redirect to dashboard with session cookies like _session_id and user_credentials.

### Step 2: Navigate to Help Manual

**Context**: Access the help section to load the /help_docs endpoint.

Click 'Help Manual' or equivalent link; intercept the initial request in proxy.

> Expected: Page loads with /help_docs calls visible in proxy history.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]
- [[tools/ZAP]]

## Tags

- authentication
- web
