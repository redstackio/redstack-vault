---
id: cmd-grep-urlnode-001
data: grep -rn "urlnode" src/
tags:
  - search
  - static-analysis
type: command
output: List of files and lines containing 'urlnode' references
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.544Z'
verified: false
validated: true
submitted: true
---
# grep-search-urlnode

## Command

```bash
grep -rn "urlnode" src/
```

## Description

Recursively searches src/ for 'urlnode' to examine URL handling structures potentially prone to XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Recursive search | Yes |
| `-n` | Show line numbers | Yes |
| `src/` | Directory to search | Yes |
| `"urlnode"` | Search pattern | Yes |

## Examples

### Basic Usage

```bash
grep -rn "urlnode" src/
```

### Advanced Usage

```bash
grep -rn "urlnode->url" src/
```

## Expected Output

Matches like 'src/lib/url.c:456:urlnode->url = ...'.

## Related

- [[commands/grep-search-glob-url]]
- [[procedures/Static-Code-Analysis-for-Vulnerable-URL-Handling]]
