---
id: ac-omise-anon-access-001
tags:
  - access-control
  - api
  - payment
  - omise
  - unauthenticated
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Retrieve-Omise-Payment-Status-Anonymously]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.775Z'
description: >-
  Demonstrates unauthorized retrieval of payment processing status from the
  Omise API by exploiting improper access controls on the payment status
  endpoint.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Anonymous Access to Omise Payment Status via Unauthenticated API Endpoint

Multi-stage attack chain demonstrating a complete attack workflow.

The vulnerability stems from the Omise API's /payments/{payment_id}/status endpoint lacking proper authentication, enabling any unauthenticated user to query payment details like processing status. This exposes sensitive transaction information to attackers, potentially aiding in fraud or reconnaissance on payment flows. The attack requires only a known payment ID and network access to the API.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Objective]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (standard HTTP client like curl)

### Target Environment

- Web platform
- Omise Payment API service on api.omise.co
- No specific ports required (HTTPS/443)

### Initial Access Requirements

- Public network access to api.omise.co
- Knowledge of a valid payment ID (e.g., from public sources or prior enumeration)
- No credentials needed

## Detailed Attack Procedures

### Step 1: Unauthorized Payment Status Retrieval
procedure: [[procedures/Retrieve-Omise-Payment-Status-Anonymously]]

**Objective**: Access sensitive payment status information without authentication to expose transaction details.

**Instructions**: Send an unauthenticated GET request to the payment status endpoint using a tool like curl, specifying the payment ID in the path. Include standard browser-like headers to mimic a legitimate request over HTTP/2.

Execute [[commands/get-omise-payment-status]]:

```bash
curl -X GET "https://api.omise.co/payments/paym_test_5rjz482tky43reoil9f/status" \
  -H "Sec-Ch-Ua: \"\" " \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" \
  -H "Accept: */*" \
  -H "Referer: https://api.omise.co/" \
  --http2
```

**Expected Output**: JSON response with payment status, e.g., {"processed":true}.

**Success Indicators**:
- HTTP 200 OK response
- JSON body containing payment details like "processed" status
- No authentication challenge (e.g., no 401 Unauthorized)

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to access restricted payment data
2. Retrieved processing status of a payment transaction anonymously
3. Demonstrated exposure of sensitive financial information to unauthorized parties

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
