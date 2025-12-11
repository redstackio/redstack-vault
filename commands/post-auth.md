---
data: POST /v2/auth
tags:
  - auth
  - session-takeover
type: command
executor: bash
platforms:
  - Web
id: a599c7cc-616a-4d7c-9709-977ccc623686
created_at: '2025-12-11T06:10:24.190Z'
updated_at: '2025-12-11T06:10:24.190Z'
verified: false
validated: true
submitted: true
---
# post-auth

## Command

```bash
POST /v2/auth
```

## Description

Performs authentication, intercepted to swap tokens for session takeover, used in session takeover by modifying response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
POST /v2/auth
```

## Expected Output

Authentication response with Access-Token/UserID.

## Related

- [[procedures/Perform-Session-Takeover-by-Token-Swapping]]
