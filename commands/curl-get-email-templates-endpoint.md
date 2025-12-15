---
data: >-
  curl -X GET "https://target/api/1_0/EmailTemplates" -H "Accept:
  application/json"
tags:
  - access
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.587Z'
id: c593387a-201a-4740-ad28-c34c4c7f1466
verified: false
validated: true
submitted: true
---
# curl-get-email-templates-endpoint

## Command

```bash
curl -X GET "https://target/api/1_0/EmailTemplates" -H "Accept: application/json"
```

## Description

Retrieves email templates via unauthenticated GET to assess exposure and manipulation potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `"https://target/api/1_0/EmailTemplates"` | Templates endpoint | Yes |
| `-H "Accept: application/json"` | JSON response header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/api/1_0/EmailTemplates" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X POST "https://example.com/api/1_0/EmailTemplates" -H "Content-Type: application/json" -d '{"test":"data"}'
```

## Expected Output

JSON list of templates.

## Related

- [[Related Procedure]]
