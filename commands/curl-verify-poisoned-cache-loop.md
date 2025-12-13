---
data: 'while true; do curl -ik "https://themes.shopify.com:443/"|grep ":1337"; done'
tags:
  - web-cache-poisoning
  - verification
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ff515ba2-13de-4e14-9d7c-b8f43e8e10ad
created_at: '2025-12-13T09:00:34.701Z'
updated_at: '2025-12-13T09:00:34.701Z'
verified: false
validated: true
submitted: true
---
# curl Verify Poisoned Cache Loop

## Command

```bash
while true; do curl -ik "https://themes.shopify.com:443/"|grep ":1337"; done
```

## Description

This command repeatedly sends a GET request to the homepage and greps the response for the poisoned port to confirm successful cache poisoning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ik` | Ignore certificate errors and show headers | Yes |
| `|grep ":1337"` | Filters output to check for the poisoned port | Yes |
| `https://themes.shopify.com:443/` | Target URL for the homepage | Yes |

## Examples

### Basic Usage

```bash
while true; do curl -ik "https://themes.shopify.com:443/"|grep ":1337"; done
```

### Advanced Usage

```bash
while true; do curl -ik "https://example.com:443/"|grep ":9999"; done
```

## Expected Output

Output lines containing :1337, such as <link rel="canonical" href="https://themes.shopify.com:1337/">, indicating the cache serves poisoned content.

## Related

- [[commands/curl-poison-host-header-loop]]
- [[procedures/Verify-Cache-Poisoning-on-Homepage]]
