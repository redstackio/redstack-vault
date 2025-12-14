---
id: cmd-uuid-001
data: npm install angular-http-server
tags:
  - installation
  - npm
type: command
output: Installation logs indicating successful download and setup of the module
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.716Z'
verified: false
validated: true
submitted: true
---
# npm-install-angular-http-server

## Command

```bash
npm install angular-http-server
```

## Description

Installs the angular-http-server Node.js package using npm, downloading it to the local node_modules for setting up a vulnerable HTTP server environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `angular-http-server` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install angular-http-server
```

### Advanced Usage

```bash
npm install angular-http-server --global
```

## Expected Output

npm logs such as 'added 1 package in X ms' confirming successful installation without errors.

## Related

- [[Related Procedure|procedures/Install-Vulnerable-angular-http-server]]
