---
tags:
  - web
  - endpoint-access
  - order-viewing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-get-order-endpoint]]'
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1a2b9aec-2b0d-461c-b97b-bceb8ba43926
created_at: '2025-12-14T17:25:33.594Z'
updated_at: '2025-12-14T17:25:33.594Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Order-Viewing-Endpoint

## Summary

This procedure accesses the order viewing endpoint in the Bohemia Interactive store using an authenticated session to retrieve legitimate order details and inspect the URL structure for potential manipulation.

## Description

The order viewing endpoint at https://store.bistudio.com/order/{order_id}?confirmed=true allows authenticated users to view their purchase history. This step uses a known personal order ID to fetch data, confirming session validity and revealing the parameter format vulnerable to IDOR. It operates on the web platform and requires prior authentication.

## Requirements

1. Active session from authentication procedure
2. Known personal order ID (e.g., from account dashboard)
3. Curl or browser for HTTP GET requests

## Defense

Defensive measures and detection strategies:

- Enforce server-side ownership checks on order IDs
- Log and alert on access to non-owned resources
- Rate-limit endpoint requests to prevent enumeration

## Objectives

1. Retrieve personal order data
2. Identify the manipulable order_id parameter
3. Validate endpoint response format

## Instructions

### Step 1: Prepare Session

**Context**: Ensure cookies from login are available for the request.

**Command** ([[commands/curl-get-order-endpoint]]):
```bash
# Load session cookies
curl -b cookies.txt "https://store.bistudio.com/order/1003793?confirmed=true"
```

> Replace 1003793 with your order ID. Response includes order details.

### Step 2: Inspect Response

**Context**: Analyze the output to confirm access and note sensitive fields like IP.

**Command** ([[commands/curl-get-order-endpoint]]):
```bash
curl -b cookies.txt -v "https://store.bistudio.com/order/1003793?confirmed=true" > order_response.html
```

> Use -v for headers; save response for review.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-order-endpoint]]

## Tools Used


## Tags

- [[web]]
- [[endpoint-access]]
- [[order-viewing]]
