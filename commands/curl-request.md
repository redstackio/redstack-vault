---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: 'curl http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php'
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:08:48.584Z'
verified: false
validated: true
submitted: true
---
# curl-request

## Command

```bash
curl http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php
```

## Description

Sends a GET request to the CSS optimizer endpoint to access the interface without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php
```

### Advanced Usage

```bash
curl -v http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php
```

## Expected Output

HTML response with the CSS tidying form, indicating successful access.

## Related

- [[Related Procedure]]
