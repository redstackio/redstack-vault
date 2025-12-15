---
data: hexo server -d
tags:
  - server
  - hexo
type: command
output: 'Local server running at http://localhost:4000'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.701Z'
id: 7f24281a-5d1f-4518-be66-6e3f33485c0b
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

Starts the Hexo development server in deploy mode, automatically generating static files and serving the site locally on port 4000. Used after installation or rebuilds to host the blog and access the admin panel.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Deploy mode: generates files before serving | Yes |

## Examples

### Basic Usage

```bash
hexo server -d
```

### Advanced Usage

```bash
hexo server -d --port 5000
```

## Expected Output

INFO  Local server started at http://localhost:4000/

## Related

- [[commands/hexo-generate]]
- [[procedures/Install-and-Setup-Hexo-with-Admin-Plugin]]
