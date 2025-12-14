---
data: 'curl "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/[VIDEO_ID]"'
tags:
  - api-test
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.466Z'
id: 3a98cb1c-73ad-457d-82ca-3caf1dea8caa
verified: false
validated: true
submitted: true
---
# curl-vimeo-oembed-test

## Command

```bash
curl "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/[VIDEO_ID]"
```

## Description

This command queries Vimeo's legacy oEmbed API endpoint to retrieve JSON metadata for a specified video ID, useful for testing privacy enforcement and information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Encoded Vimeo video URL (e.g., https%3A//vimeo.com/12345) | Yes |
| `-s` | Silent mode to suppress progress meter | No |
| `-I` | Fetch headers only for page tests | No |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/152133387"
```

### Advanced Usage

```bash
curl -s -w "%{http_code}" "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/[ID]"
```

## Expected Output

For public/restricted videos: JSON like {"type":"video","version":"1.0","title":"Video Title","provider_name":"Vimeo"}. For strict private: 404 or empty.

## Related

- [[Related Procedure: Exploit-OEmbed-API-with-Restricted-Private-Videos]]
