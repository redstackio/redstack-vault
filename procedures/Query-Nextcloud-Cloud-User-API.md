---
id: proc-002
tags:
  - api-query
  - nextcloud
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-nextcloud-user-endpoint]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.093Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Query-Nextcloud-Cloud-User-API

## Summary

This procedure sends a GET request to the Nextcloud OCS API's cloud/user endpoint to retrieve user data in JSON format, exposing sensitive details like the storage location path.

## Description

The vulnerability lies in the `/ocs/v1.php/cloud/user?format=json` endpoint, which returns user information including the unsanitized `storageLocation` field containing the full server path (e.g., `/home/bohwaz/www/tmp/nextcloud/data/bohwaz`). This requires authentication and targets Nextcloud instances on PHP web servers. The outcome is disclosure of internal filesystem paths for reconnaissance.

## Requirements

1. Authenticated session or basic auth credentials
2. Access to the OCS API endpoint (typically over HTTPS)
3. HTTP client supporting headers like OCS-APIRequest

## Defense

Defensive measures and detection strategies:

- Sanitize API responses to redact paths (e.g., via Nextcloud configuration or patches)
- Log and monitor OCS API calls for unusual user data queries
- Implement role-based access controls to limit endpoint visibility

## Objectives

1. Retrieve user data from the OCS API
2. Capture the response for path analysis
3. Identify server configuration details without direct filesystem access

## Instructions

### Step 1: Prepare Authentication

**Context**: Include session cookie or basic auth from prior login.

**Command** ([[commands/curl-nextcloud-user-endpoint]]):
```bash
curl -H "OCS-APIRequest: true" -u admin:adminpass https://nextcloud.example.com/ocs/v1.php/cloud/user?format=json
```

> This sends the GET request with basic auth. Expected output is a JSON object with user details if authenticated.

### Step 2: Handle Session-Based Auth

**Context**: If using cookies instead of basic auth, load from login step.

**Command** ([[commands/curl-nextcloud-user-endpoint]]):
```bash
curl -H "OCS-APIRequest: true" -b cookies.txt https://nextcloud.example.com/ocs/v1.php/cloud/user?format=json
```

> Alternative for cookie-based sessions. Expected output same as above, confirming API access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-nextcloud-user-endpoint]]

## Tools Used


## Tags

- [[api-query]]
- [[nextcloud]]
- [[information-disclosure]]
