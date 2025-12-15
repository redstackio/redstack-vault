---
tags:
  - idor
  - dos
  - shopify
  - session-expiration
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-as-Attacker-to-Shopify-Admin]]'
  - '[[procedures/Navigate-to-Account-Settings]]'
  - '[[procedures/Capture-Session-Expiration-Request]]'
  - '[[procedures/Modify-Request-with-Victim-Account-ID]]'
  - '[[procedures/Forward-Modified-Request-and-Verify-Logout]]'
step_count: 5
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.847Z'
description: >-
  An authenticated attacker exploits an Insecure Direct Object Reference (IDOR)
  vulnerability in Shopify's admin settings to expire sessions of arbitrary
  users, resulting in a denial-of-service by forcing logouts and disrupting
  account access.
skill_level: intermediate
impact_level: medium
id: d1dfe5a6-94c9-4863-a69d-8aa0c8b01539
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Shopify IDOR to Expire Arbitrary User Sessions

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR in Shopify's admin panel to perform a denial-of-service attack by expiring other users' sessions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login as Attacker] --> B[Navigate to Settings]
    B --> C[Capture Request]
    C --> D[Modify and Forward]
    D --> E[Victim Logout]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Shopify admin panel (web application)
- Required services/ports: HTTPS on port 443
- Network access requirements: Direct internet access to Shopify's admin domain

### Initial Access Requirements

- Valid attacker credentials for Shopify admin access
- Network position: Any authenticated session
- Prior access needed: None beyond authentication

## Detailed Attack Procedures

### Step 1: Login as Attacker
procedure: [[procedures/Login-as-Attacker-to-Shopify-Admin]]

**Objective**: Authenticate into the Shopify admin panel to establish a valid session for the attacker.

**Instructions**: Use standard login procedures to access the admin interface with attacker credentials.

**Expected Output**: Successful login redirect to the admin dashboard.

**Success Indicators**:
- Admin dashboard loads without errors
- Session cookies are set

### Step 2: Navigate to Account Settings
procedure: [[procedures/Navigate-to-Account-Settings]]

**Objective**: Access the account settings page to prepare for session expiration action.

**Instructions**: From the admin dashboard, navigate to the account settings via the menu or direct URL /admin/settings/account.

**Expected Output**: Account settings page loads, displaying options including session management.

**Success Indicators**:
- Page title indicates account settings
- Session expiration option is visible

### Step 3: Capture Session Expiration Request
procedure: [[procedures/Capture-Session-Expiration-Request]]

**Objective**: Intercept the HTTP POST request generated when attempting to expire the attacker's own sessions.

**Instructions**: Configure [[tools/Burp-Suite]] as a proxy, then click the 'expire all sessions' option on the account settings page to trigger and capture the request.

**Expected Output**: Captured POST request to /admin/settings/account/expire_specific_users_sessions/{attacker_id} with parameters like utf8=%E2%9C%93&_method=patch&authenticity_token={token}.

**Success Indicators**:
- Request intercepted in proxy tool
- Request details match expected format

### Step 4: Modify Request with Victim Account ID
procedure: [[procedures/Modify-Request-with-Victim-Account-ID]]

**Objective**: Alter the captured request to target the victim's account ID instead of the attacker's.

**Instructions**: In the proxy tool, edit the URL path to replace {attacker_id} with {victim_id}, e.g., change 7641433 to the victim's ID. Use [[commands/expire-user-sessions-curl]] for simulation if needed.

**Expected Output**: Modified POST request ready for forwarding, with victim's ID in the path.

**Success Indicators**:
- URL path updated correctly
- Parameters intact, including authenticity token

### Step 5: Forward Modified Request and Verify Logout
procedure: [[procedures/Forward-Modified-Request-and-Verify-Logout]]

**Objective**: Send the tampered request to the server and confirm the victim's sessions are expired.

**Instructions**: Forward the modified request through the proxy. Monitor the victim's account for logout on next access.

**Expected Output**: Server response indicating successful processing (e.g., 200 OK), and victim forced to re-login.

**Success Indicators**:
- No authorization errors on forward
- Victim reports or observes logout

## Attack Chain Summary

### Key Achievements

1. Authenticated access to admin panel
2. Exploitation of IDOR to target arbitrary accounts
3. Successful denial-of-service via session expiration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Impact]]

---

*Last updated: 2023-10-01T00:00:00Z*
