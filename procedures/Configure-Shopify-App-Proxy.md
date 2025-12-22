---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - shopify
  - app-proxy
  - configuration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.257Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Shopify-App-Proxy

## Summary

This procedure sets up a Shopify App Proxy by creating a private app and configuring proxy settings to route requests to an external backend, enabling testing of proxy behaviors like header injection.

## Description

Shopify's App Proxy allows apps to handle custom subpaths on a store. This configuration points the proxy to a mock backend, facilitating tests for misconfigurations in NGINX handling of upstream responses. Targets Shopify stores; requires admin access. Outcome: A functional proxy URL for triggering requests.

## Requirements

1. Shopify Partners account
2. Access to a test/development shop
3. Mock backend URL from prior setup

## Defense

Defensive measures and detection strategies:

- Restrict App Proxy configurations to trusted apps only
- Audit proxy URLs and subpaths regularly
- Implement rate limiting on proxy endpoints

## Objectives

1. Install private app on target shop
2. Set proxy to route to controlled backend
3. Enable subpath proxying for testing

## Instructions

### Step 1: Create Private App

**Context**: Generate a new app in Shopify Partners for proxy use.

Log in to Shopify Partners, create a new private application, and install it on the target shop via the app's installation URL.

> Expected output: App installed; note the API keys if needed, though not required for proxy setup.

### Step 2: Configure Proxy Settings

**Context**: Define the proxy route in the shop admin.

In the shop admin, go to Apps > Extensions > Online Store > App Proxy. Set Subpath prefix: 'a', Subpath: 'apps', Proxy URL: [mock URL from Step 1, e.g., https://run.mocky.io/v3/d7cdfcbc-6994-4f3b-a323-fe8377535507]. Save changes.

> Expected output: Proxy active; test by accessing https://{shop}.myshopify.com/a/apps (should hit mock).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- app-proxy
- configuration
