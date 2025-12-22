---
data: npm i pm2
tags:
  - setup
  - install
type: command
output: Installation logs and success message
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.448Z'
id: e2b6d80a-aaf2-4947-868a-44b053c292f5
verified: false
validated: true
submitted: true
---
# npm-i-pm2

## Command

```bash
npm i pm2
```

## Description

Installs the PM2 Node.js process manager locally in the current project directory via npm, enabling access to its vulnerable install function for command injection exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Installs the specified package (pm2) | Yes |
| `pm2` | Package name for PM2 | Yes |

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

NPM download and installation logs, confirming PM2 v3.5.1 (vulnerable version) is added to node_modules, with a success message indicating completion.

## Related

- [[commands/pm2-start]]
- [[procedures/Install-and-Verify-PM2]]
