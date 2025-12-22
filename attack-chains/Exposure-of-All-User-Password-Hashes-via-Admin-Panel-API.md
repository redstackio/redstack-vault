---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Exposure of All User Password Hashes via Admin Panel API
tags:
  - information-disclosure
  - password-hash-exposure
  - api-vulnerability
  - admin-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Admin-Login-for-Initial-Access]]'
  - '[[procedures/Navigate-to-User-Search-Interface]]'
  - '[[procedures/Trigger-API-Request-to-Expose-Hashes]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:20.386Z'
description: >-
  An authenticated admin can access the /api/users endpoint through the user
  search feature, which exposes hashed passwords for all users regardless of
  search parameters, enabling potential offline cracking of weak passwords.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Exposure of All User Password Hashes via Admin Panel API

Multi-stage attack chain demonstrating how an authenticated admin can extract all user password hashes via a misconfigured API endpoint in the user search feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Admin Authentication] --> B[Interface Navigation]
    B --> C[API Request and Hash Extraction]
    C --> D[Potential Cracking and Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with Developer Tools)
- [[tools/curl]]

### Target Environment

- Web application platform
- Admin panel accessible via HTTPS
- No specific ports required beyond standard web (443)

### Initial Access Requirements

- Valid admin credentials (username and password)
- Direct network access to the application
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Admin Authentication
procedure: [[procedures/Admin-Login-for-Initial-Access]]

**Objective**: Gain authenticated access to the admin panel using valid credentials.

**Instructions**: Open a web browser and navigate to the login page. Enter admin credentials to authenticate.

**Expected Output**: Successful login redirecting to the admin dashboard.

**Success Indicators**:
- Admin dashboard loads without errors
- Session cookie or token is established (visible in browser dev tools)

### Step 2: Navigate to User Search Interface
procedure: [[procedures/Navigate-to-User-Search-Interface]]

**Objective**: Access the user search functionality within the admin panel to prepare for triggering the vulnerable API.

**Instructions**: From the admin dashboard, click on "Admin" menu, then select "Search Users" to load the search interface.

**Expected Output**: User search form appears, ready for input.

**Success Indicators**:
- Search interface loads
- No authentication errors occur

### Step 3: Trigger API Request to Expose Hashes
procedure: [[procedures/Trigger-API-Request-to-Expose-Hashes]]

**Objective**: Send a search request that invokes the /api/users endpoint, capturing the response containing all user password hashes.

**Instructions**: In the search form, enter a test value like "test" in the firstName field and submit. Use browser dev tools (Network tab) to inspect the GET request to /api/users. Alternatively, use [[commands/curl-api-users-request]] to simulate:

```bash
curl -H "Authorization: Bearer <admin-token>" "https://target.com/api/users?page=1&userId=&firstName=test&lastName=&email=&partnerOrg=&highSchool="
```

Parse the JSON response to extract the "passwordHash" fields from the user objects.

**Expected Output**: JSON array of users including fields like id, firstName, email, and passwordHash for all users.

**Success Indicators**:
- Response includes passwordHash values
- All users returned, not filtered by search

## Attack Chain Summary

### Key Achievements

1. Authenticated access to admin panel
2. Navigation to vulnerable search interface
3. Extraction of all user password hashes via API

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

---
*Last updated: 2023-10-01T12:00:00Z*
