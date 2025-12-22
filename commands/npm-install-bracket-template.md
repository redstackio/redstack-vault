---
data: npm install bracket-template
tags:
  - install
  - npm
  - node.js
type: command
executor: bash
platforms:
  - Node.js
id: 277444cb-bdb8-44d1-ab5c-71b615bb0ab6
created_at: '2025-12-14T03:16:37.176Z'
updated_at: '2025-12-14T03:16:37.176Z'
verified: false
validated: true
submitted: true
---
# npm-install-bracket-template

## Command

```bash
npm install bracket-template
```

## Description

Installs the bracket-template package from the npm registry, used here to add the vulnerable templating module to a Node.js project for XSS reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `bracket-template` | The package name to install (version 1.1.5 vulnerable) | Yes |
| `--save` | Automatically adds to package.json (default in modern npm) | No |

## Examples

### Basic Usage

```bash
npm install bracket-template
```

### Advanced Usage

```bash
npm install bracket-template@1.1.5 --save
```

## Expected Output

Installation logs showing download progress, followed by 'added 1 package' and updates to package.json/node_modules.

## Related

- [[Related Procedure: Setup-Vulnerable-bracket-template-Application]]
