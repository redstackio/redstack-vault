---
tags:
  - broken-access-control
  - shopify
  - api-bypass
  - privilege-escalation
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/mitmproxy]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-Shopify-Mobile-with-Limited-Access]]'
  - '[[procedures/Capture-Access-Token-from-Mobile-Session]]'
  - '[[procedures/Exploit-API-for-Unauthorized-User-Management]]'
  - '[[procedures/Access-Users-Endpoint-for-Discovery]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:01.797Z'
description: >-
  Multi-stage attack exploiting improper authentication in Shopify's API to
  bypass access controls, enabling limited users to escalate privileges by
  creating full-access accounts, deleting users, and discovering all store
  users.
skill_level: intermediate
impact_level: high
id: bc9a8aed-5cd1-41ca-952c-3b76d45cb27f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Shopify API Broken Access Control for Privilege Escalation and User Discovery

Multi-stage attack chain demonstrating exploitation of Shopify's API authentication flaws, allowing limited-access users to gain full administrative control and disclose user lists.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login with Limited Access] --> B[Capture Token]
    B --> C[Unauthorized User Management]
    C --> D[User List Discovery]
    D --> E[Privilege Escalation Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/mitmproxy]]
- [[tools/curl]]

### Target Environment

- Shopify store with API access
- Shopify Mobile app installed on iOS/Android
- Network access to Shopify API endpoints (e.g., admin.shopify.com)

### Initial Access Requirements

- Valid limited-access admin credentials for the Shopify store
- Ability to intercept mobile app traffic (e.g., rooted/jailbroken device or proxy setup)
- No prior full admin access needed

## Detailed Attack Procedures

### Step 1: Login to Shopify Mobile App
procedure: [[procedures/Login-to-Shopify-Mobile-with-Limited-Access]]

**Objective**: Authenticate with a limited-access account to initiate a session in the mobile app.

**Instructions**: Install the Shopify Mobile app and log in using limited-access admin credentials. Ensure the device is configured for traffic interception if needed for the next step.

**Expected Output**: Successful login to the app dashboard with limited functionality visible.

**Success Indicators**:
- App loads store dashboard
- Limited features (e.g., no full user management) are accessible

### Step 2: Capture Access Token
procedure: [[procedures/Capture-Access-Token-from-Mobile-Session]]

**Objective**: Extract the authentication token generated during mobile login for reuse in API calls.

**Instructions**: Set up a proxy like [[tools/mitmproxy]] to intercept app traffic. Perform actions in the app to trigger API calls, then extract the bearer token from request headers.

**Expected Output**: A valid access token string (e.g., starting with 'shpat_').

**Success Indicators**:
- Token captured in proxy logs
- Token can be used in manual API tests without errors

### Step 3: Exploit API for Unauthorized User Management
procedure: [[procedures/Exploit-API-for-Unauthorized-User-Management]]

**Objective**: Use the captured token to bypass restrictions and perform admin actions like creating or deleting users.

**Instructions**: Use [[commands/curl-api-request]] to send POST requests to user creation endpoints with the token. Verify by checking the store's user list post-exploitation.

```bash
curl -X POST -H "X-Shopify-Access-Token: <captured_token>" https://<store>.myshopify.com/admin/api/2023-10/staff_members.json -d '{"staff_member":{"email":"newadmin@example.com","password":"pass123","permissions":["full"]}}'
```

**Expected Output**: JSON response confirming user creation (e.g., {"staff_member": {...}}).

**Success Indicators**:
- New full-access user created
- Ability to delete existing users via similar DELETE requests

### Step 4: Access Users Endpoint for Discovery
procedure: [[procedures/Access-Users-Endpoint-for-Discovery]]

**Objective**: Query the users endpoint to retrieve the full list of store users, even without proper permissions.

**Instructions**: Send a GET request to the users endpoint using the captured token with [[commands/curl-api-request]]. Parse the response for user details.

```bash
curl -H "X-Shopify-Access-Token: <captured_token>" https://<store>.myshopify.com/admin/api/2023-10/staff_members.json
```

**Expected Output**: JSON array of all staff members, including emails and roles.

**Success Indicators**:
- Full user list returned, including those not visible in the web interface
- No permission errors in response

## Attack Chain Summary

### Key Achievements

1. Bypassed API permission checks using mobile-derived tokens
2. Escalated from limited to full access by creating admin users
3. Disclosed complete store user inventory for potential targeting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
