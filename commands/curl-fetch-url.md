---
id: cmd-curl-fetch-url
data: 'curl -s "https://proxy.duckduckgo.com/50x.html?e=&atb=" | grep atb'
tags:
  - web-testing
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.480Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-url

## Command

```bash
curl -s "https://proxy.duckduckgo.com/50x.html?e=&atb=" | grep atb
```

## Description

Fetches a URL silently and searches for a specific parameter in the response to check for reflection in web pages during vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, no progress meter | Yes |
| URL | Target endpoint with parameters | Yes |
| `| grep atb` | Pipe to search for 'atb' in output | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://example.com/page?param=" | grep param
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" "https://target.com/50x.html?e=&atb=" | grep -i atb
```

## Expected Output

Lines containing 'atb' if reflected, e.g., atb="value" in HTML source.

## Related

- [[Related Procedure]]
