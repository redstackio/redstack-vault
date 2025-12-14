---
id: uuid-curl-test
data: >-
  curl
  "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort="
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.914Z'
verified: false
validated: true
submitted: true
---
# curl-api-test

## Command

```bash
curl "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort="
```

## Description

Sends a baseline GET request to the Atavist API endpoint to test normal behavior and confirm parameter acceptance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full endpoint with query parameters | Yes |

## Examples

### Basic Usage

```bash
curl "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort="
```

### Advanced Usage

Add -v for verbose output:

```bash
curl -v "https://docs.atavist.com/reader_api/stories.php?limit=10&offset=20&organization_id=88822&search=0&sort="
```

## Expected Output

JSON response with an array of story objects, e.g., {"stories": [...]}, returned in under 1 second.

## Related

- [[commands/curl-sleep-payload]]
