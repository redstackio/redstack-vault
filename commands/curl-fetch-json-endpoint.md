---
data: >-
  curl https://lookup.nextcloud.com/vendor/composer/installed.json -o
  composer_data.json
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.645Z'
id: 00fa3a1d-9e85-4136-abff-c85674bbac50
verified: false
validated: true
submitted: true
---
# curl-fetch-json-endpoint

## Command

```bash
curl https://lookup.nextcloud.com/vendor/composer/installed.json -o composer_data.json
```

## Description

This command uses curl to fetch the exposed JSON endpoint from Nextcloud's composer lookup service and saves it to a local file for offline analysis. It performs a simple GET request without authentication, exploiting the lack of access controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target endpoint URL | Yes |
| -o | Output file flag to save response | Yes |

## Examples

### Basic Usage

```bash
curl https://lookup.nextcloud.com/vendor/composer/installed.json -o composer_data.json
```

### Advanced Usage

```bash
curl -s https://lookup.nextcloud.com/vendor/composer/installed.json | jq '.'
```

> The -s flag silences progress output, piping to jq for immediate viewing.

## Expected Output

A JSON array of composer package objects, e.g., {"name": "package", "version": "1.0", "authors": [{"email": "user@example.com"}]}. File saved successfully if HTTP 200.

## Related

- [[Related Procedure: Access-Exposed-Composer-JSON-Endpoint]]
