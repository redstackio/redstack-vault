---
id: ac-idor-phabricator-slowvote-001
tags:
  - idor
  - phabricator
  - api
  - information-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Phabricator-Slowvote-API]]'
step_count: 3
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.724Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  Phabricator's slowvote API to access hidden polls, bypassing visibility
  restrictions.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Phabricator Slowvote to Disclose Hidden Poll Details

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in Phabricator's slowvote feature. An authorized user creates a hidden slowvote, which is inaccessible via the web interface to unauthorized users. However, by directly manipulating the poll_id parameter in the API endpoint, an attacker can retrieve details like titles and authors, bypassing visibility controls.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Hidden Slowvote] --> B[Confirm Web Access Denial]
    B --> C[Exploit API IDOR]
    C --> D[Disclose Poll Details]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser dev tools)

### Target Environment

- Phabricator instance (web application)
- API endpoint accessible (/api/slowvote.info)
- Valid session cookies for an unauthorized user

### Initial Access Requirements

- Authenticated session as an unauthorized user (e.g., User B)
- Knowledge of a potential hidden poll ID (e.g., via enumeration or guess)
- Network access to the Phabricator server

## Detailed Attack Procedures

### Step 1: Create Hidden Slowvote (Setup by Authorized User)
procedure: [[procedures/Exploit-IDOR-in-Phabricator-Slowvote-API]]

**Objective**: Simulate the creation of a restricted slowvote to test visibility controls. This step is performed by an authorized user (e.g., User A) to establish the vulnerable hidden object.

**Instructions**: Navigate to the slowvote creation page and set visibility to 'No one' or specific users excluding the attacker.

**Expected Output**: A new slowvote with a unique poll ID (e.g., V1), URL format: http://phabricator.localhost.com/V1.

**Success Indicators**:
- Slowvote created successfully with restricted visibility.
- Poll ID noted for later exploitation.

### Step 2: Confirm Lack of Web Access
procedure: [[procedures/Exploit-IDOR-in-Phabricator-Slowvote-API]]

**Objective**: Verify that the web interface enforces visibility restrictions, confirming the vulnerability is in the API.

**Instructions**: As an unauthorized user (e.g., User B), attempt to access the slowvote URL directly in the browser.

**Expected Output**: Access denied message, such as a permission error page.

**Success Indicators**:
- Unauthorized access denied via web UI.
- Confirms the need for API exploitation.

### Step 3: Exploit API to Access Hidden Slowvote
procedure: [[procedures/Exploit-IDOR-in-Phabricator-Slowvote-API]]

**Objective**: Bypass restrictions by directly referencing the poll ID in the API request to disclose hidden details.

**Instructions**: Use an HTTP client to send a POST request to the API endpoint, specifying the target poll_id. Execute [[commands/phabricator-slowvote-api-idor]] with the appropriate parameters:

```bash
curl -X POST 'http://phabricator.localhost.com/api/slowvote.info' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: phsid=smpm4rp6yltbzna3qda2nwbomsoidzwjfshkkw7v; phusr=admin' \
  -d '__csrf__=B%40wmnrkyq3468c99179280354c&__form__=1&params[poll_id]=1&output=human'
```

Replace poll_id with the target ID (e.g., 1).

**Expected Output**: JSON or human-readable response containing the hidden slowvote's title, author, and other details.

**Success Indicators**:
- Poll information retrieved despite web denial.
- Details like title and author exposed.

## Attack Chain Summary

### Key Achievements

1. Confirmed web visibility restrictions are enforced.
2. Bypassed API authorization via direct object reference.
3. Disclosed sensitive poll metadata to unauthorized users.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---

*Last updated: 2024-01-01T00:00:00Z*
