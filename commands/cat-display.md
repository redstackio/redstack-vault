---
id: cmd-cat-display-2380084
data: cat archived_urls.txt | head -10
tags:
  - utility
  - display
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.075Z'
verified: false
validated: true
submitted: true
---
# cat-display

## Command

```bash
cat archived_urls.txt | head -10
```

## Description

This command displays the contents of a file, limited to the first 10 lines, for quick verification of query results.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cat archived_urls.txt` | Outputs file contents | Yes |
| `| head -10` | Limits to first 10 lines | No |

## Examples

### Basic Usage

```bash
cat urls.txt
```

### Advanced Usage

```bash
cat archived_urls.txt | head -5 | tail -1
```

## Expected Output

First 10 lines of the file displayed in terminal.

## Related

- [[commands/curl-cdx-query]]
- [[procedures/Query-Internet-Archive-CDX-for-Domain]]
