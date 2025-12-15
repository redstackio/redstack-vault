---
id: proc-001
name: Initiate-OIDC-Login-Flow
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.582Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - oidc
  - nextcloud
commands:
  - '[[commands/curl-initiate-oidc]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Initiate-OIDC-Login-Flow

## Summary

This procedure starts the OpenID Connect (OIDC) authentication flow in Nextcloud, generating a CSRF state parameter stored in the session for subsequent verification.

## Description

In Nextcloud's OIDC integration, initiating the login redirects the user to an identity provider while storing a state parameter in the session to prevent CSRF attacks. This step sets up the session necessary for later exploitation of the state leak vulnerability in the callback handling.

## Requirements

1. Access to a Nextcloud instance with OIDC enabled
2. Network connectivity to the login endpoint
3. Tools like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Enable strict CSRF token validation without debug leaks
- Monitor for unusual login initiations from non-browser clients
- Use web application firewalls to block malformed OIDC requests

## Objectives

1. Establish a valid session with CSRF state
2. Prepare for callback exploitation
3. Simulate legitimate user initiation

## Instructions

### Step 1: Send Login Initiation Request

**Context**: Trigger the OIDC flow to create the session state.

**Command** ([[commands/curl-initiate-oidc]]):
```bash
curl -c cookies.txt -L "https://target.com/login?openIdConnect=1"
```

> This command follows redirects (-L) and saves session cookies (-c), initiating the flow and storing the state server-side.

### Step 2: Verify Session Establishment

**Context**: Check that cookies indicate an active session.

**Command** ([[commands/curl-initiate-oidc]]):
```bash
cat cookies.txt
```

> Expected output includes session cookies; no errors in the response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-initiate-oidc]]

## Tools Used


## Tags

- [[csrf]]
- [[oidc]]
- [[nextcloud]]
