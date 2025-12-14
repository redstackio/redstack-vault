---
id: proc-modify-order-id-instacart
tags:
  - authorization-bypass
  - idor
  - parameter-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile (iOS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:57.167Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Modify Order Delivery ID to Access Unauthorized Order Data

## Summary

This procedure exploits an authorization bypass by altering the order_delivery_id parameter in the Instacart API request, allowing access to other users' private chat logs, order details, and Firebase tokens.

## Description

The /api/v2/order_deliveries/{order_delivery_id}/order_change_logs endpoint fails to validate the requesting user's permissions for the specified ID, enabling IDOR-style attacks. Using an intercepted request from the user's own order, replace the ID with another (e.g., obtained from app enumeration or prior leaks) to disclose sensitive data like chat messages between buyers, shoppers, and drivers, product names, order times, and Firebase tokens.

## Requirements

1. Intercepted baseline request from Step 1 (authenticated session).
2. Knowledge of another order_delivery_id (e.g., 261972220, potentially from app UI or other sources).
3. Burp Suite Repeater or similar tool for request modification.
4. Stable proxy connection to the API host www.instacart.com.

## Defense

Defensive measures and detection strategies:

- Implement server-side permission checks tying order IDs to user accounts.
- Rate-limit API requests by user and monitor for ID pattern anomalies.
- Enable logging of accessed order IDs and alert on cross-user access attempts.

## Objectives

1. Bypass authorization to retrieve unauthorized order data.
2. Expose private communications and details.
3. Leak tokens for potential chained attacks.

## Instructions

### Step 1: Prepare Modified Request

**Context**: Use the intercepted request as a template and alter the order_delivery_id.

**Instructions**: In Burp Repeater, paste the original GET request. Change the path from /api/v2/order_deliveries/261932226/order_change_logs to /api/v2/order_deliveries/261972220/order_change_logs. Preserve all headers, including Authorization.

No command; modify directly in Burp's request editor.

> Ensure the request remains authenticated; forward to send.

### Step 2: Send and Analyze Response

**Context**: Execute the modified request and review for successful data disclosure.

**Instructions**: Click 'Send' in Burp Repeater. Inspect the JSON response body for chat messages, order changes, product details, and any Firebase-related tokens.

> Expected output: 200 OK with JSON like {"logs": [{"message": "Chat content", "timestamp": "..."}], "firebase_token": "xy8TcFsDZiKm1JwnqqFp"}—no 403 or auth error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authorization-bypass]]
- [[idor]]
