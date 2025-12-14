---
id: cmd-npm-install-001
data: npm install hangersteak
tags:
  - setup
  - installation
type: command
output: Installation logs and confirmation of package download
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.520Z'
verified: false
validated: true
submitted: true
---
# npm-install-hangersteak

## Command

```bash
npm install hangersteak
```

## Description

Installs the hangersteak package from the npm registry, defaulting to version 0.2.4, which contains the directory traversal vulnerability. Use this to set up a vulnerable environment for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `hangersteak` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install hangersteak
```

### Advanced Usage

```bash
npm install hangersteak@0.2.4
```

## Expected Output

Logs showing package resolution, download, and addition to node_modules, e.g., "added 1 package in 1s".

## Related

- [[Related Procedure|procedures/Install-Vulnerable-Hangersteak-Module]]
