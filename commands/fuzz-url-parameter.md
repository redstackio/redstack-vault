---
id: 8185dbb0-92ad-4345-83d2-0ab7a2f937be
name: fuzz-url-parameter
type: command
executor: bash
data: 'curl "https://target.com/?param=test" -s | grep test'
output: null
created_at: '2025-12-11T06:10:22.177Z'
updated_at: '2025-12-11T06:10:22.177Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - fuzzing
  - web
verified: false
validated: true
submitted: true
---

# fuzz-url-parameter

## Command

```bash
curl "https://target.com/?param=test" -s | grep test
```

## Description

This command uses curl to test if a URL parameter reflects input by grepping for the test string in the response, useful for discovering potential XSS vectors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The target URL with parameter | Yes |
| `-s` | Silent mode | No |

## Examples

### Basic Usage

```bash
curl "https://www.tiktok.com/?param=test" -s | grep test
```

### Advanced Usage

```bash
curl "https://www.tiktok.com/?param=<script>alert(1)</script>" -s | grep "<script>"
```

## Expected Output

If reflected, the response will contain the test string or payload unescaped.

## Related

- [[commands/inject-xss-payload]]
- [[procedures/Discover-Reflected-XSS-Vulnerability]]
