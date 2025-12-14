---
id: 123e4567-e89b-12d3-a456-426614174007
name: apache-rewritecond-match-api-requests
type: command
executor: apache
data: 'RewriteCond %{REQUEST_URI} ^/api.php/v1/issues'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.869Z'
platforms:
  - Linux
tags:
  - apache
  - rewrite
verified: false
validated: true
submitted: true
---

# apache-rewritecond-match-api-requests

## Command

```apache
RewriteCond %{REQUEST_URI} ^/api.php/v1/issues
```

## Description

This Apache directive checks if the request URI matches the pattern for ZenTao API issue endpoints, used in .htaccess to condition rewrites for serving malicious payloads in the XSS attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %{REQUEST_URI} | The incoming request URI | Yes |
| ^/api.php/v1/issues | Regex pattern to match API paths | Yes |

## Examples

### Basic Usage

```apache
RewriteCond %{REQUEST_URI} ^/api.php/v1/issues
```

### Advanced Usage

```apache
RewriteCond %{REQUEST_URI} ^/api.php/v1/issues/story-[0-9]+
```

## Expected Output

Triggers the subsequent RewriteRule if the condition is met, no direct output but enables rewrite processing.

## Related

- [[commands/apache-rewritrule-serve-malicious-json]]
