---
data: 'curl -i "http://target/path"'
tags:
  - recon
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 67a2c88b-ef92-49d4-90bd-061aa02e9c8f
created_at: '2025-12-11T06:10:24.848Z'
updated_at: '2025-12-11T06:10:24.849Z'
verified: false
validated: true
submitted: true
---
# curl-path-manipulation

## Command

```bash
curl -i "http://target/path"
```

## Description

Uses curl to manipulate and request web paths for reconnaissance, error triggering, or form submission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| `url` | Target URL with path | Yes |

## Examples

### Basic Usage

```bash
curl -i "http://subdomain.starbucks.com/<CMS-name>"
```

### Advanced Usage

```bash
curl -X POST "http://subdomain.starbucks.com/josso/signin" -d "username=admin&password=admin"
```

## Expected Output

HTTP response with headers and body, potentially including redirects or errors.

## Related

- [[commands/curl-directory-traversal]]
- [[procedures/Reconnaissance-via-Subdomain-and-Path-Enumeration]]
