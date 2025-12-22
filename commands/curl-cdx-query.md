---
id: cmd-curl-cdx-2380084
data: >-
  curl
  "https://web.archive.org/cdx/search/cdx?url=TARGET_DOMAIN/*&collapse=urlkey&output=text&fl=original"
  > archived_urls.txt
tags:
  - osint
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.082Z'
verified: false
validated: true
submitted: true
---
# curl-cdx-query

## Command

```bash
curl "https://web.archive.org/cdx/search/cdx?url=TARGET_DOMAIN/*&collapse=urlkey&output=text&fl=original" > archived_urls.txt
```

## Description

This command queries the Internet Archive's CDX API to fetch a list of archived URLs for a target domain, saving the results to a file for further analysis in OSINT operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=TARGET_DOMAIN/*` | Specifies the domain to search (e.g., subscriptions.firefox.com/*) | Yes |
| `collapse=urlkey` | Removes duplicate captures | No |
| `output=text` | Outputs in plain text format | Yes |
| `fl=original` | Limits output to original URLs | Yes |
| `> archived_urls.txt` | Redirects output to file | Yes |

## Examples

### Basic Usage

```bash
curl "https://web.archive.org/cdx/search/cdx?url=example.com/*&output=text&fl=original" > urls.txt
```

### Advanced Usage

```bash
curl "https://web.archive.org/cdx/search/cdx?url=subscriptions.firefox.com/*&collapse=urlkey&output=json&fl=original,timestamp" > detailed_urls.json
```

## Expected Output

A text file with one archived URL per line, e.g., 'https://subscriptions.firefox.com/config'.

## Related

- [[commands/grep-search]]
- [[procedures/Query-Internet-Archive-CDX-for-Domain]]
