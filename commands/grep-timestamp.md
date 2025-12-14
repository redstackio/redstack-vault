---
id: cmd-grep-timestamp
data: 'grep -o ''[0-9]\{10\}'' error_response.txt'
tags:
  - parsing
  - recon
type: command
output: '1527341299'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.384Z'
verified: false
validated: true
submitted: true
---
# grep-timestamp

## Command

```bash
grep -o '[0-9]\{10\}' error_response.txt
```

## Description

Extracts a 10-digit Unix timestamp from a server error response file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Outputs only the matched parts | Yes |
| `'[0-9]\{10\}'` | Regex for 10 digits | Yes |
| `error_response.txt` | Input file | Yes |

## Examples

### Basic Usage

```bash
grep -o '[0-9]\{10\}' error_response.txt
```

## Expected Output

Timestamp like "1527341299".

## Related

- [[procedures/Extract-Upload-Timestamp]]
