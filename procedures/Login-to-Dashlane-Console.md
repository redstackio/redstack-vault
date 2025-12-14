---
id: uuid-login-dashlane
tags:
  - authentication
  - initial-access
  - dashlane
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:59.269Z'
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
# Login-to-Dashlane-Console

## Summary

This procedure establishes an authenticated session in the Dashlane admin console, serving as the entry point for intercepting API traffic and exploiting vulnerabilities.

## Description

The Dashlane console at console.dashlane.com requires user authentication to access team management features. This step involves signing up or logging in to obtain a valid session, which is proxied through Burp Suite for subsequent request manipulation. It targets web-based SaaS environments like password managers where user consoles expose APIs.

## Requirements

1. Internet access to console.dashlane.com
2. Valid email for registration (business trial link: https://www.dashlane.com/business/trial)
3. Burp Suite configured as browser proxy (e.g., 127.0.0.1:8080)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for console logins
- Monitor for unusual login patterns from new IPs
- Use certificate pinning to prevent proxy interception

## Objectives

1. Obtain authenticated session for API access
2. Enable traffic proxying for request capture
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept browser traffic.

**Instructions**: Launch Burp, configure proxy listener on 8080, and set browser proxy settings accordingly. Install Burp CA certificate in browser.

### Step 2: Access and Authenticate

**Context**: Navigate to the console and log in.

**Instructions**: Open console.dashlane.com, click 'Sign up' or 'Log in', provide credentials, and complete any trial registration.

> Upon success, you will be redirected to the dashboard with session cookies set.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- web
