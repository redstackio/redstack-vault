---
id: proc-uuid-001
name: Access-Zomato-Gold-Payment-Success-Endpoint
tags:
  - idor
  - web
  - access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-known-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.705Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Zomato-Gold-Payment-Success-Endpoint

## Summary

This procedure accesses the Zomato Gold payment success endpoint with known subscription_id and user_id parameters to observe normal behavior and establish a baseline for IDOR exploitation.

## Description

In the context of testing the Zomato Gold service, this step involves sending a GET request to the payment success endpoint using valid parameters from an authenticated or known session. It confirms the endpoint's response format, which includes subscription details, and sets the stage for parameter manipulation to exploit IDOR. No authorization checks are performed, making it vulnerable to unauthorized access.

## Requirements

1. Network access to www.zomato.com
2. Known valid subscription_id and user_id (from own account)
3. curl or browser/Burp Suite for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks on subscription endpoints
- Log and monitor unusual parameter values in requests
- Rate-limit requests to payment endpoints

## Objectives

1. Establish baseline response from the endpoint
2. Verify normal subscription details display
3. Identify response structure for exploitation

## Instructions

### Step 1: Send Request with Known Parameters

**Context**: Use a tool like curl to mimic browser access and observe the response.

**Command** ([[commands/curl-access-known-endpoint]]):
```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=██████████&user_id=█████████" -i
```

> This command sends a GET request and displays headers. Expected output includes HTTP 200 with JSON or HTML containing subscription info.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-known-endpoint]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- web-access
