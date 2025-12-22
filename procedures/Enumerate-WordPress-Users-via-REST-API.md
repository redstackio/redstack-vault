---
tags:
  - information-disclosure
  - wordpress
  - api
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-wordpress-users-api]]'
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 42182a74-d660-440f-8eec-b5ce6aced28d
created_at: '2025-12-14T17:25:18.104Z'
updated_at: '2025-12-14T17:25:18.104Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-WordPress-Users-via-REST-API

## Summary

This procedure exploits the default WordPress REST API configuration to unauthenticatedly enumerate all users on a site, retrieving sensitive details like IDs, usernames, slugs, descriptions, and avatar URLs. It is commonly used in reconnaissance to map user accounts for subsequent attacks such as brute-force logins or personalized phishing.

## Description

WordPress sites from version 4.7 onward include a REST API accessible at /wp-json/, with the /wp/v2/users/ endpoint exposing user data by default unless explicitly disabled or protected (e.g., via plugins like Disable REST API). In the NordVPN case, endpoints like https://nordvpn.com/wp-json/wp/v2/users/ and https://nordvpn.com/?rest_route=/wp/v2/users/ returned full user lists in JSON format without checks. Attackers can use this to harvest data for targeted exploitation, as user slugs often match login usernames, aiding credential guessing.

## Requirements

1. Publicly accessible WordPress site with REST API enabled
2. HTTP client (e.g., curl, browser, or Postman)
3. Basic knowledge of JSON parsing for data extraction

## Defense

Defensive measures and detection strategies:

- Install plugins like 'Disable REST API' or 'WP REST API Authentication' to restrict endpoints
- Implement authentication via .htaccess or server rules to block unauthenticated /wp-json/ access
- Monitor access logs for repeated GET requests to /wp/v2/users/
- Use WAF rules to block enumeration patterns (e.g., high-volume API calls)

## Objectives

1. Gather user account details for reconnaissance
2. Identify high-value targets like administrators or employees
3. Enable follow-on attacks using exposed usernames and bios

## Instructions

### Step 1: Access the Primary REST API Endpoint

**Context**: Send a direct GET request to the standard WordPress users endpoint to fetch the user list.

**Command** ([[commands/curl-wordpress-users-api]]):
```bash
curl https://target.com/wp-json/wp/v2/users/
```

> This command retrieves a JSON array of all users. Successful output includes user objects with fields like id, name, slug, description, and avatar_urls. If paginated, follow ?page=2 parameters for more results.

### Step 2: Access via Query Parameter Alternative

**Context**: If the primary path is blocked, use the rest_route query parameter as a fallback to query the same endpoint.

**Command** ([[commands/curl-wordpress-users-api]]):
```bash
curl "https://target.com/?rest_route=/wp/v2/users/"
```

> This mirrors the primary endpoint's response. Use this if URL rewriting issues affect /wp-json/. Parse with jq for specific fields: curl ... | jq '.[].slug' to extract usernames.

### Step 3: Parse and Analyze Output

**Context**: Extract actionable data from the JSON response for further use.

**Command** ([[commands/curl-wordpress-users-api]]):
```bash
curl https://target.com/wp-json/wp/v2/users/ | jq -r '.[] | ["id:\(.id)", "name:\(.name)", "slug:\(.slug)" ] | join(" ")'
```

> Outputs formatted lines like "id:123 name:John Doe slug:john-doe". Save to file: > users.txt for offline analysis.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-wordpress-users-api]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[wordpress]]
- [[api]]
- [[enumeration]]
