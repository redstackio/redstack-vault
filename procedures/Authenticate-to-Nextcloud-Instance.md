---
id: 00000000-0000-0000-0000-000000000002
name: Authenticate-to-Nextcloud-Instance
type: procedure
verified: false
submitted: true
created_at: '2023-12-14T00:00:00Z'
updated_at: '2025-12-14T04:08:48.777Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
tags:
  - authentication
  - nextcloud
platforms:
  - Web
tools: []
commands: []
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

# Authenticate-to-Nextcloud-Instance

## Summary

This procedure establishes an authenticated session to a Nextcloud instance using admin or privileged user credentials, enabling access to features like the Calendar app for subsequent exploitation.

## Description

In the context of SSRF exploitation, authentication is required as the vulnerability affects authenticated users who can interact with the Calendar and DAV apps. The process involves logging in via the web interface or API, obtaining a session that allows creating calendar events with malicious WebCal URLs. This step is prerequisite for triggering server-side jobs that perform the SSRF fetch.

## Requirements

1. Valid Nextcloud admin or privileged user credentials (username and password)
2. Network access to the Nextcloud web interface (e.g., http://target/nextcloud)
3. Web browser or API client (e.g., curl for testing)

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin accounts
- Monitor login attempts and failed authentications via Nextcloud logs
- Use IP whitelisting or VPN for admin access

## Objectives

1. Obtain a valid session token for authenticated API calls
2. Verify access to Calendar app features
3. Prepare for event creation without triggering alerts

## Instructions

### Step 1: Access Login Interface

**Context**: Navigate to the Nextcloud login page to initiate authentication.

**Command** (Manual Browser Access):

Open a web browser and visit the Nextcloud URL, e.g., `http://192.168.0.105/nextcloud`.

> Enter username (e.g., admin) and password. Upon success, the dashboard loads with calendar access.

### Step 2: Verify Authenticated Session

**Context**: Confirm the session allows Calendar interactions.

**Command** (API Test with curl):
```bash
curl -u admin:"[password]" -X GET "http://192.168.0.105/nextcloud/remote.php/dav/calendars/admin/"
```

> Returns 200 OK with calendar listings if authenticated successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- nextcloud
