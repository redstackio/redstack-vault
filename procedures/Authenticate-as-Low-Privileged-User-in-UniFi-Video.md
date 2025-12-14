---
id: proc-auth-low-priv-unifi-329659
tags:
  - authentication
  - initial-access
  - unifi-video
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:09.724Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Low-Privileged-User-in-UniFi-Video

## Summary

This procedure establishes a session in the UniFi Video web interface using low-privileged credentials from PUBLIC_GROUP or CUSTOM_GROUP, setting the stage for exploiting privilege check vulnerabilities without requiring admin access.

## Description

In the UniFi Video environment, low-privileged users can log in to the web interface (typically hosted on Windows servers) to access basic features. This procedure uses valid but limited credentials to authenticate, obtaining a session that can be used to probe and exploit endpoints lacking proper authorization. The target is the UniFi Video Server's web UI, and success results in a valid session cookie for further requests. Prerequisites include knowing or obtaining low-priv credentials, such as through social engineering or default accounts.

## Requirements

1. Valid low-privileged credentials (username/password for PUBLIC_GROUP or CUSTOM_GROUP)
2. Network access to the UniFi Video web interface (e.g., https://target:7443)
3. Web browser or HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for all users
- Monitor login attempts from unusual IPs or with low-priv accounts followed by config changes
- Use web application firewalls (WAF) to log anomalous session usage

## Objectives

1. Establish an authenticated session as a non-admin user
2. Obtain session tokens for endpoint access
3. Prepare for privilege escalation without alerting defenses

## Instructions

### Step 1: Prepare Login Request

**Context**: Identify the login endpoint, typically /login or similar in the UniFi Video web interface.

Navigate to the login page in a browser or prepare a curl command to submit credentials.

### Step 2: Submit Credentials

**Context**: Authenticate using low-priv credentials to gain a session.

Use a browser to enter username and password, or execute an HTTP POST with curl:

```bash
curl -X POST -d "username=lowpriv_user&password=lowpriv_pass" https://target-unifi-video/login -c cookies.txt
```

> This command sends credentials and saves the session cookie to cookies.txt. Expected output: HTTP 302 redirect or success message indicating login.

### Step 3: Verify Session

**Context**: Confirm access to basic features without admin privileges.

Send a GET request to a dashboard endpoint using the session cookie:

```bash
curl -X GET -b cookies.txt https://target-unifi-video/dashboard
```

> Expected output: HTML or JSON response showing limited user interface, confirming low-priv access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[initial-access]]
- [[unifi-video]]
