---
id: cmd1-uuid
name: start-simple-web-server
type: command
executor: bash
data: cd $_DIRECTORY && python3 -m http.server $_PORT
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - web-hosting
  - csrf
verified: true
validated: true
---

# Start Simple Web Server

## Command

```bash
cd $_DIRECTORY && python3 -m http.server $_PORT
```

## Description

Launches a basic HTTP file server using Python's built-in module to host static content like CSRF payload pages during web attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DIRECTORY | Directory path containing files to serve (e.g., /tmp/csrf) | Yes |
| $_PORT | Listening port (default: 8000, use 80 for root if permitted) | No |

## Examples

### Basic Usage

```bash
cd /path/to/csrf-files && python3 -m http.server 8000
```

### Advanced Usage

```bash
cd /var/www/evil && python3 -m http.server 80 --bind 127.0.0.1
```

## Expected Output

Serving HTTP on :: port 8000 (http://[::]:8000/) ...
127.0.0.1 - - [01/Oct/2024 12:00:00] code 200, message File

## Related

- [[procedures/csrf-referer-bypass-with-question-mark-injection]]
