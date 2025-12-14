---
id: cmd-mv-rename
data: mv picture.png picture.php
tags:
  - file-management
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.387Z'
verified: false
validated: true
submitted: true
---
# mv-rename-file

## Command

```bash
mv picture.png picture.php
```

## Description

Renames a file to change its extension, preparing it for PHP execution on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `picture.png` | Source file | Yes |
| `picture.php` | Destination name | Yes |

## Examples

### Basic Usage

```bash
mv picture.png picture.php
```

## Expected Output

No output; file is renamed. Verify with `ls`.

## Related

- [[procedures/Rename-Image-to-PHP-Extension]]
