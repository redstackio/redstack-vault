---
data: 'curl https://gitlab.com/api/v4/projects/PROJECT_ID/import'
tags:
  - api
  - query
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 6abab995-f216-45ad-98ca-31a8b455484d
created_at: '2025-12-11T03:47:56.774Z'
updated_at: '2025-12-11T03:47:56.774Z'
verified: false
validated: true
submitted: true
---
# curl-api-query

## Command

```bash
curl https://gitlab.com/api/v4/projects/PROJECT_ID/import
```

## Description

This command sends a GET request to the GitLab import API endpoint to retrieve import status and leaked data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `PROJECT_ID` | ID of the imported project | Yes |

## Examples

### Basic Usage

```bash
curl https://gitlab.com/api/v4/projects/12345/import
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer TOKEN" https://gitlab.com/api/v4/projects/12345/import
```

## Expected Output

JSON response containing import status and up to 250 bytes of leaked file data.

## Related

- [[procedures/Query-Import-API-Endpoint]]
