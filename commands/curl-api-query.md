---
data: 'curl ''https://cortex-ingest.shopifycloud.com/api/v1/query?query=up'''
tags:
  - api
  - query
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.342Z'
id: 34871d8c-35cd-4784-bd83-9c99d5c3dc9a
verified: false
validated: true
submitted: true
---
# curl-api-query

## Command

```bash
curl 'https://cortex-ingest.shopifycloud.com/api/v1/query?query=up'
```

## Description

Performs a basic PromQL query on the Cortex API to retrieve metrics data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `?query=up` | PromQL query parameter | Yes |
| `https://.../api/v1/query` | API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl 'https://cortex-ingest.shopifycloud.com/api/v1/query?query=up'
```

### Advanced Usage

```bash
curl 'https://cortex-ingest.shopifycloud.com/api/v1/query?query=up[5m]' -H 'X-Scope-OrgID: tenant1'
```

## Expected Output

{"status":"success","data":{"resultType":"vector","result":[{"metric":{},"value":[timestamp,"1"]}]}}

## Related

- [[Related Procedure]]
