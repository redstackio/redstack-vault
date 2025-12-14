---
id: cmd-uuid-4
data: >-
  curl https://hackyholidays.h1ctf.com/swag-shop/api/sessions | jq -r
  '.sessions[]' | base64 -d | jq
tags:
  - json
  - decode
type: command
output: Sessions with UUIDs.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.485Z'
verified: false
validated: true
submitted: true
---
# Curl Decode Sessions Jq

## Command

```bash
curl https://hackyholidays.h1ctf.com/swag-shop/api/sessions | jq -r '.sessions[]' | base64 -d | jq
```

## Description

Fetches and decodes base64 sessions to extract UUIDs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Sessions endpoint | Yes |

## Examples

### Basic Usage

```bash
curl api/sessions | jq ...
```

## Expected Output

Parsed JSON with UUIDs.

## Related

- [[procedures/Fuzz-API-Endpoints-and-Extract-UUID-for-IDOR]]
