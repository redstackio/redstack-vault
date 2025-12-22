---
id: 123e4567-e89b-12d3-a456-426614174001
name: Access-Portainer-Web-Interface
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.879Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - portainer
  - web-access
  - authentication
commands:
  - '[[commands/curl-portainer-login]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Access-Portainer-Web-Interface

## Summary

This procedure outlines gaining access to the Portainer web management interface, a prerequisite for exploiting vulnerabilities like SSRF in Docker environments.

## Description

Portainer is a web-based UI for managing Docker environments. Accessing it involves navigating to the hosted instance (e.g., on data-07.uberinternal.com) and authenticating with credentials. This step sets up the session for subsequent manipulations, such as SSRF attacks, in scenarios where the interface is exposed or credentials are compromised.

## Requirements

1. Network access to the Portainer URL (e.g., https://data-07.uberinternal.com:9443)
2. Valid username and password for Portainer admin or user account
3. Browser or command-line tool like curl for API interactions

## Defense

Defensive measures and detection strategies:

- Enforce strong authentication with MFA for Portainer logins
- Monitor login attempts and failed authentications in access logs
- Restrict Portainer access to VPN or internal networks only

## Objectives

1. Establish a authenticated session in Portainer
2. Verify UI accessibility for endpoint management
3. Prepare for internal request manipulation

## Instructions

### Step 1: Verify Portainer Accessibility

**Context**: Confirm the Portainer instance is reachable and the login endpoint responds.

**Command** ([[commands/curl-portainer-login]]):
```bash
curl -X GET https://data-07.uberinternal.com:9443/api/status
```

> This command checks the status endpoint. Expected output: JSON with version info indicating the service is running.

### Step 2: Authenticate to Portainer

**Context**: Log in to obtain a JWT token for subsequent API calls.

**Command** ([[commands/curl-portainer-login]]):
```bash
curl -X POST https://data-07.uberinternal.com:9443/api/auth -H "Content-Type: application/json" -d '{"username":"admin","password":"yourpassword"}'
```

> This submits credentials. Expected output: JSON response with "jwt" field containing the auth token on success (HTTP 200).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-portainer-login]]

## Tools Used


## Tags

- portainer
- web-access
- authentication
