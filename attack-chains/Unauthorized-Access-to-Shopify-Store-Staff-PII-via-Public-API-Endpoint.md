---
tags:
  - auth-bypass
  - pii-disclosure
  - shopify
  - api
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-api-request]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Access-Shopify-Public-API-Without-Authentication]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  An attack chain exploiting improper authentication in Shopify's public API to
  disclose store staff first and last names without credentials.
skill_level: beginner
impact_level: medium
id: 6b0549a6-25c5-4fd7-9827-73101a344e2e
created_at: '2025-12-14T17:28:45.031Z'
updated_at: '2025-12-14T17:28:45.031Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Access to Shopify Store Staff PII via Public API Endpoint

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via API] --> B[Data Collection]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Shopify store platform
- Public API endpoint accessible over HTTPS
- No specific ports required beyond standard web (443)

### Initial Access Requirements

- Internet access to the target Shopify store
- No credentials needed due to the vulnerability
- Knowledge of the target store's domain

## Detailed Attack Procedures

### Step 1: Access Public API Endpoint
procedure: [[procedures/Access-Shopify-Public-API-Without-Authentication]]

**Objective**: Retrieve store staff first and last names without authentication by exploiting the unprotected API endpoint.

**Instructions**: Identify the target Shopify store domain, then use [[commands/curl-api-request]] to send an unauthenticated GET request to the public API endpoint that exposes staff details.

```bash
curl -X GET "https://target-shopify-store.myshopify.com/api/staff" -H "Content-Type: application/json"
```

**Expected Output**: JSON response containing an array of staff objects with fields like "first_name" and "last_name".

**Success Indicators**:
- HTTP 200 response with staff PII data
- No authentication prompt or error

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication to access sensitive staff information
2. Disclosed personally identifiable information (PII) including names
3. Demonstrated impact of improper API protections in e-commerce platforms

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-23*
