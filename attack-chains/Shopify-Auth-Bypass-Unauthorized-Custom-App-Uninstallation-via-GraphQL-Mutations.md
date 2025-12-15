---
id: ac-shopify-auth-bypass-app-uninstall
tags:
  - auth-bypass
  - shopify
  - graphql
  - app-uninstall
  - integrity-violation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Limited-Staff-Account]]'
  - '[[procedures/Identify-Target-App-ID]]'
  - '[[procedures/Execute-GraphQL-App-Uninstall-Mutation]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:19.758Z'
description: >-
  Multi-stage attack exploiting improper authorization in Shopify's GraphQL API
  to allow staff users with limited permissions to uninstall custom apps,
  disrupting store functionality.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Shopify Auth Bypass: Unauthorized Custom App Uninstallation via GraphQL Mutations

Multi-stage attack chain demonstrating improper authorization in Shopify's admin GraphQL API, where staff users with only 'Manage and install apps and channels' permission can uninstall custom apps without the required 'Develop apps' permission. This leads to a low-severity integrity violation by enabling unauthorized app removal, potentially disrupting store operations such as custom integrations or automations.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Limited Staff Account] --> B[Identify Target App ID]
    B --> C[Execute GraphQL Uninstall Mutation]
    C --> D[App Uninstalled - Integrity Violation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or curl for sending HTTP requests
- Access to Shopify admin panel

### Target Environment

- Shopify store with admin access
- Custom apps installed
- GraphQL API endpoints available (/admin/internal/web/graphql/core)

### Initial Access Requirements

- Valid Shopify store owner credentials to create staff accounts
- Network access to the Shopify admin domain (e.g., *.myshopify.com)

## Detailed Attack Procedures

### Step 1: Create Limited Staff Account
procedure: [[procedures/Create-Limited-Staff-Account]]

**Objective**: Establish a compromised or test staff user with insufficient permissions to bypass authorization checks for app uninstallation.

**Instructions**: Log in to the Shopify admin panel as a store owner and navigate to Settings > Users and permissions. Create a new staff account, assigning only the 'Manage and install apps and channels' permission while explicitly excluding 'Develop apps'. Note the login credentials for subsequent authentication.

**Expected Output**: Staff account created successfully, visible in the users list with limited role.

**Success Indicators**:
- Staff user logs in without 'Develop apps' permission
- User can access app management sections but should not see developer tools

### Step 2: Identify Target App ID
procedure: [[procedures/Identify-Target-App-ID]]

**Objective**: Locate the global ID of the custom app to target for unauthorized uninstallation.

**Instructions**: Using the staff account, navigate to Apps in the Shopify admin. List installed custom apps and inspect their details (e.g., via browser dev tools or API queries) to extract the global ID in the format 'gid://shopify/App/XXXXXXX'. Alternatively, if known from prior installation, use that ID directly.

**Expected Output**: Global app ID retrieved, e.g., 'gid://shopify/App/6431859'.

**Success Indicators**:
- App ID confirmed and valid
- Staff user can view app details without errors

### Step 3: Execute GraphQL App Uninstall Mutation
procedure: [[procedures/Execute-GraphQL-App-Uninstall-Mutation]]

**Objective**: Send unauthorized GraphQL mutations to uninstall the target custom app, exploiting the permission check bypass.

**Instructions**: Authenticate as the limited staff user to obtain session cookies and CSRF token. Use tools like curl or Postman to send POST requests to /admin/internal/web/graphql/core. Start with the primary UninstallCustomApp mutation using [[commands/shopify-uninstall-custom-app-graphql]]:

```bash
curl -X POST 'https://example.myshopify.com/admin/internal/web/graphql/core?operation=AccountEdit&type=query' \
  -H 'Cookie: your_session_cookie' \
  -H 'X-Csrf-Token: your_csrf_token' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":"UninstallCustomApp","variables":{"appId":"gid://shopify/App/6431859"},"query":"mutation UninstallCustomApp($appId: ID!) { appUninstall(input: {id: $appId}) { app { id __typename } userErrors { field message __typename } __typename } }"}'
```

If successful, verify app removal in the admin panel. For alternatives, use [[commands/shopify-remove-channel-graphql]] or [[commands/shopify-app-uninstall-update-graphql]].

**Expected Output**: JSON response with {"data":{"appUninstall":{"app":{"id":"gid://shopify/App/6431859","__typename":"App"},"userErrors":[]}}}

**Success Indicators**:
- No userErrors in response
- Target app disappears from installed apps list
- Store functionality tied to the app is disrupted

## Attack Chain Summary

### Key Achievements

1. Bypassed 'Develop apps' permission requirement using limited staff role
2. Successfully uninstalled custom app via multiple GraphQL mutation paths
3. Demonstrated low-severity integrity impact on store operations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
