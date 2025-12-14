---
id: cmd-uuid-3
data: 'scout url -s https://hackyholidays.h1ctf.com/swag-shop/api'
tags:
  - fuzzing
type: command
output: Discovered /user and /sessions endpoints.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.489Z'
verified: false
validated: true
submitted: true
---
# Scout Fuzz Api Endpoints

## Command

```bash
scout url -s https://hackyholidays.h1ctf.com/swag-shop/api
```

## Description

Fuzzes API base URL to discover hidden endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent mode | No |
| url | Target API | Yes |

## Examples

### Basic Usage

```bash
scout url https://api.example.com
```

## Expected Output

List of endpoints.

## Related

- [[procedures/Fuzz-API-Endpoints-and-Extract-UUID-for-IDOR]]
