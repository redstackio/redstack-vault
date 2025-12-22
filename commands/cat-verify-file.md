---
data: cat /tmp/vakzz
tags:
  - file-read
  - verification
type: command
executor: bash
platforms:
  - Linux
id: 6527a19f-22e5-481d-a145-b7b7ee63499d
created_at: '2025-12-11T06:10:40.396Z'
updated_at: '2025-12-11T06:10:40.396Z'
verified: false
validated: true
submitted: true
---
# cat-verify-file

## Command

```bash
cat /tmp/vakzz
```

## Description

Reads the contents of a file to verify successful command execution on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/vakzz` | File path | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/vakzz
```

## Expected Output

'vakzz was here'

## Related

- [[commands/curl-send-malicious-cookie]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
