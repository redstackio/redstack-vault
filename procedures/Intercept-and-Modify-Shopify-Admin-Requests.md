---
id: 123e4567-e89b-12d3-a456-426614174001
name: Intercept-and-Modify-Shopify-Admin-Requests
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.831Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - intercept
  - proxy
  - shopify
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Intercept-and-Modify-Shopify-Admin-Requests

## Summary

This procedure captures legitimate Shopify Admin requests using a proxy tool and modifies them to target the vulnerable GraphQL endpoint, enabling further exploitation with low-privilege credentials.

## Description

In the context of Shopify's Admin interface, low-privilege staff accounts (e.g., marketing permissions) can access internal endpoints due to missing checks. This step involves proxying traffic to alter requests, setting up for GraphQL mutations that install and activate workflows without required apps permissions.

## Requirements

1. Burp Suite installed and configured as a proxy
2. Valid Shopify staff login session (low-privilege)
3. Network access to Shopify Admin domain

## Defense

Defensive measures and detection strategies:

- Implement strict proxy detection (e.g., TLS fingerprinting)
- Monitor for unusual GraphQL introspection queries
- Enforce role-based access controls on internal endpoints

## Objectives

1. Gain control over Admin requests to pivot to vulnerable endpoint
2. Preserve session authenticity for unauthorized actions
3. Set stage for mutation-based exploitation

## Instructions

### Step 1: Capture Legitimate Request

**Context**: Intercept any POST request during normal Shopify Admin usage to obtain a base template.

**Instructions**: Configure browser proxy to Burp Suite and navigate Shopify Admin. Capture a POST request and forward to Repeater.

> No specific command; use Burp UI to intercept and forward.

### Step 2: Modify Endpoint and Headers

**Context**: Alter the request to hit the GraphQL flow endpoint with proper session headers.

**Instructions**: In Burp Repeater, change path to POST /admin/internal/web/graphql/flow. Add headers: Cookie (session ID), X-Csrf-Token, Content-Type: application/json. Use marketing-permission account.

> Example modified request structure:
>
> POST /admin/internal/web/graphql/flow HTTP/2
> Host: example.myshopify.com
> Cookie: _secure_admin_session_id=abc123
> X-Csrf-Token: token123
> Content-Type: application/json
>
> {}

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[shopify]]
