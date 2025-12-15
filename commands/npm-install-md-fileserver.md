---
data: npm install -g md-fileserver
tags:
  - installation
  - node-js
type: command
executor: bash
platforms:
  - Node.js
  - Linux
id: b5e3b687-4f8c-490c-af16-965626d47e3f
created_at: '2025-12-14T17:26:05.881Z'
updated_at: '2025-12-14T17:26:05.881Z'
verified: false
validated: true
submitted: true
---
# npm-install-md-fileserver

## Command

```bash
npm install -g md-fileserver
```

## Description

This command installs the md-fileserver Node.js module globally from the npm registry, enabling the mdstart command for launching a vulnerable local file server prone to path traversal attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally, adding binaries to the system PATH | Yes |
| `md-fileserver` | The package name to install (version 1.3.2 is vulnerable) | Yes |

## Examples

### Basic Usage

```bash
npm install -g md-fileserver
```

### Advanced Usage

```bash
npm install -g md-fileserver@1.3.2
```

## Expected Output

Installation progress with lines like "added 5 packages in 2s" and no errors, confirming global availability of mdstart.

## Related

- [[Related Procedure|procedures/Install-md-fileserver-Module]]
