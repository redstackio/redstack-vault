---
id: cmd-uuid-1
data: 'echo ''site:data.gov'' | googler -n 100 > urls.txt'
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.807Z'
verified: false
validated: true
submitted: true
---
# google-search-scrape

## Command

```bash
echo 'site:data.gov' | googler -n 100 > urls.txt
```

## Description

Scrapes Google search results for site-specific URLs using the googler tool, saving to a file for manual review in vulnerability hunting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n 100` | Number of results | No |
| `site:data.gov` | Search query | Yes |

## Examples

### Basic Usage

```bash
googler 'site:data.gov' -n 50 > urls.txt
```

### Advanced Usage

```bash
googler 'site:data.gov inurl:issue' -n 100 > issue_urls.txt
```

## Expected Output

A text file urls.txt containing 100 URLs from data.gov, ready for manual testing.

## Related

- [[Related Procedure]]
