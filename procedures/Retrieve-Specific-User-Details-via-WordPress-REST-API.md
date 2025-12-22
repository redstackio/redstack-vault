---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - information-disclosure
  - user-enumeration
  - wordpress
  - rest-api
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-get-user-id]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:11.085Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Retrieve Specific User Details via WordPress REST API

## Summary

This procedure fetches detailed information for a specific user ID via the WordPress REST API, building on user enumeration to expose admin bios, avatars, and links without authentication in vulnerable setups like WordPress 4.7.

## Description

After enumerating users, target a specific ID (e.g., 1 for admin) to retrieve richer data. The /wp-json/wp/v2/users/{id}/ endpoint leaks details like descriptions, which can aid social engineering. This assumes the prior step identified valid IDs and targets public sites.

## Requirements

1. Valid user ID from enumeration (e.g., admin ID 1)
2. Same vulnerable WordPress environment as enumeration
3. HTTP client like curl for GET requests

## Defense

Defensive measures and detection strategies:

- Patch to WordPress 4.7.2+ to restrict user detail access
- Use .htaccess to block /wp-json/wp/v2/users/* for unauthenticated requests
- Log and alert on anomalous API calls to user endpoints
- Enable WordPress authentication plugins for API

## Objectives

1. Obtain detailed profile data for targeted users
2. Enhance reconnaissance for admin accounts
3. Prepare for credential attacks using exposed info

## Instructions

### Step 1: Send GET Request to Specific User Endpoint

**Context**: This targets a known user ID to pull full details, confirming admin exposure.

**Command** ([[commands/curl-get-user-id]]):
```bash
curl -s https://owncloud.com/wp-json/wp/v2/users/1
```

> Outputs JSON with user specifics, e.g., {"id":1,"name":"Admin","description":"Site owner",...}. Use for verification; errors like 404 indicate invalid ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-user-id]]

## Tools Used


## Tags

- information-disclosure
- user-enumeration
- wordpress
- rest-api
