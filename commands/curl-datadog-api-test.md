---
data: >-
  curl -X GET "https://api.datadoghq.com/api/v1/sites" -H "DD-API-KEY:
  <extracted_api_key>" -H "DD-APPLICATION-KEY: <extracted_app_key>"
tags:
  - api-testing
  - datadog
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.262Z'
id: bbd579c2-f74e-4cf2-9832-834c439dd104
verified: false
validated: true
submitted: true
---
# curl-datadog-api-test

## Command

```bash
curl -X GET "https://api.datadoghq.com/api/v1/sites" -H "DD-API-KEY: <extracted_api_key>" -H "DD-APPLICATION-KEY: <extracted_app_key>"
```

## Description

This command tests read access to a Datadog instance using exposed API and application keys by querying the sites endpoint. Use it to validate unauthorized access in a vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://api.datadoghq.com/api/v1/sites` | Datadog API endpoint for sites | Yes |
| `-H "DD-API-KEY: <key>"` | Header with API key for authentication | Yes |
| `-H "DD-APPLICATION-KEY: <key>"` | Header with application key for app access | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.datadoghq.com/api/v1/sites" -H "DD-API-KEY: aa123..." -H "DD-APPLICATION-KEY: app456..."
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X GET "https://api.datadoghq.com/api/v1/sites" -H "DD-API-KEY: aa123..." -H "DD-APPLICATION-KEY: app456..."
```

## Expected Output

On success: HTTP 200 with JSON like {"sites": [{"name": "example-site"}]}. On failure: 401 Unauthorized if keys are invalid.

## Related

- [[Related Procedure: Validate-Unauthorized-Access-Using-Exposed-Datadog-Keys]]
