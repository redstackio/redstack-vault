---
data: yarn add untitled-model
tags:
  - installation
  - node.js
type: command
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
id: a4650bbe-08ce-452d-bdc6-89e91cb6bb9a
created_at: '2025-12-14T03:46:15.037Z'
updated_at: '2025-12-14T03:46:15.037Z'
verified: false
validated: true
submitted: true
---
# yarn-add-untitled-model

## Command

```bash
yarn add untitled-model
```

## Description

Installs the untitled-model package from the npm registry into the current Node.js project's dependencies, enabling use of the vulnerable module for SQL injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `add` | Specifies the action to add a package | Yes |
| `untitled-model` | The package name to install (version 1.0.5 vulnerable) | Yes |

## Examples

### Basic Usage

```bash
yarn add untitled-model
```

### Advanced Usage

```bash
yarn add untitled-model@1.0.5
```

## Expected Output

Yarn will display installation progress, resolve dependencies, and update package.json with {"untitled-model": "^1.0.5"}. No errors if network and npm access available.

## Related

- [[Related Procedure|procedures/Install-Vulnerable-untitled-model-Module]]
