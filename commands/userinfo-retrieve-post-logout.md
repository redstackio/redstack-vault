---
data: >-
  curl -X GET https://accounts.shopify.com/oauth/userinfo -H "Authorization:
  Bearer [tokenA]"
tags:
  - userinfo
  - post-logout
type: command
output: >-
  HTTP/1.1 200 OK
  {"sub":"...","email":"r...@gmail.com","email_verified":true,"family_name":"Doe","given_name":"John","locale":"en","name":"John
  Doe","nickname":"r****","updated_at":1619245470,"zoneinfo":"*****","tfa_enabled":false}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.057Z'
id: 5655a28d-4ced-490b-9c69-6078e9ad1223
verified: false
validated: true
submitted: true
---
# userinfo-retrieve-post-logout

## Command

```bash
curl -X GET https://accounts.shopify.com/oauth/userinfo -H "Authorization: Bearer [tokenA]"
```

## Description

Retrieves userinfo after logout to verify persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Authorization` | Bearer tokenA | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

User data, indicating validity.

## Related

- [[Related Procedure: Verify-Persistent-Access-Token-Post-Logout]]
