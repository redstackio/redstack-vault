---
id: cmd-002
data: npm i
tags:
  - install
  - dependencies
type: command
output: |-
  added X packages from Yms
  ... (installation logs)
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.545Z'
verified: false
validated: true
submitted: true
---
---

# npm-install-dependencies

## Command

```bash
npm i
```

## Description

Installs project dependencies listed in package.json, including vulnerable Sapper v0.27.10. Run in the project root after cloning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install mode (alias for install) | Yes |

## Examples

### Basic Usage

```bash
npm i
```

### Advanced Usage

```bash
npm i --production
```

## Expected Output

List of added packages and creation of node_modules.

## Related

- [[Related Procedure: Install-Sapper-Dependencies]]

---
