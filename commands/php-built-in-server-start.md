---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: 'php -S localhost:8000'
tags:
  - hosting
  - server
type: command
output: 'PHP 8.x.x Development Server (http://localhost:8000) started'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:02.908Z'
verified: false
validated: true
submitted: true
---
# php-built-in-server-start

## Command

```bash
php -S localhost:8000
```

## Description

Starts PHP's built-in development web server to host static files like HTML from the current directory, useful for local testing of web exploits without a full web server setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-S` | Enables server mode with host:port specification | Yes |
| `localhost:8000` | Binds to localhost on port 8000; change port if needed | Yes |

## Examples

### Basic Usage

```bash
php -S localhost:8000
```

### Advanced Usage

```bash
php -S 0.0.0.0:8080
```

> Binds to all interfaces on port 8080 for broader access.

## Expected Output

Server starts serving files from the current directory at http://localhost:8000. Press Ctrl+C to stop. Errors if port is in use.

## Related

- [[Related Procedure: Host-Exploit-Files-Locally-with-PHP-Server]]
