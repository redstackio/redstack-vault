---
data: 'curl https://paypal.com/signin'
tags:
  - xss
type: command
executor: bash
platforms:
  - Web
id: fa422819-cc50-46c4-9bca-fdce1248ce9b
created_at: '2025-12-14T00:11:25.420Z'
updated_at: '2025-12-14T00:11:25.420Z'
verified: false
validated: true
submitted: true
---
# Verify XSS Payload

## Command

```bash
curl https://paypal.com/signin
```

## Description

Verifies if the cached page serves the injected XSS payload by requesting the page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl https://paypal.com/signin
```

### Advanced Usage

```bash
curl -v https://paypal.com/signin | grep 'script'
```

## Expected Output

Response containing injected XSS content or script tags.

## Related

- [[commands/craft-poisoning-request]]
- [[procedures/Verify-Stored-XSS-via-Cache-Poisoning]]
