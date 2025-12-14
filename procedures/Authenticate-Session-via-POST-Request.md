---
tags:
  - authentication
  - session-hijack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/authenticate-session-post]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3a18f54f-679b-4b50-acc9-6582583377d4
created_at: '2025-12-13T23:56:20.324Z'
updated_at: '2025-12-13T23:56:20.324Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate Session via POST Request

## Summary

This procedure authenticates a user session on uber.readme.io by sending a POST request with login credentials, upgrading the initial session cookie to an authenticated one for accessing restricted features like suggested edits.

## Description

Using the initial connect.sid cookie, a JSON payload with email, password, and action is sent to the /users/session endpoint. This grants authenticated access, enabling further exploitation such as payload injection. The procedure targets web applications with session-based authentication and assumes valid credentials are available.

## Requirements

1. Initial connect.sid cookie from prior access.
2. Valid email and password for the target system.
3. HTTP client like curl or Burp Suite for sending the request.

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA).
- Monitor login attempts and anomalous POST requests to session endpoints.

## Objectives

1. Obtain an authenticated session cookie.
2. Gain access to editing interfaces.
3. Prepare for payload injection.

## Instructions

### Step 1: Prepare and Send Authentication Request

**Context**: Authenticate using the provided credentials and cookie.

**Command** ([[commands/authenticate-session-post]]):
```bash
POST /users/session HTTP/1.1
Host: uber.readme.io
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Content-Length: 84
Cookie: YOUR CONNECT.SID COOKIE HERE
Connection: close
Pragma: no-cache
Cache-Control: no-cache

{"email":"readme2@thursday.eml.cc","password":"pjJnBODjkLFv!!11","action":"session"}
```

> This request authenticates the session and returns user details with a new cookie.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/authenticate-session-post]]

## Tools Used



## Tags

- authentication
- session-hijack
