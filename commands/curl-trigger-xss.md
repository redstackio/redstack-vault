---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
name: curl-trigger-xss
type: command
executor: bash
data: curl URL > poisoned.js
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.632Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - http
  - xss
  - trigger
verified: false
validated: true
submitted: true
---

# curl-trigger-xss

## Command

```bash
curl URL > poisoned.js
```

## Description

Downloads the poisoned JS file for local execution in a browser to trigger XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Poisoned endpoint URL | Yes |
| `> poisoned.js` | Redirect output to file | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/poisoned.js > test.js
```

### Advanced Usage

```bash
curl https://www.abritel.fr/...php.js?xxxd > poisoned.js && cat poisoned.js | grep svg
```

## Expected Output

File containing JS with injected <svg> payload; browser execution shows alert.

## Related

- [[Related Procedure: Trigger-XSS-via-Poisoned-Cache]]
