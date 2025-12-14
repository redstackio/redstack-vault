---
data: >-
  curl -X GET https://accounts.shopify.com/oauth/userinfo -H "Accept-Encoding:
  gzip, deflate" -H "Authorization: Bearer [tokenA]"
tags:
  - userinfo
  - api
type: command
output: >-
  {"sub":"...","email":".....@gmail.com","email_verified":true,"family_name":"Doe","given_name":"....","locale":"en","name":"....
  ...","nickname":".....","updated_at":.....,"zoneinfo":"....","tfa_enabled":false}
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.089Z'
id: c6be4736-1252-4678-8d3c-01f16235bb54
verified: false
validated: true
submitted: true
---
# userinfo-retrieve

## Command

```bash
curl -X GET https://accounts.shopify.com/oauth/userinfo -H "Accept-Encoding: gzip, deflate" -H "Authorization: Bearer [tokenA]"
```

## Description

Fetches user profile using access_token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Authorization` | Bearer tokenA | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

User data JSON.

## Related

- [[Related Procedure: Perform-Authenticated-Actions-with-Primary-Token]]
