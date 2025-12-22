---
id: 123e4567-e89b-12d3-a456-426614174008
name: apache-rewritrule-serve-malicious-json
type: command
executor: apache
data: 'RewriteRule .* /zentao/issue.json [L]'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.867Z'
platforms:
  - Linux
tags:
  - apache
  - rewrite
verified: false
validated: true
submitted: true
---

# apache-rewritrule-serve-malicious-json

## Command

```apache
RewriteRule .* /zentao/issue.json [L]
```

## Description

This Apache rewrite rule redirects any matching request to the malicious JSON file containing XSS payloads, used in .htaccess for the mock ZenTao server in the GitLab attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| .* | Matches any remaining path after condition | Yes |
| /zentao/issue.json | Target file path for the payload | Yes |
| [L] | Last rule flag, stops further processing | Yes |

## Examples

### Basic Usage

```apache
RewriteRule .* /zentao/issue.json [L]
```

### Advanced Usage

```apache
RewriteRule ^/api.php/v1/issues/(.*)$ /zentao/issue-$1.json [L]
```

## Expected Output

Serves the content of /zentao/issue.json as the response, e.g., malicious JSON with HTML injection.

## Related

- [[commands/apache-rewritecond-match-api-requests]]
