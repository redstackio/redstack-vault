---
data: |-
  curl -s $TARGET | grep -i generator
  curl -s "$TARGET/wp-admin/admin-ajax.php?action=upload-errors"
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.040Z'
id: d4a7adea-0c72-4296-b9f5-ae16b147018c
verified: false
validated: true
submitted: true
---
# curl-check-wp

## Command

```bash
curl -s $TARGET | grep -i generator
curl -s "$TARGET/wp-admin/admin-ajax.php?action=upload-errors"
```

## Description

Checks a target URL for WordPress fingerprints and vulnerable SWFUpload endpoint using curl and grep.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$TARGET` | Target URL (e.g., https://blog.makerdao.com) | Yes |
| `-s` | Silent mode (no progress bar) | No |
| `grep -i generator` | Case-insensitive search for WordPress meta | No |

## Examples

### Basic Usage

```bash
TARGET=https://blog.makerdao.com
curl -s $TARGET | grep -i generator
```

### Advanced Usage

```bash
TARGET=https://blog.makerdao.com
curl -s "$TARGET/wp-admin/admin-ajax.php?action=upload-errors"
```

## Expected Output

WordPress meta tag like: <meta name="generator" content="WordPress 4.8" /> or 200 OK response from endpoint.

## Related

- [[Related Procedure]]
