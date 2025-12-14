---
id: cmd-grep-strcpy-001
data: grep -rn "strcpy" src/
tags:
  - search
  - static-analysis
type: command
output: List of files and lines containing 'strcpy' function calls
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.540Z'
verified: false
validated: true
submitted: true
---
# grep-search-strcpy

## Command

```bash
grep -rn "strcpy" src/
```

## Description

Searches for 'strcpy' in src/ to find unsafe string operations that could contribute to insecure URL processing and XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Recursive search | Yes |
| `-n` | Show line numbers | Yes |
| `src/` | Directory to search | Yes |
| `"strcpy"` | Search pattern | Yes |

## Examples

### Basic Usage

```bash
grep -rn "strcpy" src/
```

### Advanced Usage

```bash
grep -rn "strcpy.*url" src/
```

## Expected Output

Lines like 'src/somefile.c:789:strcpy(dest, src_url);'.

## Related

- [[commands/grep-search-urlnode]]
- [[procedures/Static-Code-Analysis-for-Vulnerable-URL-Handling]]
