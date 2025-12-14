---
data: 'curl -I http://ci.owncloud.com/'
tags:
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
id: 42908823-fb99-45db-8115-f89d87ba4b0d
created_at: '2025-12-14T17:23:28.133Z'
updated_at: '2025-12-14T17:23:28.133Z'
verified: false
validated: true
submitted: true
---
# curl-check-jenkins-url

## Command

```bash
curl -I http://ci.owncloud.com/
```

## Description

This command performs a HEAD request to check the accessibility and headers of a potential Jenkins instance URL, identifying exposure without downloading the full page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Fetch headers only | Yes |
| `http://ci.owncloud.com/` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I http://ci.owncloud.com/
```

### Advanced Usage

```bash
curl -I -v http://ci.owncloud.com/  # Verbose for connection details
```

## Expected Output

HTTP/1.1 200 OK
Server: Jetty(8.x.x)
X-Jenkins: 1.0

Indicates Jenkins presence via specific headers.

## Related

- [[Related Procedure: Discover-Exposed-Jenkins-Instance]]
