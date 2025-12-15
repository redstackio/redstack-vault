---
id: proc-intercept-graphql-request
tags:
  - interception
  - graphql
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.457Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-GraphQL-Notification-Request

## Summary

This procedure triggers a legitimate GraphQL request in the Shopify dashboard and intercepts it using browser tools, capturing the payload for modification to exploit authorization flaws.

## Description

By clicking the notification bell in the upper right of the dashboard, a GraphQL POST request is sent to https://partners.shopify.com/:id/api/graphql. Interception via dev tools allows pausing and inspection, revealing the endpoint vulnerable to payload tampering for unauthorized data access.

## Requirements

1. Active staff session in Shopify dashboard
2. Browser with dev tools (e.g., Chrome F12 > Network tab)
3. Optional: Proxy like Burp Suite for advanced control

## Defense

Defensive measures and detection strategies:

- Implement request signing or CSRF tokens on GraphQL endpoints
- Monitor for anomalous GraphQL queries from low-priv sessions
- Rate-limit API requests per user role

## Objectives

1. Trigger and capture the notification GraphQL request
2. Identify the organization ID in the URL
3. Prepare payload for exploitation

## Instructions

### Step 1: Trigger Request

**Context**: Initiate the GraphQL call via UI interaction.

Click the notification bell in the dashboard's upper right corner.

> This sends a POST to the GraphQL endpoint.

### Step 2: Intercept in Dev Tools

**Context**: Capture the request for analysis.

Open browser dev tools (F12), go to Network tab, filter for XHR/Fetch, and locate the request to https://partners.shopify.com/:id/api/graphql.

> Request details including headers, body, and :id are visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[interception]]
- [[graphql]]
- [[notification-request]]
