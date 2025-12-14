---
id: p-intercept-token
name: Intercept-Access-Token-via-Developer-Tools
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.718Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials In Files]]'
tags:
  - shopify
  - token-leak
  - graphql
  - information-disclosure
commands: []
platforms:
  - Web
tools:
  - '[[tools/Browser-Developer-Tools]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---

# Intercept-Access-Token-via-Developer-Tools

## Summary

This procedure uses browser developer tools to monitor and extract a sensitive Shopify access token from a GraphQL response in the Flow app, enabling subsequent unauthorized API access.

## Description

While authenticated as the staff user in the Flow app, navigating to the Connectors tab triggers a GraphQL query to https://flow.shopifycloud.com/graphql for shop information. The response includes the unencrypted 'shopifyToken', which provides app-level access to the store's REST API. This information disclosure vulnerability allows interception via network inspection tools. Prerequisites: Staff access to Flow app and developer tools enabled. Outcomes: Captured token usable for persistent exploitation.

## Requirements

1. Staff login to Shopify admin and Flow app
2. Browser with developer tools (e.g., Chrome DevTools)
3. Network access to Shopify domains

## Defense

Defensive measures and detection strategies:

- Encrypt or omit sensitive tokens from client-side responses
- Implement API access controls and token rotation on staff changes
- Monitor for anomalous GraphQL queries in app logs

## Objectives

1. Capture the leaked access token
2. Expose unsecured credentials in transit
3. Enable data collection via API

## Instructions

### Step 1: Open Developer Tools

**Context**: Prepare to inspect network traffic.

In the browser, right-click and select 'Inspect' or press F12 to open DevTools. Switch to the 'Network' tab.

> Expected output: Network panel ready to capture requests.

### Step 2: Navigate to Connectors Tab

**Context**: Trigger the vulnerable GraphQL query.

As staff user, in the Flow app, go to https://[store].myshopify.com/admin/apps/flow/connectors.

> This sends a POST to https://flow.shopifycloud.com/graphql with 'shopInfo' in payload.

### Step 3: Filter and Inspect Request

**Context**: Locate the specific GraphQL response.

In Network tab, filter for 'graphql' or 'flow.shopifycloud.com'. Click the shopInfo request and view the Response tab.

> Expected output: JSON with 'shopifyToken' field visible.

### Step 4: Extract Token

**Context**: Copy the token for later use.

From the response JSON, copy the value of 'shopifyToken' (e.g., a long string starting with 'shpat_').

> Success: Token saved securely for API testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[shopify]]
- [[token-leak]]
- [[graphql]]
- [[information-disclosure]]
