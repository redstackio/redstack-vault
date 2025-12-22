---
id: ac-starbucks-leaked-credentials-766770
tags:
  - credential-leak
  - github
  - api-abuse
  - unauthorized-access
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
  - '[[procedures/Discover-Exposed-Credentials-in-Public-GitHub-Repository]]'
  - '[[procedures/Authenticate-with-Leaked-Credentials-to-Obtain-Access-Token]]'
  - '[[procedures/Generate-Unauthorized-Starbucks-Coupons-Using-Access-Token]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:28:51.731Z'
description: >-
  Attack chain exploiting leaked credentials from a public GitHub repository to
  gain unauthorized access to Starbucks' API for generating coupons and virtual
  cards.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Credentials In Files]]'
---
# Leaked GitHub Credentials Enabling Unauthorized Starbucks Coupon and Card Generation

Multi-stage attack chain demonstrating exploitation of leaked credentials in a public GitHub repository to access Starbucks' China operations API and generate promotional coupons and virtual cards.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Leaked Credentials] --> B[Authenticate and Obtain Token]
    B --> C[Generate Coupons and Cards]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or GitHub search interface
- API testing tool (e.g., curl or Postman)

### Target Environment

- Public GitHub repositories
- Starbucks China API services for coupons and cards
- Internet access

### Initial Access Requirements

- No prior credentials needed; relies on publicly exposed data
- Ability to search GitHub for sensitive keywords

## Detailed Attack Procedures

### Step 1: Discover Leaked Credentials
procedure: [[procedures/Discover-Exposed-Credentials-in-Public-GitHub-Repository]]

**Objective**: Identify and extract sensitive credentials from a publicly accessible GitHub repository.

**Instructions**: Search GitHub for repositories related to the target organization using keywords like "Starbucks credentials" or specific file names. Once the repository is found, navigate to the exposed file and copy the credentials (e.g., API keys or usernames/passwords).

**Expected Output**: Raw credentials such as username:password or API tokens.

**Success Indicators**:
- Credentials successfully extracted from the repository
- Validation that credentials are active by testing in a safe environment

### Step 2: Authenticate with Leaked Credentials
procedure: [[procedures/Authenticate-with-Leaked-Credentials-to-Obtain-Access-Token]]

**Objective**: Use the discovered credentials to authenticate against the target's authentication endpoint and obtain a valid access token.

**Instructions**: Send an authentication request to the Starbucks API endpoint using the leaked credentials. For example, use a POST request to the login or token endpoint with the username and password in the body.

**Expected Output**: A JSON response containing an access token (e.g., {"access_token": "eyJ..."}).

**Success Indicators**:
- Access token received without errors
- Token can be used for subsequent API calls

### Step 3: Generate Unauthorized Coupons
procedure: [[procedures/Generate-Unauthorized-Starbucks-Coupons-Using-Access-Token]]

**Objective**: Leverage the access token to interact with the API and create unauthorized promotional coupons or virtual cards.

**Instructions**: Include the access token in the Authorization header of API requests to the coupons or cards generation endpoint. Submit requests to create new items, specifying parameters like value or type.

**Expected Output**: Confirmation of created coupons/cards, such as generated codes or QR links.

**Success Indicators**:
- Successful API response with new coupon/card details
- Ability to redeem or view the generated items

## Attack Chain Summary

### Key Achievements

1. Discovery of sensitive credentials in a public repository
2. Unauthorized authentication to obtain API access
3. Generation of promotional materials leading to potential abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Credentials In Files]] Credentials In Files

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
