---
tags:
  - wordpress
  - api
  - discovery
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:29:20.450Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2538589b-6801-4f20-9dc6-6ce1e4b679cb
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Active Scanning]]'
---
# Identify-WordPress-REST-API-Endpoint-Exposing-Users

## Summary

This procedure involves accessing the WordPress REST API users endpoint to check for unauthenticated exposure of sensitive user information, such as admin usernames, which can aid in reconnaissance for further attacks.

## Description

In WordPress installations, the REST API endpoint /wp-json/wp/v2/users/ may be accessible without authentication, returning JSON data with usernames. This is a common misconfiguration that allows attackers to enumerate admin accounts. The procedure targets public-facing WordPress sites and requires no special privileges, making it an effective initial reconnaissance step. Expected outcomes include a list of users, highlighting potential high-privilege accounts for targeting.

## Requirements

1. Public access to the target WordPress site
2. Browser or command-line tool like curl for HTTP requests
3. Knowledge of WordPress URL structure (e.g., /wp-json/wp/v2/users/)

## Defense

Defensive measures and detection strategies:

- Restrict REST API access to authenticated users via plugins like Disable REST API
- Monitor access logs for repeated requests to /wp-json/wp/v2/users/
- Implement rate limiting on API endpoints

## Objectives

1. Enumerate admin and user accounts without authentication
2. Identify potential targets for credential attacks
3. Gather intelligence on site structure

## Instructions

### Step 1: Access the Endpoint

**Context**: Directly query the WordPress REST API to retrieve user data and confirm exposure.

**Command** (Manual browser access or curl):

Use a browser to visit the endpoint or execute a simple GET request.

```bash
curl https://example.com/wp-json/wp/v2/users/
```

> This command fetches the JSON response. If successful, it returns user objects with fields like 'slug' containing usernames. Look for admin-like names (e.g., 'admin', 'administrator').

### Step 2: Parse and Analyze Response

**Context**: Review the JSON output to extract usernames and assess sensitivity.

No specific command; use JSON parsing tools or browser console.

> Expected: Array of users, e.g., {"id":1,"slug":"admin"}. Success if data is returned without login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery
- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[api]]
- [[Discovery]]
