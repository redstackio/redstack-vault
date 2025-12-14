---
id: proc-omise-anon-status-001
tags:
  - access-control
  - api
  - payment
  - omise
  - unauthenticated
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-omise-payment-status]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.773Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Omise-Payment-Status-Anonymously

## Summary

This procedure exploits improper access controls in the Omise API to anonymously retrieve the status of payment transactions, such as whether they have been processed, without any authentication. It targets the /payments/{payment_id}/status endpoint on api.omise.co, allowing attackers to view sensitive transaction details that should be restricted to authorized users.

## Description

The Omise Payment API, used for processing online payments, fails to enforce authentication on its payment status endpoint. By sending a simple unauthenticated GET request over HTTP/2 with standard headers, an attacker can query any payment ID's status. This vulnerability was reported via HackerOne (Report #1546726) and enables reconnaissance on payment flows or potential follow-on attacks like fraud. The procedure assumes the attacker has a valid payment ID, which could be obtained from public sources, error messages, or enumeration. Expected outcomes include receiving JSON data confirming payment processing status, exposing details to unauthorized parties.

## Requirements

1. Network access to https://api.omise.co (public internet connectivity)
2. A valid payment ID (e.g., paym_test_5rjz482tky43reoil9f from testing or leaks)
3. HTTP client like curl supporting HTTP/2
4. No account credentials or prior access needed

## Defense

Defensive measures and detection strategies:

- Implement API authentication (e.g., API keys or OAuth) on all sensitive endpoints
- Use rate limiting and IP whitelisting to restrict anonymous queries
- Monitor API logs for unauthenticated access patterns to /payments/{id}/status
- Validate and sanitize payment IDs to prevent enumeration

## Objectives

1. Gain unauthorized access to payment transaction status
2. Expose processing details for potential fraud or reconnaissance
3. Demonstrate the impact of missing access controls in financial APIs

## Instructions

### Step 1: Send Unauthenticated GET Request to Payment Status Endpoint

**Context**: This step directly queries the vulnerable endpoint without login, mimicking a browser request to retrieve the payment status.

**Command** ([[commands/get-omise-payment-status]]):
```bash
curl -X GET "https://api.omise.co/payments/paym_test_5rjz482tky43reoil9f/status" \
  -H "Sec-Ch-Ua: \"\" " \
  -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" \
  -H "Accept: */*" \
  -H "Referer: https://api.omise.co/" \
  --http2
```

> This command sends a GET request to the specified endpoint with browser-like headers over HTTP/2. A successful response will return HTTP/2 200 OK with Content-Type: application/json and a body like {"processed":true}, indicating the payment status without any auth requirement.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/get-omise-payment-status]]

## Tools Used


## Tags

- access-control
- api
- payment
- omise
- unauthenticated
