---
id: cmd-001
data: npm i node-df@0.1.4
tags:
  - installation
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.979Z'
verified: false
validated: true
submitted: true
---
# npm-install-node-df

## Command

```bash
npm i node-df@0.1.4
```

## Description

Installs the specific vulnerable version 0.1.4 of the node-df package using npm, enabling exploitation of command injection in a Node.js project.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install flag (alias for install) | Yes |
| `node-df@0.1.4` | Package name and version | Yes |

## Examples

### Basic Usage

```bash
npm i node-df@0.1.4
```

### Advanced Usage

```bash
npm i node-df@0.1.4 --save
```

## Expected Output

Installation logs including 'added 1 package' and path to node_modules/node-df, confirming successful install without errors.

## Related

- [[Related Procedure: Install-Vulnerable-node-df-Module]]
