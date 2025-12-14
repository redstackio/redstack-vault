---
tags:
  - api
  - access-control
  - token
  - hackerone
  - banned-user
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-HackerOne-Test-Account]]'
  - '[[procedures/Generate-HackerOne-API-Token]]'
  - '[[procedures/Ban-HackerOne-Test-Account]]'
  - '[[procedures/Exploit-HackerOne-API-with-Old-Token]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:48.479Z'
description: >-
  Demonstrates how banned and deleted HackerOne user accounts can be accessed
  using unrevoked API tokens, allowing retrieval of sensitive data like reports,
  payments, and programs.
skill_level: intermediate
impact_level: high
id: 53a72d80-e8ac-4638-8907-143e759a8211
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Banned User Access to Deleted HackerOne Account via Persistent API Token

Multi-stage attack chain demonstrating improper access control in HackerOne's API, where banned and deleted user accounts remain accessible via previously generated API tokens that are not revoked upon banning. This allows full access to sensitive data including reports, balance, earnings, payouts, weaknesses, and programs, potentially exposing private information of banned users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Test Account] --> B[Generate API Token]
    B --> C[Ban Account]
    C --> D[Exploit API Endpoints]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Platform: Web (HackerOne platform)
- Required services/ports: HTTPS (443) access to api.hackerone.com
- Network access requirements: Internet connectivity to HackerOne API

### Initial Access Requirements

- No prior credentials needed for test account creation
- Ability to register on HackerOne
- Administrative access to ban the account (simulated via support request in testing)

## Detailed Attack Procedures

### Step 1: Create Test Account
procedure: [[procedures/Create-HackerOne-Test-Account]]

**Objective**: Establish a test user account on HackerOne to simulate the vulnerability setup.

**Instructions**: Register a new user account using valid email and credentials on the HackerOne platform.

**Expected Output**: Successful account creation with login credentials.

**Success Indicators**:
- Account login successful
- User dashboard accessible

### Step 2: Generate API Token
procedure: [[procedures/Generate-HackerOne-API-Token]]

**Objective**: Create an API token for the test account before banning to enable persistent access.

**Instructions**: Log in to the account and generate an API token via the user settings.

**Expected Output**: API token generated, e.g., 'XXXXXXXXXXXXXXXXXXXX=' for username 'mrtst'.

**Success Indicators**:
- Token visible in account settings
- Token can be used for API authentication

### Step 3: Ban the Account
procedure: [[procedures/Ban-HackerOne-Test-Account]]

**Objective**: Simulate account banning to trigger the deletion process while keeping the token active.

**Instructions**: Request a permanent ban on the test account through HackerOne support and wait for processing; ensure no pending payouts to allow deletion.

**Expected Output**: Account marked as banned and deleted.

**Success Indicators**:
- Ban confirmation received
- Account no longer accessible via web login

### Step 4: Exploit API Endpoints
procedure: [[procedures/Exploit-HackerOne-API-with-Old-Token]]

**Objective**: Use the old API token to access sensitive data from the banned/deleted account.

**Instructions**: Authenticate to various API endpoints using curl with the old token and username. For example, fetch reports with [[commands/curl-hackerone-fetch-reports]]:

```bash
curl "https://api.hackerone.com/v1/hackers/me/reports" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

Fetch balance with [[commands/curl-hackerone-fetch-balance]]:

```bash
curl "https://api.hackerone.com/v1/hackers/payments/balance" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

Similarly, use [[commands/curl-hackerone-fetch-earnings]], [[commands/curl-hackerone-fetch-payouts]], [[commands/curl-hackerone-fetch-program-weaknesses]] (replace {handle}), and [[commands/curl-hackerone-fetch-programs]].

**Expected Output**: JSON responses containing sensitive data like reports, financial info, and programs.

**Success Indicators**:
- API returns 200 OK with data
- Sensitive information retrieved despite ban

## Attack Chain Summary

### Key Achievements

1. Successful creation and banning of test account
2. Generation of persistent API token
3. Access to deleted account's reports and financial data
4. Exposure of private program weaknesses and associations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
