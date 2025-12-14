---
id: cmd-grep-search-2380084
data: grep -i 'clientid' archived_urls.txt
tags:
  - search
  - osint
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.080Z'
verified: false
validated: true
submitted: true
---
# grep-search

## Command

```bash
grep -i 'clientid' archived_urls.txt
```

## Description

This command searches a text file of archived URLs for case-insensitive matches of keywords like 'clientId' to identify potential sensitive content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Case-insensitive search | No |
| `'clientid'` | Keyword to search for | Yes |
| `archived_urls.txt` | Input file | Yes |

## Examples

### Basic Usage

```bash
grep -i 'apikey' urls.txt
```

### Advanced Usage

```bash
grep -i -n 'clientid\|dsn' archived_urls.txt
```

## Expected Output

Matching lines from the file, e.g., 'https://domain.com/{encoded with clientId}'.

## Related

- [[commands/curl-cdx-query]]
- [[procedures/Search-Archived-Content-for-Sensitive-Keywords]]
