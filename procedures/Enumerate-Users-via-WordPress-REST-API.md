---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
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
  - '[[commands/curl-get-users]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:11.086Z'
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
# Enumerate Users via WordPress REST API

## Summary

This procedure exploits an information disclosure in the WordPress REST API to anonymously retrieve a list of all users who have authored published posts, including admin accounts. It targets vulnerable WordPress versions like 4.7 where authentication is not enforced on the /wp-json/wp/v2/users/ endpoint.

## Description

In vulnerable WordPress installations, the REST API exposes user enumeration without checks, allowing attackers to discover usernames and basic details. This is particularly dangerous for admin users, as it facilitates brute-force attacks or phishing. The procedure assumes public access to the site and uses simple HTTP GET requests. Expected outcomes include a JSON list of users, which can be parsed for usernames like 'admin'.

## Requirements

1. Publicly accessible WordPress site with REST API enabled
2. Vulnerable version (e.g., WordPress 4.7, unpatched)
3. Network access to the target URL (no VPN or credentials needed)

## Defense

Defensive measures and detection strategies:

- Update WordPress to 4.7.2 or later to disable unauthenticated user enumeration
- Disable REST API for users endpoint via plugins like Disable REST API
- Monitor access logs for repeated GET requests to /wp-json/wp/v2/users/
- Implement rate limiting on API endpoints

## Objectives

1. Discover all user accounts that have published content
2. Identify admin usernames for further attacks
3. Gather initial reconnaissance data without alerting defenses

## Instructions

### Step 1: Send GET Request to Users Endpoint

**Context**: This step queries the REST API to list users, exploiting the lack of authentication.

**Command** ([[commands/curl-get-users]]):
```bash
curl -s https://owncloud.com/wp-json/wp/v2/users/
```

> This command silently fetches the JSON response. Successful output is an array of user objects, e.g., [{"id":1,"name":"admin","slug":"admin",...}]. Parse with jq if needed: curl ... | jq '.[].name' to list usernames.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-users]]

## Tools Used


## Tags

- information-disclosure
- user-enumeration
- wordpress
- rest-api
