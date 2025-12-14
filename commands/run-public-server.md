---
id: cmd-uuid-2
data: ./node_modules/public/bin/public ./ 8000
tags:
  - server
  - nodejs
type: command
output: 'Public.js server running with [path] on port 8000'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.871Z'
verified: false
validated: true
submitted: true
---
# run-public-server

## Command

```bash
./node_modules/public/bin/public ./ 8000
```

## Description

Launches the 'public' module's binary to serve the current directory (./) on port 8000 with directory indexing, exposing the XSS vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ./ | Directory to serve (current) | Yes |
| 8000 | Port to bind to | Yes |
| -p (optional) | Specify port alternative | No |

## Examples

### Basic Usage

```bash
./node_modules/public/bin/public ./ 8000
```

### Advanced Usage

```bash
./node_modules/public/bin/public /path/to/dir 3000
```

## Expected Output

Public.js server running with ./ on port 8000. Server listens until interrupted.

## Related

- [[commands/npm-install-public]]
- [[procedures/Run-Public-Server]]
