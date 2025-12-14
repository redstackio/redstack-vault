---
id: ac-instacart-auth-bypass-chat-logs
tags:
  - authorization-bypass
  - idor
  - api-vulnerability
  - data-disclosure
  - firebase-leak
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Mobile (iOS)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Intercept-API-Traffic-with-Burp-Suite-to-Identify-Chat-Logs-Endpoint]]
  - '[[procedures/Modify-Order-Delivery-ID-to-Access-Unauthorized-Order-Data]]'
  - >-
    [[procedures/Exploit-Leaked-Firebase-Tokens-to-Retrieve-Additional-Order-Data]]
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:57.173Z'
description: >-
  Multi-stage attack exploiting an authorization bypass in the Instacart mobile
  app API to access other users' order chat logs, details, and leaked Firebase
  tokens for further data exfiltration.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
  - '[[Unsecured Credentials]]'
---
# Authorization Bypass in Instacart Order Delivery Chat Logs Leading to Private Data Disclosure

Multi-stage attack chain demonstrating an authorization bypass in the Instacart mobile app API, allowing authenticated users to access private chat logs, order details, and Firebase tokens of other users by manipulating the order_delivery_id parameter.

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
    A[Intercept API Traffic] --> B[Modify Request ID]
    B --> C[Exploit Leaked Tokens]
    C --> D[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/curl]]

### Target Environment

- Instacart mobile app (iOS)
- Authenticated session to www.instacart.com API
- Network access to intercept mobile traffic (e.g., via proxy)

### Initial Access Requirements

- Valid Instacart user account with at least one past order
- Ability to proxy mobile app traffic (e.g., configure iOS proxy to Burp)
- No elevated privileges needed beyond authentication

## Detailed Attack Procedures

### Step 1: Intercept API Traffic
procedure: [[procedures/Intercept-API-Traffic-with-Burp-Suite-to-Identify-Chat-Logs-Endpoint]]

**Objective**: Capture and analyze the API request triggered by viewing chat logs on a past order to identify the vulnerable endpoint.

**Instructions**: Configure Burp Suite as a proxy for the Instacart iOS app traffic. Navigate to a past order in the app and tap 'View Chat Logs' to trigger the request. Intercept the GET request to /api/v2/order_deliveries/{order_delivery_id}/order_change_logs.

**Expected Output**: HTTP request details showing the endpoint structure, e.g., GET /api/v2/order_deliveries/261932226/order_change_logs on host www.instacart.com.

**Success Indicators**:
- Request intercepted successfully
- Endpoint path confirmed with order_delivery_id parameter

### Step 2: Modify Order Delivery ID
procedure: [[procedures/Modify-Order-Delivery-ID-to-Access-Unauthorized-Order-Data]]

**Objective**: Alter the order_delivery_id in the intercepted request to access another user's private data without authorization checks.

**Instructions**: In Burp Suite, change the order_delivery_id from your own order (e.g., 261932226) to another user's order ID (e.g., 261972220). Forward the modified GET request to the same endpoint. Review the response for leaked data.

**Expected Output**: JSON response containing chat messages, order placement time, out-of-stock changes, product names, and Firebase tokens—no authorization error.

**Success Indicators**:
- Response returns data for the targeted order
- Private chat logs and details disclosed

### Step 3: Exploit Leaked Firebase Tokens
procedure: [[procedures/Exploit-Leaked-Firebase-Tokens-to-Retrieve-Additional-Order-Data]]

**Objective**: Use exposed Firebase tokens from the API response to query the Firebase Realtime Database for further unauthorized order delivery data.

**Instructions**: Extract the Firebase token/ID from the leaked JSON response (e.g., xy8TcFsDZiKm1JwnqqFp). Execute [[commands/curl-firebase-order-deliveries]] to fetch additional order delivery IDs.

```bash
curl https://instacart.firebaseio.com/order_deliveries/xy8TcFsDZiKm1JwnqqFp.json
```

**Expected Output**: JSON object listing order delivery IDs, e.g., {"46671792":"","46671794":"",...}.

**Success Indicators**:
- Firebase query succeeds without authentication
- Additional order IDs retrieved for potential further exploitation

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access private chat logs and order details of arbitrary users.
2. Exposed sensitive Firebase tokens enabling database exfiltration.
3. Demonstrated potential for broader data compromise via chained leaks.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery
- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
