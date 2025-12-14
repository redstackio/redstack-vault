---
id: cmd-exiftool-verify
data: exiftool -ver
tags:
  - verification
type: command
output: '12.50'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.390Z'
verified: false
validated: true
submitted: true
---
# exiftool-verify

## Command

```bash
exiftool -ver
```

## Description

Checks the installed version of exiftool to ensure it's available for metadata operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ver` | Displays the version number | Yes |

## Examples

### Basic Usage

```bash
exiftool -ver
```

## Expected Output

Version string, e.g., "12.50" - confirms tool is installed and functional.

## Related

- [[procedures/Prepare-Malicious-Image-with-PHP-Shell]]
- [[commands/exiftool-embed-php]]
