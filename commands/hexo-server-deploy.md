---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
name: hexo-server-deploy
type: command
executor: bash
data: hexo server -d
output: 'Local server running at localhost:4000 with the blog site accessible'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.025Z'
platforms:
  - Node.js
tags:
  - hexo
  - server
verified: false
validated: true
submitted: true
---

# hexo-server-deploy

## Command

```bash
hexo server -d
```

## Description

Starts the Hexo development server in deploy mode, automatically generating static files before serving them locally on port 4000. Used to host the blog and access the admin panel for testing vulnerabilities like stored XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d, --deploy` | Generates files before starting the server | No |

## Examples

### Basic Usage

```bash
hexo server -d
```

### Advanced Usage

```bash
hexo server -d --port 3000
```

## Expected Output

Server logs indicate successful generation and startup: INFO Generated in X ms, Server running at http://localhost:4000.

## Related

- [[commands/hexo-generate]]
- [[procedures/Start-Hexo-Server-and-Access-Admin-Panel]]
