---
tags:
  - wordpress
  - api
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
procedures:
  - '[[procedures/Enumerate-WordPress-Users-via-Exposed-REST-API]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
description: >-
  An attack chain exploiting an exposed WordPress REST API endpoint to disclose
  sensitive user information, including admin usernames, enabling further
  brute-force attacks.
skill_level: beginner
impact_level: high
id: 06458496-40e6-4bbf-a745-c5f4de729b2e
created_at: '2025-12-14T17:30:27.217Z'
updated_at: '2025-12-14T17:30:27.217Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# WordPress REST API User Enumeration Leading to Admin Username Disclosure

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
    A[Reconnaissance: Access Exposed API] --> B[Discovery: Extract User Data]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- None (browser or curl sufficient)

### Target Environment

- Target OS/Platform: Web
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Public internet access to the target domain

### Initial Access Requirements

- Credential requirements: None
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Access Exposed REST API for User Enumeration
procedure: [[procedures/Enumerate-WordPress-Users-via-Exposed-REST-API]]

**Objective**: Retrieve a list of all users, including admin usernames, from the unprotected WordPress REST API endpoint to facilitate targeted brute-force attacks.

**Instructions**: Directly access the WordPress REST API users endpoint using a browser or [[commands/curl-access-wp-rest-api]] to fetch the JSON response containing user details.

```bash
curl -s http://affiliates.udemy.com/wp-json/wp/v2/users
```

Parse the JSON output to identify admin users by checking roles or slugs (e.g., usernames like 'hamza', 'imanrana', 'nupoora').

**Expected Output**: A JSON array of user objects, each with fields like 'id', 'name', 'slug', 'roles', revealing admin usernames without authentication.

**Success Indicators**:
- JSON response contains user list with admin details
- No authentication prompt or error (e.g., 401 Unauthorized)

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of admin usernames via public API access
2. Identification of targets for brute-force password attacks
3. Potential pathway to full administrative access on the WordPress site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2024-10-01T00:00:00Z*
