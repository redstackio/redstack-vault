---
id: cmd-uuid-2
data: cat /tmp/file
tags:
  - verification
type: command
output: |-
  commit f00f9538d29b176e9dfb2eb1bfe1eab190cad3d9
  Author: Administrator <admin@example.com>
  Date: Wed Jul 24 13:08:51 2019 +0000

   controlled content
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.336Z'
verified: false
validated: true
submitted: true
---
# cat-tmp-file

## Command

```bash
cat /tmp/file
```

## Description

Displays the contents of the overwritten /tmp/file to verify the command injection payload from git log.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/file | Path to the test file | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/file
```

## Expected Output

Commit hash, author, date, and controlled commit message.

## Related

- [[Related Procedure: Exploit-Search-API-Command-Injection]]
