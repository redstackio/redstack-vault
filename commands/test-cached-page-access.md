---
data: 'curl -v https://paypal.com/signin'
tags:
  - verification
  - xss
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: bfa4a956-4876-44a6-9134-4a5ca06b54cd
created_at: '2025-12-11T03:47:56.874Z'
updated_at: '2025-12-11T03:47:56.874Z'
verified: false
validated: true
submitted: true
---
# test-cached-page-access

## Command

```bash
curl -v https://paypal.com/signin
```

## Description

Tests access to a cached page to verify if poisoning or XSS has taken effect by examining the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for headers | Yes |
| `URL` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -v https://target.com/page
```

### Advanced Usage

```bash
curl -v -H "Cache-Control: no-cache" https://target.com/page
```

## Expected Output

Verbose output showing headers and body, potentially including poisoned content or redirects.

## Related

- [[procedures/Verify-Stored-XSS-Impact]]
