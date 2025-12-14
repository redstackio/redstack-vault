---
data: 'while true; do curl -ik "https://themes.shopify.com/" | grep ":1337"; done'
tags:
  - verification
  - web-cache-poisoning
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 9d4916e9-dff9-400c-9103-ca7ba80cda48
created_at: '2025-12-14T17:26:55.891Z'
updated_at: '2025-12-14T17:26:55.891Z'
verified: false
validated: true
submitted: true
---
# curl-verify-poisoned-cache

## Command

```bash
while true; do curl -ik "https://themes.shopify.com/" | grep ":1337"; done
```

## Description

This command loops requests to the target homepage, piping responses through grep to detect if the cache poisoning has taken effect by searching for the injected string ':1337'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ik` | Include headers (-i) and insecure SSL (-k) | Yes |
| `https://themes.shopify.com/` | Target homepage URL | Yes |
| `| grep ":1337"` | Search for poison indicator in response | Yes |

## Examples

### Basic Usage

```bash
while true; do curl -ik "https://themes.shopify.com/" | grep ":1337"; done
```

### Advanced Usage

```bash
while true; do curl -ik "https://themes.shopify.com/" -H "Accept-Encoding: gzip" | gunzip | grep -i ":1337"; sleep 1; done
```

## Expected Output

Grep matches like <link rel="canonical" href="https://themes.shopify.com:1337/">, indicating successful cache poisoning.

## Related

- [[Related Procedure: Verify-Cache-Poisoning-via-Response-Inspection]]
