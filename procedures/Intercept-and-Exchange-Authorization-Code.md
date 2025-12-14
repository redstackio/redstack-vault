---
tags:
  - code-interception
  - token-exchange
type: procedure
tools:
  - '[[tools/Shop-PRO-Malicious-App]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Android
  - iOS
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Adversary-in-the-Middle]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: d0e4c4f0-c3ea-43cd-b1aa-8a96e209e321
created_at: '2025-12-14T17:31:31.003Z'
updated_at: '2025-12-14T17:31:31.003Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Adversary-in-the-Middle]]'
---
# Intercept-and-Exchange-Authorization-Code

## Summary

This procedure captures the OAuth authorization code from the deep link in the malicious app and exchanges it for an access token to access Outlook emails or link via Shopify GraphQL.

## Description

The deep link URI contains the code (e.g., shopapp://callback?code=ABC123). The app parses it and sends a POST to Microsoft's token endpoint or Shopify's GraphQL to obtain persistent access, bypassing PKCE protections.

## Requirements

1. Malicious app receiving the deep link
2. Network access to OAuth endpoints
3. Client ID/secret from Shopify app (if needed for exchange)

## Defense

Defensive measures and detection strategies:

- Enforce PKCE and state parameters in OAuth
- Short-lived codes with binding to client
- Monitor token exchanges for anomalous IPs/devices

## Objectives

1. Extract code from URI
2. Exchange for access/refresh tokens
3. Gain read access to emails or account linkage

## Instructions

### Step 1: Parse Deep Link

**Context**: In the app's intent handler, extract the code parameter.

Use URL parsing to get ?code= value.

**Expected Output**: Code string isolated (e.g., "ABC123").

### Step 2: Exchange via Microsoft Endpoint

**Context**: POST to token endpoint.

Send: POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token with code, client_id, etc.

**Expected Output**: JSON with access_token.

### Step 3: Use Token or Link Account

**Context**: Access emails or mutate Shopify GraphQL.

For linkage: POST https://server.shop.app/graphql with LinkOutlookAccount mutation using code.

**Expected Output**: Successful API response, emails accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Shop-PRO-Malicious-App]]

## Tags

- [[code-interception]]
- [[token-exchange]]
