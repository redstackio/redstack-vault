---
id: cmd-uuid-1
data: npm i cloudcmd
tags:
  - installation
  - npm
type: command
output: Installation logs and confirmation of package installation in node_modules
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.044Z'
verified: false
validated: true
submitted: true
---
# npm-i-cloudcmd

## Command

```bash
npm i cloudcmd
```

## Description

Installs the CloudCMD package from the npm registry, used as the initial setup for exploiting its stored XSS vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i | Install flag (shortcut for --save) | Yes |
| cloudcmd | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i cloudcmd
```

### Advanced Usage

```bash
npm i cloudcmd@9.1.5
```

## Expected Output

npm WARN deprecated ... (warnings if any)
+ cloudcmd@9.1.5
added 1 package in X ms

## Related

- [[commands/cloudcmd-launch-server]]
