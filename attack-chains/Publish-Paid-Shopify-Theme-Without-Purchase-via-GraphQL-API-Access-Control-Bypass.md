---
id: ac-shopify-paid-theme-bypass-927567
tags:
  - shopify
  - graphql
  - access-control
  - api-abuse
  - bypass
  - unauthorized-access
type: attack_chain
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Shopify-Themes-for-Exploitation]]'
  - '[[procedures/Extract-Paid-Theme-ID-from-Shopify-Admin]]'
  - '[[procedures/Capture-Free-Theme-Publish-GraphQL-Request]]'
  - '[[procedures/Modify-and-Execute-Paid-Theme-Publish-Mutation]]'
  - '[[procedures/Verify-Paid-Theme-Publication-and-Access]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:29.101Z'
description: >-
  Exploits improper access controls in Shopify's GraphQL API to publish and gain
  effective ownership of paid themes without payment, allowing unauthorized
  editing and downloading of theme assets.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Publish Paid Shopify Theme Without Purchase via GraphQL API Access Control Bypass

Multi-stage attack chain exploiting improper authorization in Shopify's theme management GraphQL API to publish paid themes without purchase, granting unauthorized access to edit, rename, and download theme files. This leads to potential content theft, revenue loss for Shopify, and disclosure of proprietary theme assets.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Themes] --> B[Extract ID]
    B --> C[Capture Request]
    C --> D[Modify and Publish]
    D --> E[Verify Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Developer-Tools]]

### Target Environment

- Shopify merchant admin panel
- Active Shopify store account with theme management access
- No special ports; operates over HTTPS on web browser

### Initial Access Requirements

- Valid Shopify admin session (logged-in user)
- Network access to Shopify admin (https://yourshop.myshopify.com/admin)
- Browser with developer tools enabled (e.g., Chrome DevTools)

## Detailed Attack Procedures

### Step 1: Prepare Themes
procedure: [[procedures/Prepare-Shopify-Themes-for-Exploitation]]

**Objective**: Install and set up free and paid themes to prepare for ID extraction and request capture.

**Instructions**: Log in to the Shopify admin panel. Ensure the default theme is published. Install a free theme from the theme store, then install a paid theme without completing purchase (it installs as a demo).

**Expected Output**: Free and paid themes visible in the themes list.

**Success Indicators**:
- Default theme active
- Free theme installed
- Paid theme installed with 'Theme trial' badge

### Step 2: Extract Paid Theme ID
procedure: [[procedures/Extract-Paid-Theme-ID-from-Shopify-Admin]]

**Objective**: Obtain the GraphQL ID of the paid theme from the admin URL.

**Instructions**: In the Shopify admin themes page, click 'Customize' on the paid theme. The URL will show the theme ID in the format https://yourshop.myshopify.com/admin/themes/[theme_id]/editor. Copy the [theme_id] value.

**Expected Output**: Numeric theme ID (e.g., 1234567890).

**Success Indicators**:
- Theme ID extracted successfully
- ID in format gid://shopify/OnlineStoreTheme/[PAID_THEME_ID]

### Step 3: Capture Free Theme Publish Request
procedure: [[procedures/Capture-Free-Theme-Publish-GraphQL-Request]]

**Objective**: Publish the free theme to capture the legitimate GraphQL mutation request for later modification.

**Instructions**: Publish the free theme via the admin interface. Open Browser Developer Tools (Network tab), filter for XHR, and copy the POST request to /admin/online-store/admin/api/unversioned/graphql as a Fetch command.

**Expected Output**: JavaScript fetch code snippet with ThemePublishLegacy mutation.

**Success Indicators**:
- Free theme published
- Fetch request captured in console

### Step 4: Modify and Execute Paid Theme Publish Mutation
procedure: [[procedures/Modify-and-Execute-Paid-Theme-Publish-Mutation]]

**Objective**: Alter the captured request to target the paid theme ID and execute it to bypass purchase checks.

**Instructions**: In the browser console, paste the captured fetch code. Replace the free theme ID in the variables with the paid theme ID (gid://shopify/OnlineStoreTheme/[PAID_THEME_ID]). Execute the modified [[commands/theme-publish-graphql-mutation]].

```javascript
fetch("https://yourshop.myshopify.com/admin/online-store/admin/api/unversioned/graphql", {
  "headers": {
    "accept": "application/json",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-online-store-web": "1"
  },
  "referrerPolicy": "no-referrer",
  "body": "{\"operationName\":\"ThemePublishLegacy\",\"variables\":{\"id\":\"gid://shopify/OnlineStoreTheme/[PAID_THEME_ID]\"},\"query\":\"mutation ThemePublishLegacy($id: ID!) {\n  onlineStoreThemePublish(id: $id) {\n    theme {\n      id\n      __typename\n    }\n    userErrors {\n      field\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\"}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});"
```

**Expected Output**: JSON response showing successful publication without userErrors.

**Success Indicators**:
- No errors in response
- Paid theme targeted successfully

### Step 5: Verify Paid Theme Publication and Access
procedure: [[procedures/Verify-Paid-Theme-Publication-and-Access]]

**Objective**: Confirm the paid theme is published and accessible without purchase restrictions.

**Instructions**: Refresh the themes page in Shopify admin. Publish another theme (e.g., free one) and check the paid theme: it should lack the 'Theme trial' badge and allow renaming, editing, and downloading files.

**Expected Output**: Paid theme listed as active, with full management options enabled.

**Success Indicators**:
- Paid theme published and active
- Editing/downloading possible without purchase prompt
- No trial badge visible

## Attack Chain Summary

### Key Achievements

1. Bypassed purchase requirement for paid themes via API mutation abuse
2. Gained unauthorized ownership and access to paid theme files
3. Enabled potential theft of proprietary theme content and caused revenue impact to Shopify

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
