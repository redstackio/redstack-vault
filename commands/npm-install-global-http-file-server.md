---
id: cmd-npm-install-http
data: npm install -g http-file-server@0.2.6
tags:
  - installation
  - npm
type: command
output: Installation logs and confirmation of successful install
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.575Z'
verified: false
validated: true
submitted: true
---
# npm-install-global-http-file-server

## Command

```bash
npm install -g http-file-server@0.2.6
```

## Description

Installs the http-file-server module version 0.2.6 globally using npm, preparing a vulnerable Node.js file server for path traversal testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally, making it available system-wide | Yes |
| `http-file-server@0.2.6` | Specifies the exact vulnerable version to install | Yes |

## Examples

### Basic Usage

```bash
npm install -g http-file-server@0.2.6
```

### Advanced Usage

```bash
npm install -g http-file-server@0.2.6 --registry https://registry.npmjs.org/
```

## Expected Output

Progress bars for downloading dependencies, followed by "added X packages" and confirmation that http-file-server@0.2.6 is installed. No errors in logs.

## Related

- [[commands/start-http-file-server-with-tmp-root]]
- [[procedures/Install-Vulnerable-http-file-server]]
