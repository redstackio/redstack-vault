---
tags:
  - idor
  - web
  - credit-card
  - payment
  - disclosure
  - modification
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Payment-Profile-Endpoint]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.574Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Yelp's payment profile endpoint to unauthorizedly access,
  disclose partial credit card details, and modify any user's credit card
  information.
skill_level: intermediate
impact_level: high
id: 750c9487-f3e3-4aad-8466-69006b5a5670
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Yelp Payment Endpoint to Edit User Credit Card Information and Disclose Partial Details

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in Yelp's /profile_payment/save endpoint.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Authenticated Session] --> B[Exploit IDOR to Access and Modify Payment Data]
    B --> C[Disclose Partial Credit Card Details]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]] (for intercepting and manipulating requests)

### Target Environment

- Web application (Yelp platform)
- Required services/ports: HTTPS on port 443
- Network access requirements: Internet access to Yelp's domain

### Initial Access Requirements

- Authenticated user session (valid Yelp account login)
- Network position: External attacker with a legitimate account
- Prior access needed: None beyond basic user registration

## Detailed Attack Procedures

### Step 1: Exploit IDOR in Payment Profile
procedure: [[procedures/Exploit-IDOR-in-Payment-Profile-Endpoint]]

**Objective**: Gain unauthorized access to another user's payment profile, disclose partial credit card details via error messages, and modify their credit card information by manipulating the user ID parameter in the save endpoint.

**Instructions**: Authenticate to Yelp, intercept the payment save request using a proxy like Burp Suite, and replace the user ID parameter with a target user's ID to trigger the IDOR. Submit the modified request to attempt editing or observe error messages revealing the last four digits of the target's credit card.

Use [[commands/curl-idor-exploit]] to simulate the manipulated POST request:

```bash
curl -X POST 'https://www.yelp.com/profile_payment/save' \
  -H 'Cookie: session=your_session_token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'user_id=TARGET_USER_ID&cc_number=4111111111111111&cc_exp=12/25&cvv=123'
```

Then, check the response for error messages that may leak the original last four digits.

**Expected Output**: HTTP response with error message containing partial credit card info (e.g., "Card ending in 1234 already exists") or successful modification confirmation.

**Success Indicators**:
- Error response discloses last four digits of target's card
- Ability to update card details without authorization errors
- No access denied messages for the target user ID
