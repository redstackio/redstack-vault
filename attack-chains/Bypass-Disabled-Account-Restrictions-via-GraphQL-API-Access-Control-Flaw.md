---
tags:
  - graphql
  - access-control-bypass
  - disabled-account
  - data-exfiltration
  - api-modification
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
  - '[[Command and Control]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Configure-Burp-Suite-Proxy]]'
  - '[[procedures/Authenticate-Disabled-Account]]'
  - '[[procedures/Observe-UI-Redirects]]'
  - '[[procedures/Intercept-GraphQL-Requests]]'
  - '[[procedures/Modify-and-Replay-GraphQL-Queries]]'
  - '[[procedures/Execute-Sessions-Data-Retrieval]]'
  - '[[procedures/Perform-Payment-Method-Mutation]]'
  - '[[procedures/Verify-Changes-After-Reactivation]]'
step_count: 8
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T17:25:53.416Z'
description: >-
  Attack chain exploiting improper access controls in HackerOne's GraphQL API,
  allowing disabled accounts to authenticate and perform data retrieval and
  modifications without reactivation.
skill_level: intermediate
impact_level: high
id: deff2680-8baf-4732-9c21-cb7668c2fe94
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Bypass Disabled Account Restrictions via GraphQL API Access Control Flaw

Multi-stage attack chain demonstrating exploitation of improper access controls in HackerOne's GraphQL endpoint, where disabled user accounts can still authenticate and execute queries/mutations to access sensitive data like session history, team memberships, payment details, and even modify preferences without triggering user notifications.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Configure Proxy] --> B[Authenticate Disabled Account]
    B --> C[Observe UI Restrictions]
    C --> D[Intercept GraphQL Requests]
    D --> E[Modify and Replay Queries]
    E --> F[Retrieve Sensitive Data]
    F --> G[Perform Data Mutations]
    G --> H[Verify Impact Post-Reactivation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#9b59b6
    style G fill:#9b59b6
    style H fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with GraphQL API (e.g., HackerOne at hackerone.com/graphql)
- Required services/ports: HTTPS on port 443
- Network access requirements: Direct internet access to target domain

### Initial Access Requirements

- Valid credentials (username/password) for a disabled target account
- Network position: External attacker with stolen credentials
- Prior access needed: None, but credentials must be obtained separately (e.g., via phishing)

## Detailed Attack Procedures

### Step 1: Configure Proxy
procedure: [[procedures/Configure-Burp-Suite-Proxy]]

**Objective**: Set up traffic interception to capture and modify API requests from the authenticated session.

**Instructions**: Launch Burp Suite and configure the browser to route traffic through Burp's proxy on localhost:8080. Enable interception if needed for real-time capture, but use HTTP History for post-login analysis.

**Expected Output**: Browser traffic proxied; Burp captures requests to hackerone.com.

**Success Indicators**:
- Burp Proxy tab shows active listener on 127.0.0.1:8080
- Browser F12 network tab reflects proxied requests

### Step 2: Authenticate Disabled Account
procedure: [[procedures/Authenticate-Disabled-Account]]

**Objective**: Log in with disabled account credentials to establish an authenticated session despite UI blocks.

**Instructions**: Navigate to the login page (https://hackerone.com/login) and enter the disabled account's credentials. The authentication succeeds backend, generating X-Auth-Token and session cookies.

**Expected Output**: Redirect to disabled account page with message: "You are unable to log in and others are unable to interact with this account..."

**Success Indicators**:
- Authentication token in cookies/headers
- UI shows disabled status but session is active

### Step 3: Observe UI Restrictions
procedure: [[procedures/Observe-UI-Redirects]]

**Objective**: Confirm frontend enforcement of disabled status while identifying backend bypass opportunities.

**Instructions**: Interact with the UI by clicking menus or settings; observe redirects to https://hackerone.com/settings/disabled/edit.

**Expected Output**: All UI actions blocked or redirected, but underlying requests in Burp History show GraphQL POSTs.

**Success Indicators**:
- Redirects to disabled/edit page
- GraphQL requests appear in Burp despite UI blocks

### Step 4: Intercept GraphQL Requests
procedure: [[procedures/Intercept-GraphQL-Requests]]

**Objective**: Capture legitimate GraphQL requests triggered by the UI for later modification.

**Instructions**: In Burp's HTTP History, filter for POST requests to /graphql and identify the latest one post-login.

**Expected Output**: List of intercepted POST /graphql requests with JSON payloads.

**Success Indicators**:
- Requests show X-Auth-Token header and session cookies
- Payloads contain GraphQL queries like Sessions_page

### Step 5: Modify and Replay GraphQL Queries
procedure: [[procedures/Modify-and-Replay-GraphQL-Queries]]

**Objective**: Alter intercepted requests to execute custom queries bypassing UI limits.

**Instructions**: Right-click the request in History, send to Repeater. Edit the JSON body to replace with a custom query (e.g., for sessions or teams), then send.

**Expected Output**: Modified request sent; response with targeted data.

**Success Indicators**:
- Repeater shows successful 200 OK response
- No authentication errors in response

### Step 6: Retrieve Sensitive Data
procedure: [[procedures/Execute-Sessions-Data-Retrieval]]

**Objective**: Exfiltrate sensitive information like session history, IPs, and team details.

**Instructions**: Use a modified query for Sessions_page or User_programs_settings_page in Repeater, setting variables like first_0:10.

**Expected Output**: JSON with session IDs, IP addresses, user agents, team memberships.

**Success Indicators**:
- Data includes sensitive fields (e.g., IP, payment prefs)
- No errors; full dataset returned

### Step 7: Perform Data Mutations
procedure: [[procedures/Perform-Payment-Method-Mutation]]

**Objective**: Modify account data, such as adding a payment method, without owner notification.

**Instructions**: Craft a mutation like Create_paypal_preference_mutation with input paypal_email: "test@example.com", send via Repeater.

**Expected Output**: JSON response with was_successful: true and updated preferences.

**Success Indicators**:
- Mutation executes without errors
- No reactivation email triggered

### Step 8: Verify Impact
procedure: [[procedures/Verify-Changes-After-Reactivation]]

**Objective**: Confirm persistence of changes after account enablement.

**Instructions**: Click 'Enable' to reactivate (triggers email), then log in normally and check settings/payment_preferences.

**Expected Output**: New payment method visible in UI.

**Success Indicators**:
- Added payment method persists
- Original owner unaware until email (if any)

## Attack Chain Summary

### Key Achievements

1. Successful authentication and API access with disabled credentials
2. Retrieval of sensitive data (sessions, teams, payments) via custom GraphQL queries
3. Modification of account data (e.g., payment methods) without notifications

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Exfiltration Over Alternative Protocol]] Exfiltration Over Alternative Protocol

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection
- [[Command and Control]] Defense Evasion

---

*Last updated: 2023-10-01T00:00:00Z*
