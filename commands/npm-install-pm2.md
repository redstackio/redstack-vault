---
id: uuid-npm-install
data: npm i pm2
tags:
  - setup
  - npm
type: command
output: Installation logs and node_modules/pm2 directory created
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.566Z'
verified: false
validated: true
submitted: true
---
# npm-install-pm2

## Command

```bash
npm i pm2
```

## Description

Installs the PM2 module locally via npm in the current project directory, targeting vulnerable version 3.5.1 for exploitation setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install flag to add the package | Yes |
| `pm2` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i pm2
```

### Advanced Usage

```bash
npm i pm2@3.5.1
```

## Expected Output

npm logs showing dependency resolution, download, and installation; creates ./node_modules/pm2 with binaries and libs.

## Related

- [[commands/ln-symlink-pm2]]
- [[procedures/Install-and-Setup-PM2]]
