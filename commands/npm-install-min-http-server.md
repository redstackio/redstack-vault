---
id: cmd-uuid-1234
data: npm install min-http-server -g
tags:
  - installation
  - npm
type: command
output: Installation logs and confirmation of successful install
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.316Z'
verified: false
validated: true
submitted: true
---
# npm-install-min-http-server

## Command

```bash
npm install min-http-server -g
```

## Description

Installs the min-http-server Node.js module globally, enabling its use as a command-line tool for setting up the vulnerable server in path traversal demonstrations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally, making it available system-wide | Yes |

## Examples

### Basic Usage

```bash
npm install min-http-server -g
```

### Advanced Usage

```bash
npm install min-http-server -g --save-dev
```

## Expected Output

Logs showing package resolution, download progress, and final confirmation: "+ min-http-server@version added X packages in Ys".

## Related

- [[Related Procedure|procedures/Install-min-http-server-Module]]
