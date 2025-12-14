---
id: cmd-curl-endpoint-test
data: >-
  curl -X GET
  "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase"
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
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.790Z'
verified: false
validated: true
submitted: true
---
# curl-endpoint-test

## Command

```bash
curl -X GET "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase"
```

## Description

This command performs a GET request to probe the GiftCert-Purchase endpoint, retrieving its HTML to inspect for forms and parameters. Use it during reconnaissance to discover eCommerce vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase"
```

### With Output to File

```bash
curl -X GET "http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-Purchase" -o endpoint.html
```

## Expected Output

HTML response containing the gift certificate purchase form, including input fields for amount and email.

## Related

- [[Related Procedure]]
