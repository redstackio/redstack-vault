---
data: npm i blamer@0.1.13
tags:
  - installation
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.781Z'
id: 57dc9640-2a80-4124-a276-e6f7bb75f9b2
verified: false
validated: true
submitted: true
---
# npm-install-blamer

## Command

```bash
npm i blamer@0.1.13
```

## Description

Installs the vulnerable blamer Node.js module version 0.1.13 from npm, used to set up the environment for RCE exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install mode (shortcut for --save) | Yes |
| `blamer@0.1.13` | Package name and specific vulnerable version | Yes |

## Examples

### Basic Usage

```bash
npm i blamer@0.1.13
```

### Advanced Usage

```bash
npm i blamer@0.1.13 --save-dev
```

## Expected Output

Installation logs showing download and placement in node_modules/blamer, ending with confirmation.

## Related

- [[commands/node-execute-poc]]
