---
tags:
  - api-interception
  - transaction-history
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Mobile (iOS)
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:35.187Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b00e38cc-aafc-4e7a-adce-e2c2f4956233
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Capture-Recharge-Transaction-History-Request

## Summary

This procedure navigates the MyMTN NG app to the transaction history section, triggering and intercepting the POST request to /api/v2/rechargeTransactionHistory via proxy to analyze the payload structure.

## Description

The endpoint uses a JSON payload with customer_id (authenticated MSISDN), start_date, and end_date. Intercepting this reveals the exact format and allows preparation for modification. The request is sent over HTTP/2, and the response contains the user's own transaction data for validation.

## Requirements

1. Authenticated session in MyMTN NG app
2. Active proxy interception setup
3. Knowledge of date ranges for querying history

## Defense

Defensive measures and detection strategies:

- Log all API requests with client identifiers for anomaly detection
- Implement request signing or token validation per endpoint
- Monitor for proxy-intercepted traffic patterns in logs

## Objectives

1. Trigger the vulnerable API endpoint
2. Capture the request payload for analysis
3. Verify response with legitimate user data

## Instructions

### Step 1: Navigate to Transaction History

**Context**: Use the app UI to initiate the API call.

No command; app navigation.

> In the app, select 'Wallet' or 'History' > 'Recharge Transactions', choose a date range (e.g., last 30 days).

### Step 2: Intercept in Proxy

**Context**: Capture the outgoing request in Burp Suite.

No specific command; proxy action.

> The app sends POST to https://api.mymtn.com.ng/api/v2/rechargeTransactionHistory with headers including Authorization token. Drop or forward in Burp to inspect JSON: {"customer_id": "2347032233323", "start_date": "2023-09-01", "end_date": "2023-10-01"}.

### Step 3: Analyze Response

**Context**: Forward the request and review output.

No command.

> Response: Array of transactions with fields like rechargeDate, amountBefore, transactionId. Confirm it matches your own history.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api-interception
- transaction-history
