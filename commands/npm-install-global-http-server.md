---
data: npm install -g http_server
tags:
  - installation
  - npm
type: command
output: Installation completion message
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:49.787Z'
id: 1aa1f569-b463-447a-aaeb-f0a17e2c54f7
verified: false
validated: true
submitted: true
---
# npm-install-global-http-server

## Command

```bash
npm install -g http_server
```

## Description

Installs the http_server Node.js module globally, allowing the http_server command to be run from any directory for serving static files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally | Yes |
| `http_server` | Package name from npm registry | Yes |

## Examples

### Basic Usage

```bash
npm install -g http_server
```

### Advanced Usage

```bash
npm install -g http_server --save-dev
```

## Expected Output

npm progress bars followed by "added X packages in Ys" confirming successful global installation.

## Related

- [[commands/http-server-start]]
