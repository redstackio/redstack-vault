---
id: proc-uuid-001
tags:
  - privilege-escalation
  - graphql
  - beta-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:20.159Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Enable POS Staff Feature via GraphQL Response Modification

## Summary

This procedure bypasses a client-side beta flag in Shopify's GraphQL API to enable POS staff management features in environments where they are disabled, such as a sandbox, by intercepting and modifying the API response using a proxy tool.

## Description

In Shopify Plus Partner Sandbox environments, POS staff features are disabled by default via a 'staffPermissionsBetaFlag' set to false in the GraphQL Overview query response. This procedure exploits the lack of server-side validation by tampering with the client-side response to flip the flag to true, granting access to the feature. It sets the stage for further unauthorized actions like creating and deleting POS staff. The target is the /graphql-proxy/admin endpoint, and it requires an authenticated admin session.

## Requirements

1. Authenticated admin access to Shopify admin panel
2. Burp Suite or similar proxy for intercepting HTTP traffic
3. Network access to Shopify's GraphQL endpoints
4. Knowledge of GraphQL response structure

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for all feature flags to prevent client-side bypasses
- Monitor for anomalous GraphQL responses or proxy-intercepted traffic in logs
- Enforce strict Content-Security-Policy (CSP) to limit tampering capabilities

## Objectives

1. Enable disabled POS staff management UI
2. Bypass beta feature restrictions without server authentication
3. Prepare for unauthorized staff operations

## Instructions

### Step 1: Access POS App and Intercept GraphQL Query

**Context**: Start an admin session and navigate to the POS app to trigger the Overview query, then intercept it to identify the beta flag.

No specific command; use browser navigation:

Navigate to the Shopify POS app in the admin panel.

> The POST request to /graphql-proxy/admin includes the Overview query fetching shop features. The response contains '"staffPermissionsBetaFlag": false'.

### Step 2: Configure Proxy for Response Modification

**Context**: Set up Burp Suite to automatically modify the response body and enable the flag.

Use Burp Suite Match and Replace:

In Burp Suite, go to Proxy > Options > Match and Replace, add a rule to replace '"staffPermissionsBetaFlag":false' with '"staffPermissionsBetaFlag":true' in the response body for the GraphQL endpoint.

> Upon interception, the modified response tricks the client into enabling the feature.

### Step 3: Refresh and Verify Access

**Context**: Apply the modification and confirm the UI update.

Refresh the POS app page.

> The UI now displays 'Manage POS staff' due to the altered flag.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- privilege-escalation
- graphql
- beta-bypass
