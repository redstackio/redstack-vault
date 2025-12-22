---
type: command
executor: bash
data: npm install --save ws
tags:
  - setup
  - nodejs
platforms:
  - Linux
  - macOS
  - Windows
verified: true
validated: true
---

# npm-install-ws

## Command

```bash
npm install --save ws
```

## Description

This command installs the 'ws' Node.js library as a dependency, enabling WebSocket server and client functionality for testing or simulating vulnerable endpoints in CSWSH attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | NPM subcommand to install package | Yes |
| `--save` or `-S` | Save as dependency in package.json | Yes |
| `ws` | Package name for WebSocket implementation | Yes |

## Examples

### Basic Usage

```bash
npm install --save ws
```

### Advanced Usage

Install globally for CLI tools:

```bash
npm install -g ws
```

## Expected Output

```
added 1 package, and audited 2 packages in 2s
found 0 vulnerabilities
```

Success: 'ws' appears in node_modules and package.json dependencies.

## Related

- [[procedures/Perform-Cross-Site-WebSocket-Hijacking]]
