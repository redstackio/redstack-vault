---
id: proc-wordpress-user-enum-001
tags:
  - user-enumeration
  - wordpress
  - api
  - access-control
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-wordpress-users-enum]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:11.044Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# User Enumeration via WordPress REST API

## Summary

This procedure exploits the default configuration of WordPress REST API, which exposes user information without authentication or access controls, allowing attackers to enumerate registered users, including usernames, emails, and IDs. It is commonly used in reconnaissance phases to map user accounts for subsequent attacks like credential stuffing or phishing.

## Description

WordPress sites, when installed with default settings, enable the REST API (wp-json/wp/v2) which includes an endpoint for users (/users). Without plugins like 'Disable REST API' or server-side hardening (e.g., .htaccess rules to block the endpoint), this allows unauthenticated access to user data. The attack targets public-facing WordPress installations, such as on jitsi.org, where the API was not restricted, leading to low-severity information disclosure. Prerequisites include identifying a WordPress site via headers, source code, or tools like Wappalyzer. Expected outcomes include a list of users that can aid in targeted exploitation.

## Requirements

1. Network access to the target WordPress site over HTTP/HTTPS
2. Basic knowledge of HTTP requests (no credentials required)
3. Optional: curl or similar HTTP client installed

## Defense

Defensive measures and detection strategies:

- Install and configure plugins like 'Disable REST API' or 'WP REST API Authentication' to restrict endpoints
- Add server-side rules (e.g., in .htaccess or nginx.conf) to block /wp-json/wp/v2/users for unauthenticated requests
- Monitor access logs for repeated GET requests to /wp-json/wp/v2/users and implement rate limiting
- Use WordPress security plugins like Wordfence to harden API access

## Objectives

1. Retrieve a list of registered user accounts and associated metadata
2. Identify administrative or high-privilege users for prioritization
3. Gather intelligence for follow-on attacks without alerting defenses

## Instructions

### Step 1: Query the Users Endpoint

**Context**: Send an unauthenticated GET request to the WordPress REST API users endpoint to fetch user data. This exploits the lack of default access controls in standard WordPress installations.

**Command** ([[commands/curl-wordpress-users-enum]]):
```bash
curl -s https://jitsi.org/wp-json/wp/v2/users
```

> This command performs a silent GET request to the /wp-json/wp/v2/users endpoint. If successful, it returns a JSON array of user objects. Parse the output with jq for readability (e.g., curl ... | jq '.[] | {name: .name, email: .email}'). Failure indicators include empty array (if restricted) or 401/403 errors.

### Step 2: Validate and Parse Response

**Context**: Review the response for user details and confirm enumeration success. This step ensures the data is usable for further reconnaissance.

**Command** ([[commands/curl-wordpress-users-enum]] with jq):
```bash
curl -s https://jitsi.org/wp-json/wp/v2/users | jq '.[].name'
```

> This pipes the output to jq to extract usernames. Expected output: a list of usernames. If no users are returned or an error occurs, the site may have API protections in place.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-wordpress-users-enum]]

## Tools Used


## Tags

- user-enumeration
- wordpress
- api
- access-control
