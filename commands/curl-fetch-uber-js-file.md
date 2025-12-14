---
id: cmd-curl-uber-js-001
data: >-
  curl
  https://uchat-staging.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js -o
  uber-config.js
tags:
  - recon
  - info-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.321Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-uber-js-file

## Command

```bash
curl https://uchat-staging.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js -o uber-config.js
```

## Description

This command uses curl to download a static JavaScript file from Uber's staging server without authentication, capturing sensitive configuration data for analysis in information disclosure scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The direct URL to the static file | Yes |
| -o | Output file name for saving the response | Yes |

## Examples

### Basic Usage

```bash
curl https://uchat-staging.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js -o uber-config.js
```

### Advanced Usage

```bash
curl -s https://uchat-staging.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js | grep -i config
```

> Pipes output to grep for immediate analysis without saving to file.

## Expected Output

The command saves the JavaScript file to uber-config.js, which contains minified or readable JS code with embedded configuration objects, system names, and source code. No errors like 401 Unauthorized should occur if the misconfiguration persists; otherwise, a 200 OK status and file download confirm success.

## Related

- [[procedures/Access-Uber-Staging-Static-JS-File-Without-Auth]]
