---
id: proc-intercept-instacart-api-burp
tags:
  - api-interception
  - traffic-analysis
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile (iOS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.169Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept API Traffic with Burp Suite to Identify Chat Logs Endpoint

## Summary

This procedure uses Burp Suite to intercept and analyze HTTP traffic from the Instacart iOS mobile app, identifying the API endpoint for order delivery chat logs that lacks proper authorization checks.

## Description

In the context of testing the Instacart mobile app, this step involves proxying app traffic to capture requests triggered by user interactions, such as viewing chat logs on a past order. The endpoint /api/v2/order_deliveries/{order_delivery_id}/order_change_logs is revealed, setting up for parameter manipulation. Prerequisites include an authenticated app session and Burp Suite configured as a proxy on the testing device.

## Requirements

1. Instacart iOS app installed with a valid authenticated account and at least one past order.
2. Burp Suite running with proxy listener enabled (default port 8080).
3. iOS device configured to route traffic through Burp proxy (e.g., via Wi-Fi settings or manual proxy setup).
4. CA certificate installed on iOS for HTTPS interception.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or certificate installations on mobile devices.
- Implement app-level traffic encryption or pinning to prevent interception.
- Log and alert on API requests from non-standard user agents or IP ranges.

## Objectives

1. Identify the vulnerable API endpoint structure.
2. Confirm the presence of manipulable parameters like order_delivery_id.
3. Establish baseline for authenticated request format.

## Instructions

### Step 1: Configure Proxy and Intercept Traffic

**Context**: Set up Burp Suite to capture mobile app requests and trigger the chat logs feature.

**Instructions**: Launch Burp Suite, ensure the proxy is listening on 127.0.0.1:8080. On the iOS device, set Wi-Fi proxy to the Burp host/IP and port. Install Burp's CA certificate in iOS settings. Open the Instacart app, navigate to a past order, and tap 'View Chat Logs' to intercept the request.

No specific command; use Burp's Intercept tab to capture and view the GET request details.

> The intercepted request will show: GET /api/v2/order_deliveries/261932226/order_change_logs HTTP/1.1 Host: www.instacart.com. Forward the request to proceed.

### Step 2: Analyze Request and Endpoint

**Context**: Examine the captured request to document the endpoint and parameters.

**Instructions**: In Burp's Proxy > HTTP history or Repeater, inspect the URL path, headers (e.g., Authorization Bearer token), and confirm it's a GET to the order_change_logs endpoint.

> Expected output: Full request details confirming the endpoint lacks explicit permission headers for the order ID.

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

- [[api-interception]]
- [[traffic-analysis]]
