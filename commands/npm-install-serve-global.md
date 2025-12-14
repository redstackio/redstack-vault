---
id: cmd-398285-npm-add
data: npm i serve -g
tags:
  - installation
type: command
output: |-
  added 1 package in Xs
  serve@9.6.0
executor: bash
platforms:
  - Node.js
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.897Z'
verified: false
validated: true
submitted: true
---
# npm-install-serve-global

## Command

```bash
npm i serve -g
```

## Description

Alternative to yarn for globally installing the serve package via npm, enabling the same vulnerable HTTP serving functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i | Shorthand for install | Yes |
| serve | Package name | Yes |
| -g | Global installation flag | Yes |

## Examples

### Basic Usage

```bash
npm i serve -g
```

### Advanced Usage

```bash
npm install serve@9.6.0 -g
```

## Expected Output

NPM reports packages added and version installed, with serve now in global PATH.

## Related

- [[commands/yarn-global-add-serve]]
