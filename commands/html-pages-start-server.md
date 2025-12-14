---
id: cmd-uuid-3
data: ./node_modules/html-pages/bin/index.js -p 6060
tags:
  - server
  - http
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.800Z'
verified: false
validated: true
submitted: true
---
# html-pages-start-server

## Command

```bash
./node_modules/html-pages/bin/index.js -p 6060
```

## Description

Starts the html-pages development HTTP server on port 6060, serving files and vulnerable directory listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Port to bind the server | Yes |
| `6060` | Specific port value | Yes |

## Examples

### Basic Usage

```bash
./node_modules/html-pages/bin/index.js -p 6060
```

### Advanced Usage

```bash
./node_modules/html-pages/bin/index.js -p 8080 --root /path
```

## Expected Output

Server logs: 'Server running at http://127.0.0.1:6060/'.

## Related

- [[commands/npm-install-html-pages]]
- [[procedures/Start-html-pages-Server]]
