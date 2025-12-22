---
data: >-
  ffuf -u "https://api.bountypay.h1ctf.com/api/FUZZ" -H "X-Token:
  8e9998ee3137ca9ade8f372739f062c1" -w
  ./SecLists/Discovery/Web-Content/common.txt
tags:
  - api
  - fuzzing
type: command
output: Discovery of /api/staff
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.957Z'
id: 859a66a5-d442-4ceb-ac85-c3e77b4fb6c7
verified: false
validated: true
submitted: true
---
# ffuf-api-fuzz

## Command

```bash
ffuf -u "https://api.bountypay.h1ctf.com/api/FUZZ" -H "X-Token: 8e9998ee3137ca9ade8f372739f062c1" -w ./SecLists/Discovery/Web-Content/common.txt
```

## Description

Fuzzes API endpoints with authentication header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Token header | Yes |

## Examples

Basic API fuzz.

## Expected Output

Endpoints like /staff.

## Related

- [[tools/ffuf]]
