---
data: 'php -S 127.0.0.1:2000'
tags:
  - server
  - php
type: command
output: 'PHP server running, handling requests to order.php'
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.212Z'
id: 3a769cd7-2784-4a7f-a090-0ed47917e962
verified: false
validated: true
submitted: true
---
# php-server-start

## Command

```bash
php -S 127.0.0.1:2000
```

## Description

Starts the PHP built-in development server bound to localhost on port 2000 to serve the backend order.php API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-S` | Start server mode | Yes |
| `127.0.0.1:2000` | Host and port binding | Yes |

## Examples

### Basic Usage

```bash
php -S 127.0.0.1:2000
```

### Advanced Usage

```bash
php -S 0.0.0.0:2000
```

## Expected Output

[Mon Jan 01 00:00:00 2024] PHP 8.x Development Server (http://127.0.0.1:2000) started

## Related

- [[commands/node-exploit-run]]
