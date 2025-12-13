---
data: POST /v2/auth HTTP/1.1
tags:
  - api-auth
  - session-takeover
type: command
executor: http
platforms:
  - Web
id: ba00ef33-582d-466e-a54f-d398dde0ef26
created_at: '2025-12-13T09:01:26.124Z'
updated_at: '2025-12-13T09:01:26.124Z'
verified: false
validated: true
submitted: true
---
# POST Auth

## Command

```http
POST /v2/auth HTTP/1.1
```

## Description

Performs login, intercepted to swap with victim's token for takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Body contains auth data | No |

## Examples

### Basic Usage

```http
POST /v2/auth HTTP/1.1
```

## Expected Output

Login response, modified for impersonation.

## Related

- [[procedures/Perform-Account-Takeover-with-Stolen-Tokens]]
