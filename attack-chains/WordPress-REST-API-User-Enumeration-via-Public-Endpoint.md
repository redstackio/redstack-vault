---
tags:
  - wordpress
  - information-disclosure
  - user-enumeration
  - rest-api
type: attack_chain
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enumerate-WordPress-Users-via-REST-API]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:55.844Z'
description: >-
  A reconnaissance attack exploiting default WordPress REST API configuration to
  disclose user details, enabling targeted brute-force attacks.
skill_level: beginner
impact_level: medium
id: 9347e10b-5199-4809-941c-c5e3b24dd578
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# WordPress REST API User Enumeration via Public Endpoint

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Reconnaissance] --> B[User Data Collection]

    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]

### Target Environment

- Target OS/Platform: Web
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Public internet access to the target WordPress site

### Initial Access Requirements

- Credential requirements: None (unauthenticated)
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Enumerate Users via REST API

procedure: [[procedures/Enumerate-WordPress-Users-via-REST-API]]

**Objective**: Retrieve a list of all users, including admins and employees, from the public WordPress REST API endpoint to gather usernames for further attacks.

**Instructions**: Open a web browser and navigate to the target site's WordPress REST API users endpoint, such as `https://target.com/wp-json/wp/v2/users/`. The endpoint returns JSON data without authentication. Alternatively, use [[commands/curl-fetch-users]] to fetch the data via command line:

```bash
curl https://sifchain.finance/wp-json/wp/v2/users/
```

Parse the JSON response to extract usernames, IDs, and other details.

**Expected Output**: A JSON array of user objects, each containing fields like `id`, `name`, `slug` (login name), `description`, and links.

**Success Indicators**:
- JSON response with user data is returned
- Multiple user entries, including admin or employee accounts, are visible
- No authentication prompt or error occurs

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of sensitive user information without authentication
2. Identification of admin and employee usernames for targeted brute-force attacks
3. Demonstration of default WordPress misconfiguration risks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
