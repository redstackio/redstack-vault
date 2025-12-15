---
id: proc-001
tags:
  - authentication
  - nextcloud
  - login
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-nextcloud-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:12.106Z'
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
# Authenticate-to-Nextcloud-Instance

## Summary

This procedure establishes authenticated access to a Nextcloud instance, enabling subsequent API queries. It simulates user login via the web installer or direct HTTP authentication, required for accessing protected OCS endpoints.

## Description

In the context of exploiting the Nextcloud path disclosure vulnerability, authentication is necessary as the `/ocs/v1.php/cloud/user` endpoint requires a valid session. This can be done via the web interface post-installation or programmatically using HTTP clients. The target is a fresh or existing Nextcloud installation running on a PHP web server. Expected outcome is a valid session cookie or basic auth token for API calls.

## Requirements

1. Network access to the Nextcloud login endpoint (typically HTTPS port 443)
2. Valid username and password (e.g., admin account created during installation)
3. HTTP client like curl or a web browser

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for all users
- Monitor login attempts and API access logs for anomalous patterns
- Use web application firewalls (WAF) to rate-limit authentication requests

## Objectives

1. Obtain a valid session for authenticated API access
2. Verify user privileges on the instance
3. Prepare for reconnaissance queries without triggering alerts

## Instructions

### Step 1: Access Login Interface

**Context**: Navigate to the Nextcloud login page to initiate authentication.

**Command** ([[commands/curl-nextcloud-login]]):
```bash
curl -c cookies.txt -d "user=admin&password=adminpass" https://nextcloud.example.com/login
```

> This command sends a POST request to the login endpoint, saving the session cookie to `cookies.txt`. Expected output is a redirect (HTTP 302) to the dashboard if successful.

### Step 2: Verify Authentication

**Context**: Confirm the session is active by accessing a protected resource.

**Command** ([[commands/curl-nextcloud-dashboard]]):
```bash
curl -b cookies.txt https://nextcloud.example.com/index.php/apps/files/
```

> This retrieves the dashboard or files app page. Expected output is HTML content indicating successful login, such as user menu elements.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-nextcloud-login]]
- [[commands/curl-nextcloud-dashboard]]

## Tools Used


## Tags

- [[authentication]]
- [[nextcloud]]
- [[login]]
