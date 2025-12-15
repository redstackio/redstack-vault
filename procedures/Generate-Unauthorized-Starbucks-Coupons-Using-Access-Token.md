---
id: proc-generate-unauthorized-coupons
tags:
  - api-abuse
  - coupon-generation
  - unauthorized-access
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:28:51.705Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Generate Unauthorized Starbucks Coupons Using Access Token

## Summary

This procedure exploits an obtained access token to interact with the Starbucks API, creating unauthorized coupons and virtual cards, as demonstrated in the leaked credentials incident affecting promotional features.

## Description

With a valid token, make API calls to endpoints for generating promotional items. The token provides limited permissions, allowing creation but not full system access. Prerequisites: Functional access token and API documentation. Outcomes: Generated codes that could be redeemed, leading to financial or reputational impact.

## Requirements

1. Valid access token from authentication
2. API endpoints for coupons/cards (e.g., /generate/coupon)
3. Parameters for item creation (e.g., value, type)

## Defense

Defensive measures and detection strategies:

- Scope tokens to minimal permissions (e.g., read-only)
- Log and alert on unusual generation rates
- Implement CAPTCHA or verification for promo creation

## Objectives

1. Create promotional coupons/cards via API
2. Obtain redeemable codes
3. Assess potential for mass abuse

## Instructions

### Step 1: Identify Generation Endpoint

**Context**: Determine the API path for creating items.

Review API docs or test endpoints like /api/v1/coupons/generate.

> Prepare request headers: Authorization: Bearer <token>, Content-Type: application/json.

### Step 2: Submit Creation Request

**Context**: Send POST request with parameters to generate items.

POST to the endpoint with body {"value": 50, "type": "coupon", "quantity": 1}.

> Example: curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"value":50,"type":"coupon"}' https://api.starbucks.cn/coupons

### Step 3: Validate Generated Items

**Context**: Confirm creation and retrieve details.

Parse response for coupon code or card ID; test redemption if possible.

> Success: JSON with {"coupon_id": "abc123", "code": "STARBUCKS50"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (adapted for API scripting)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-abuse]]
- [[coupon-generation]]
- [[unauthorized-access]]
