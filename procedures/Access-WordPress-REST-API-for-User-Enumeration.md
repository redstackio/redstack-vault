---
tags:
  - wordpress
  - information-disclosure
  - user-enumeration
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1087.002]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: a734872d-2f59-4c4e-9ce4-43709899bc0f
created_at: '2025-12-14T17:28:44.968Z'
updated_at: '2025-12-14T17:28:44.968Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.002]]'
---
# Access-WordPress-REST-API-for-User-Enumeration

## Summary

This procedure exploits the default WordPress REST API configuration to unauthenticatedly access the /wp-json/wp/v2/users/ endpoint, retrieving a list of all registered users including their IDs, names, and usernames, enabling reconnaissance on site administrators and other users.

## Description

WordPress sites expose user information via the REST API by default without requiring authentication, allowing anyone to enumerate users. This is particularly risky on public-facing sites like mattermost.com, where admin details can be disclosed for targeted attacks. The procedure involves direct HTTP GET requests to the endpoint, succeeding due to the absence of access controls.

## Requirements

1. Web browser or HTTP client with access to the internet
2. Target WordPress site with exposed REST API (e.g., https://mattermost.com/wp-json/wp/v2/users/)
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Disable or restrict the /wp/v2/users endpoint using WordPress hooks like add_filter('rest_endpoints', ...)
- Implement authentication requirements for sensitive API routes
- Monitor access logs for repeated requests to /wp-json/wp/v2/users/
- Use web application firewalls (WAF) to block unauthenticated API enumeration

## Objectives

1. Enumerate all registered users on the target WordPress site
2. Identify admin accounts for potential follow-on attacks like phishing
3. Validate information disclosure vulnerability

## Instructions

### Step 1: Direct Endpoint Access

**Context**: Send a simple GET request to the users endpoint to fetch the JSON response containing user details.

**Instructions**: Open your browser and navigate to https://mattermost.com/wp-json/wp/v2/users/. No additional tools or commands are needed; the browser will display the raw JSON.

> The response includes an array of user objects with fields like id, name, slug (username), and registered_date. Success is indicated by a 200 OK status and parsable JSON without authentication prompts.

### Step 2: Parse and Review Response

**Context**: Examine the returned data to identify sensitive information such as admin usernames.

**Instructions**: Copy the JSON output and use a tool like jq (if available) or a JSON viewer to filter for admin-like entries (e.g., users with 'administrator' roles if exposed).

> Expected output: Filtered list of users, e.g., {"id":1,"name":"Site Admin","slug":"admin"}. Look for high-ID users or names indicating privilege.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[wordpress]]
- [[information-disclosure]]
- [[user-enumeration]]
