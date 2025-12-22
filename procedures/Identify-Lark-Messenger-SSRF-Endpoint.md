---
tags:
  - recon
  - ssrf
  - api-endpoint
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-endpoint-probe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:09.432Z'
sub_techniques: []
id: 5ac55130-794a-4c91-bfdf-1b04d747c36d
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Lark-Messenger-SSRF-Endpoint

## Summary

This reconnaissance procedure identifies the vulnerable messenger endpoint in Lark Suite by probing API documentation and testing for SSRF-prone parameters like URL inputs in message handling.

## Description

Lark Suite's messenger API allows sending messages with attachments or interactive elements that may process external URLs. Without proper validation, these can be abused for SSRF. This step involves API exploration to pinpoint the exact endpoint and confirm it accepts unsanitized inputs.

## Requirements

1. Lark Suite developer account for API access
2. Basic HTTP client for probing
3. API documentation access

## Defense

Defensive measures and detection strategies:

- Rate-limit API endpoints to prevent probing
- Log and alert on anomalous parameter values in requests
- Regularly audit API for input validation gaps

## Objectives

1. Locate the messenger send endpoint
2. Verify URL parameter acceptance
3. Confirm potential for SSRF exploitation

## Instructions

### Step 1: Probe API Endpoint

**Context**: Send a basic request to the messenger endpoint to check accessibility and response.

**Command** ([[commands/curl-endpoint-probe]]):
```bash
curl -X POST 'https://api.larksuite.com/open-apis/im/v1/messages?receive_id_type=user_id' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"receive_id": "test_user", "msg_type": "text", "content": "{\"text\":\"test\"}"}'
```

> Expected output: JSON success response indicating the endpoint is active and processes content.

### Step 2: Test for URL Input

**Context**: Modify the request to include a harmless external URL and observe if it's processed server-side.

**Command** ([[commands/curl-url-test]]):
```bash
curl -X POST 'https://api.larksuite.com/open-apis/im/v1/messages?receive_id_type=user_id' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"receive_id": "test_user", "msg_type": "interactive", "content": "{\"url\":\"https://example.com\"}"}'
```

> Expected output: No errors, confirming URL handling without validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-endpoint-probe]]
- [[commands/curl-url-test]]

## Tools Used


## Tags

- recon
- api-probing
- ssrf-identification
