---
id: cmd-uuid-002
data: angular-http-server --path ./
tags:
  - server
  - launch
type: command
output: 'Logs like ''Path specified: ./'', ''Using index.html'', ''Listening on 8080'''
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.714Z'
verified: false
validated: true
submitted: true
---
# angular-http-server-run

## Command

```bash
angular-http-server --path ./
```

## Description

Starts the angular-http-server serving files from the current directory (./) on port 8080, exposing the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--path` | Directory to serve as root (e.g., ./) | Yes |

## Examples

### Basic Usage

```bash
angular-http-server --path ./
```

### Advanced Usage

```bash
angular-http-server --path /path/to/dir
```

## Expected Output

Server startup messages: 'Path specified: ./', 'Using index.html', 'Listening on 8080'.

## Related

- [[Related Procedure|procedures/Setup-and-Run-angular-http-server]]
