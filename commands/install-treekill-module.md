---
id: cmd-001
data: npm i treekill
tags:
  - npm
  - install
type: command
output: null
executor: bash
platforms:
  - Windows
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.584Z'
verified: false
validated: true
submitted: true
---
# install-treekill-module

## Command

```bash
npm i treekill
```

## Description

Installs the treekill Node.js module from the npm registry, specifically version 1.0.0 which contains the RCE vulnerability, as part of reproducing the command injection exploit on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Alias for --install, triggers package installation | Yes |
| `treekill` | Name of the package to install | Yes |

## Examples

### Basic Usage

```bash
npm i treekill
```

### Advanced Usage

```bash
npm i treekill@1.0.0
```

## Expected Output

Package installation logs, including fetching metadata, resolving dependencies, and a summary like "added 1 package in X ms".

## Related

- [[Related Procedure|procedures/Install-Vulnerable-treekill-Module]]
