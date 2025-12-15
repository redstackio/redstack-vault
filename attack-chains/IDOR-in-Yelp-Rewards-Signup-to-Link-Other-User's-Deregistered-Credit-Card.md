---
id: yelp-idor-rewards-credit-card
tags:
  - idor
  - yelp
  - credit-card
  - privacy-violation
  - web-vulnerability
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
  - '[[procedures/Discover-IDOR-in-Yelp-Rewards-Signup]]'
  - '[[procedures/Exploit-IDOR-to-Link-External-Credit-Card]]'
step_count: 2
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:47.516Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  Yelp's /rewards/signup endpoint to associate another user's deregistered
  credit card with the attacker's account, enabling access to transaction
  history and cash back details.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
---
# IDOR in Yelp Rewards Signup to Link Other User's Deregistered Credit Card

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in Yelp's rewards system.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of IDOR] --> B[Exploitation to Link Card]
    B --> C[Access Transaction Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for inspecting requests
- Valid Yelp account

### Target Environment

- Web platform
- Yelp rewards system service
- Access to /rewards/signup endpoint

### Initial Access Requirements

- Authenticated session on Yelp
- Knowledge of external credit card identifiers (e.g., from prior testing or leaks)
- No special network access beyond internet

## Detailed Attack Procedures

### Step 1: Discovery of IDOR Vulnerability
procedure: [[procedures/Discover-IDOR-in-Yelp-Rewards-Signup]]

**Objective**: Identify the lack of authorization checks in the /rewards/signup endpoint that allows associating arbitrary credit card identifiers.

**Instructions**: Inspect the rewards signup process using browser developer tools or a proxy. Attempt to add a randomly generated but deregistered credit card identifier during signup and observe if it associates without validation.

**Expected Output**: The endpoint accepts the external card ID without error, indicating missing access controls.

**Success Indicators**:
- Card association succeeds for non-owned cards
- No authorization denial on external IDs

### Step 2: Exploitation to Link External Credit Card
procedure: [[procedures/Exploit-IDOR-to-Link-External-Credit-Card]]

**Objective**: Manipulate the endpoint to link another user's deregistered credit card to the attacker's account, gaining access to related data.

**Instructions**: Use a tool like curl to send a modified request to the /rewards/signup endpoint with the target credit card identifier. Ensure the request includes the attacker's session cookies for authentication.

Execute [[commands/curl-yelp-rewards-signup]] to perform the association:

```bash
curl -X POST 'https://www.yelp.com/rewards/signup' \
  -H 'Cookie: session=attacker_session' \
  -H 'Content-Type: application/json' \
  -d '{"card_id": "external_card_identifier_from_other_user"}'
```

Then, query the rewards dashboard to verify access to transaction history.

**Expected Output**: Successful response confirming card linkage, followed by visible transaction and cash back data.

**Success Indicators**:
- Card linked to attacker's account
- Transaction history and cash back details accessible

## Attack Chain Summary

### Key Achievements

1. Discovered IDOR allowing unauthorized card associations
2. Linked external deregistered credit card to own account
3. Accessed privacy-sensitive transaction data without card usage

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Web Session Cookie]] Data from Information Repositories
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
