---
id: ac-wordpress-user-enum-001
tags:
  - user-enumeration
  - wordpress
  - api
  - access-control
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/User-Enumeration-via-WordPress-REST-API]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:11.045Z'
description: >-
  Demonstrates enumeration of WordPress users through the default REST API
  endpoint without access controls, leading to disclosure of user information.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# User Enumeration via Unprotected WordPress REST API

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery] --> B[Enumeration]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- WordPress platform
- Web service accessible over HTTP/HTTPS
- No specific ports required beyond standard 80/443

### Initial Access Requirements

- Public network access to the target WordPress site
- No credentials needed
- Prior reconnaissance to identify WordPress installation

## Detailed Attack Procedures

### Step 1: User Enumeration
procedure: [[procedures/User-Enumeration-via-WordPress-REST-API]]

**Objective**: Identify and list registered users on the target WordPress site by querying the unprotected REST API endpoint.

**Instructions**: Access the WordPress REST API users endpoint using [[commands/curl-wordpress-users-enum]] to retrieve user data without authentication:

```bash
curl -s https://jitsi.org/wp-json/wp/v2/users
```

This command sends a GET request to the default users endpoint, which returns JSON data including usernames, emails, and other user details if not restricted.

**Expected Output**: JSON array of user objects, e.g., {"id":1,"name":"admin","url":"","description":"","link":"https://jitsi.org/author/admin/","slug":"admin","avatar_urls":{"24":"https://...","48":"https://...","96":"https://..."},"meta":[],"_links":{"self":[{"href":"https://jitsi.org/wp-json/wp/v2/users/1"}],"collection":[{"href":"https://jitsi.org/wp-json/wp/v2/users"}]}}

**Success Indicators**:
- JSON response containing user data (e.g., usernames, IDs)
- No authentication prompt or 403 error
- Multiple users listed if site has registrations enabled

## Attack Chain Summary

### Key Achievements

1. Successful enumeration of user accounts without credentials
2. Disclosure of sensitive user information like usernames and emails
3. Identification of potential targets for further attacks (e.g., brute-force or social engineering)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
