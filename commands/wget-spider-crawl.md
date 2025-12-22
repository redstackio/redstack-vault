---
data: >-
  wget --spider --recursive --no-parent -U "Mozilla/5.0" -e robots=off
  https://fake-site.com/
tags:
  - web
  - crawling
type: command
executor: bash
platforms:
  - Linux
id: b8ebc779-de86-49bd-8b6d-c9979e44baf0
created_at: '2025-12-14T03:15:26.522Z'
updated_at: '2025-12-14T03:15:26.522Z'
verified: false
validated: true
submitted: true
---
# wget-spider-crawl

## Command

```bash
wget --spider --recursive --no-parent -U "Mozilla/5.0" -e robots=off https://fake-site.com/
```

## Description

Crawls a website recursively without downloading files, simulating browser requests to trigger caching or other server-side behaviors in web exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --spider | Only fetch headers, no download | Yes |
| --recursive | Follow links | Yes |
| --no-parent | Don't ascend to parent directory | Yes |
| -U "Mozilla/5.0" | User agent string | Yes |
| -e robots=off | Ignore robots.txt | No |
| URL | Target site | Yes |

## Examples

### Basic Usage

```bash
wget --spider https://example.com/
```

### Advanced Usage

```bash
wget --spider --recursive --level=3 https://fake-site.com/
```

## Expected Output

Log of HTTP requests and responses, e.g., 'HTTP/1.1 200 OK' for each page.

## Related

- [[procedures/Spider-Site-to-Generate-Poisoned-Cache-Files]]
- [[tools/Link-Spider]]
