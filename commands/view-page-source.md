---
data: curl -s 'target-url' | less
tags:
  - recon
  - web
type: command
executor: bash
platforms:
  - Linux
  - Web
id: e19fbfb9-6e20-4855-bba9-087d3271d7bd
created_at: '2025-12-14T00:11:16.365Z'
updated_at: '2025-12-14T00:11:16.365Z'
verified: false
validated: true
submitted: true
---
# View Page Source

## Command

```bash
curl -s 'target-url' | less
```

## Description

Fetches and displays the HTML source of a web page for inspection, useful for verifying reflected inputs or vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-url` | URL of the page to fetch | Yes |
| `-s` | Silent mode | No |

## Examples

### Basic Usage

```bash
curl -s 'https://pages.et.uber.com/icecream/?lang_id=5' | less
```

### Advanced Usage

```bash
curl -s 'https://pages.et.uber.com/icecream/?lang_id=5' | grep 'lang_id'
```

## Expected Output

Raw HTML source code of the page.

## Related

- [[procedures/Identify-Vulnerable-Endpoint]]
- [[commands/inject-xss-payload-url]]
