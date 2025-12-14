---
id: cmd-grep-filter
data: grep -i 'fd' subdomains.txt > potential.txt
tags:
  - filter
  - text
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.888Z'
verified: false
validated: true
submitted: true
---
# grep-filter

## Command

```bash
grep -i 'fd' subdomains.txt > potential.txt
```

## Description

Filters a file for lines matching a pattern, used to identify potential takeover subdomains by keywords like 'fd' for Freshdesk.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Case-insensitive | No |
| `pattern` | Search term | Yes |
| `file` | Input file | Yes |
| `> output` | Redirect to file | Yes |

## Examples

### Basic Usage

```bash
grep 'fresh' list.txt
```

### Advanced Usage

```bash
grep -i 'fd\.' subdomains.txt > candidates.txt
```

## Expected Output

Filtered lines in output file, e.g., fddkim.zomato.com.

## Related

- [[Related Procedure: Enumerate-Subdomains-for-Takeover]]
