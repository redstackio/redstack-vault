---
id: 2107da44-3e8d-44d4-8541-35cefbc7aecb
name: Authenticate-and-Capture-Email-Parameter
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.519Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - login
  - session
  - web
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Authenticate-and-Capture-Email-Parameter

## Summary

This procedure describes logging into the DoD web application with valid credentials to generate a session URL containing the vulnerable 'email' parameter, setting the stage for manipulation.

## Description

After registration, authentication involves submitting credentials at the login endpoint, resulting in a redirect URL that embeds the user's email as a parameter. This flaw allows later tampering without session validation. The procedure targets the web platform and requires a verified account. Outcomes include a captured URL ready for exploitation, revealing the application's reliance on client-side parameters.

## Requirements

1. Verified account from registration
2. Web browser or proxy like [[tools/Burp-Suite]]
3. Knowledge of login endpoint (https://██████/███)

## Defense

Defensive measures and detection strategies:

- Validate session tokens server-side instead of URL parameters
- Implement CSRF tokens on login forms
- Monitor login redirects for parameter tampering attempts

## Objectives

1. Establish an authenticated session
2. Capture the URL with the email parameter
3. Identify the parameter for subsequent manipulation

## Instructions

### Step 1: Access Login Form

**Context**: Navigate to the login page post-registration.

Manually go to https://██████/███.

> The login form appears, requesting email and password.

### Step 2: Submit Credentials

**Context**: Authenticate to generate the vulnerable URL.

Enter your email and password, then submit. Intercept with [[tools/Burp-Suite]] if needed to inspect the request/response.

> Successful login redirects to a URL like https://█████████/████?email=your-email@domain.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[login]]
- [[session]]
- [[web]]
