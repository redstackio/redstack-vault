---
id: cmd-unrar-extract
data: unrar x "sample.rar" -R "directory" -o+
tags:
  - extraction
  - vulnerable
type: command
output: Output captured in $output array for parsing extracted files
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.684Z'
verified: false
validated: true
submitted: true
---
# unrar-vulnerable-extraction

## Command

```bash
unrar x "sample.rar" -R "directory" -o+
```

## Description

This command extracts RAR files using unrar, but in the Nextcloud context, it's vulnerable to injection due to direct concatenation of user input into the exec call.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| x | Extract mode | Yes |
| "sample.rar" | Input file (user-controlled, injectable) | Yes |
| -R | Recursive extraction | No |
| "directory" | Output directory (user-controlled) | Yes |
| -o+ | Overwrite existing files | No |

## Examples

### Basic Usage

```bash
unrar x "sample.rar" -R "/path/to/dir" -o+
```

### Advanced Usage

Injection example: unrar x "injected"; malicious_cmd; " -R "dir" -o+

## Expected Output

List of extracted files or errors; in PHP, captured in array for response.

## Related

- [[commands/curl-download-shell]]
