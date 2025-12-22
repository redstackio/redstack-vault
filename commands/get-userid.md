---
data: GET /v2/tabbed/home HTTP/1.1
tags:
  - api-query
  - userid-retrieval
type: command
executor: bash
platforms:
  - Web
id: 4669fc70-b832-4d65-8c26-a7756175f493
created_at: '2025-12-11T06:10:24.223Z'
updated_at: '2025-12-11T06:10:24.223Z'
verified: false
validated: true
submitted: true
---
# get-userid

## Command

```bash
GET /v2/tabbed/home HTTP/1.1
```

## Description

Retrieves UserID using stolen Access-Token, used post-exploitation to gather UserID from stolen token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
GET /v2/tabbed/home HTTP/1.1
```

## Expected Output

Response containing UserID.

## Related

- [[procedures/Retrieve-UserID-and-PII-with-Stolen-Token]]
- [[commands/get-userdetails]]
