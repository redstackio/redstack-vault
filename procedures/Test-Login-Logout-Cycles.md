---
id: proc-uuid-1
name: Test-Login-Logout-Cycles
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.840Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - authentication
  - web-testing
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Test-Login-Logout-Cycles

## Summary

This procedure simulates repeated login and logout actions on a web application to test how authentication state changes affect security tokens like CSRF tokens.

## Description

In the context of testing web applications like Liberapay, this procedure involves cycling through authentication states multiple times to observe token handling. The target environment is a web app with login/logout functionality, typically over HTTPS. Expected outcomes include successful state transitions, but it sets up for identifying flaws like token persistence. Prerequisites include valid credentials and browser access.

## Requirements

1. Valid username and password for the target web application
2. Browser with developer tools or a tool like curl for HTTP requests
3. Direct network access to the application's login endpoint

## Defense

Defensive measures and detection strategies:

- Implement token regeneration on every authentication event
- Monitor for unusual login/logout patterns via logging
- Use short-lived session tokens with automatic invalidation

## Objectives

1. Verify proper session management during auth cycles
2. Identify if tokens are invalidated post-logout
3. Prepare for token inspection in subsequent steps

## Instructions

### Step 1: Initial Login

**Context**: Authenticate to the application to establish a baseline session.

Navigate to the login page (e.g., https://liberapay.com/login) and submit credentials using the browser form or curl equivalent:

```bash
curl -X POST https://liberapay.com/login -d "username=user&password=pass" -c cookies.txt
```

> This command sends login credentials and saves session cookies. Expected output: HTTP 200 or redirect to dashboard, with session established.

### Step 2: Perform Logout

**Context**: Deauthenticate to simulate session end and observe token behavior.

Submit the logout request:

```bash
curl -X POST https://liberapay.com/logout -b cookies.txt -c cookies.txt
```

> This invalidates the session. Expected output: HTTP 200 or redirect to login, cookies updated or cleared.

### Step 3: Repeat Cycles

**Context**: Cycle 3-5 times to test consistency.

Repeat Steps 1 and 2 multiple times, noting any patterns in responses.

**Expected Output**: Consistent success across cycles without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[authentication]]
- [[web-testing]]
