---
tags:
  - intercept
  - http-proxy
  - apns
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:09.574Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 12f64b53-26f4-4d0f-9707-a77250109a1e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-Mobile-Device-Registration-Request

## Summary

This procedure captures the HTTP POST request to Shopify's `/admin/mobile_devices.json` endpoint during device registration, extracting the APNS token for later replay.

## Description

Following authentication in the Shopify mobile app, the app sends a POST request containing the device's APNS token to register for order notifications. By intercepting this with a proxy, attackers can save the request details, including headers, body (with token), and session cookies, for unauthorized replay after permission changes. This targets iOS/Android apps communicating with Shopify's API over HTTPS.

## Requirements

1. Active proxy session from privileged login
2. Burp Suite or equivalent HTTP interceptor
3. Device trust for proxy CA certificate

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning in the mobile app to prevent proxy interception
- Log and alert on unusual API request patterns or proxy-detected traffic

## Objectives

1. Capture the full registration request
2. Extract APNS token and session data
3. Enable request replay

## Instructions

### Step 1: Monitor Proxy Traffic

**Context**: Position the proxy to capture app-to-server communication.

In Burp Suite, navigate to the Proxy tab and ensure the mobile device's traffic is routed through it. Filter for requests to `*.shopify.com`.

### Step 2: Trigger and Intercept Request

**Context**: Induce the API call and block for inspection.

Perform any action in the app that confirms device registration (e.g., navigate to notifications). When the POST to `/admin/mobile_devices.json` appears, intercept it (set to 'Intercept is on').

**Expected Output**: Request details visible, including JSON body like `{"apns_token": "..."}`.

Copy the request to a file or repeater for later use.

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

- intercept
- proxy
- shopify-api
