---
tags:
  - token-capture
  - mobile-interception
  - credentials
type: procedure
tools:
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:01.793Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Credentials In Files]]'
id: ea68758c-0d56-45fc-bf8d-24b8920236c0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Capture-Access-Token-from-Mobile-Session

## Summary

This procedure intercepts and extracts the authentication token from Shopify Mobile app traffic, enabling its reuse for unauthorized API access despite limited permissions.

## Description

Shopify's mobile app uses bearer tokens for API communication, which can be captured via network proxies. This targets the vulnerability where mobile tokens bypass web authorization models. Prerequisites include a proxy setup on the device (e.g., via VPN or rooted access). Outcomes include a reusable token for API exploitation.

## Requirements

1. Proxy tool like mitmproxy installed and configured on the device/network
2. Active mobile app session from limited-access login
3. Knowledge of Shopify API endpoints (e.g., admin.shopify.com)

## Defense

Defensive measures and detection strategies:

- Use certificate pinning in mobile apps to block proxy interception
- Rotate tokens frequently and bind to device fingerprints
- Log and alert on token usage from non-mobile user agents

## Objectives

1. Intercept API requests during app usage
2. Extract bearer token from headers
3. Validate token viability for API calls

## Instructions

### Step 1: Setup Proxy

**Context**: Configure interception for mobile traffic.

Install and run [[tools/mitmproxy]] on a connected machine or device. Set the mobile device's Wi-Fi proxy to the mitmproxy IP/port (e.g., 8080). Install the mitmproxy CA certificate on the device to decrypt HTTPS.

### Step 2: Trigger and Capture Token

**Context**: Generate traffic to expose the token.

In the Shopify app, perform actions like refreshing the dashboard or viewing orders. Filter mitmproxy logs for requests to *.myshopify.com/admin/api. Locate the 'X-Shopify-Access-Token' header and copy the value.

**Expected Output**: Token string (e.g., 'shpat_xxxxxxxxxxxxxxxx').

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files]]

## Commands Used


## Tools Used

- [[tools/mitmproxy]]

## Tags

- [[token-extraction]]
- [[proxy-interception]]
- [[mobile]]
