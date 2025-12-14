---
id: cmd-php-start-server-001
data: 'php -S localhost:8000 -t /www/web/ -d session.upload_progress.cleanup=0'
tags:
  - php
  - server
  - setup
type: command
output: '[Date] PHP Development Server (http://localhost:8000) started'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:09.948Z'
verified: false
validated: true
submitted: true
---
# php-start-builtin-server

## Command

```bash
php -S localhost:8000 -t /www/web/ -d session.upload_progress.cleanup=0
```

## Description

Starts the PHP built-in development web server on localhost port 8000, serving files from the /www/web/ directory, with the session.upload_progress.cleanup INI directive set to 0 to disable cleanup and enable the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-S` | Start built-in server mode | Yes |
| `localhost:8000` | Host and port to bind | Yes |
| `-t /www/web/` | Document root directory | Yes |
| `-d session.upload_progress.cleanup=0` | Set INI directive to disable cleanup | Yes |

## Examples

### Basic Usage

```bash
php -S localhost:8000 -t /www/web/ -d session.upload_progress.cleanup=0
```

### Advanced Usage

```bash
php -S 0.0.0.0:8080 -t /var/www/ -d session.upload_progress.cleanup=0 -d display_errors=1
```

## Expected Output

Server startup message like '[Sun Feb 18 ...] PHP 7.x.x Development Server (http://localhost:8000) started' with no binding errors.

## Related

- [[Related Procedure|procedures/Setup-Vulnerable-PHP-Server]]
