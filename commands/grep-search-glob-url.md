---
id: cmd-grep-glob-001
data: grep -rn "glob_url" src/
tags:
  - search
  - static-analysis
type: command
output: List of files and lines containing 'glob_url' references
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.561Z'
verified: false
validated: true
submitted: true
---
# grep-search-glob-url

## Command

```bash
grep -rn "glob_url" src/
```

## Description

Recursively searches the src/ directory for 'glob_url' to identify potential vulnerable URL globbing code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Recursive search | Yes |
| `-n` | Show line numbers | Yes |
| `src/` | Directory to search | Yes |
| `"glob_url"` | Search pattern | Yes |

## Examples

### Basic Usage

```bash
grep -rn "glob_url" src/
```

### Advanced Usage

```bash
grep -rnw "glob_url" src/ > glob_results.txt
```

## Expected Output

File paths, line numbers, and matching lines, e.g., 'src/tool_urlglob.c:123:glob_url(...)'.

## Related

- [[commands/grep-search-urlnode]]
- [[procedures/Static-Code-Analysis-for-Vulnerable-URL-Handling]]
