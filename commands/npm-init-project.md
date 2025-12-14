---
data: npm init -y
tags:
  - setup
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.032Z'
id: f69ad7f3-8db2-4b67-bb2e-0b47849eb240
verified: false
validated: true
submitted: true
---
# npm-init-project

## Command

```bash
npm init -y
```

## Description

Initializes a new npm project by creating a package.json file with default values, enabling dependency management for the PoC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -y | Auto-yes flag to skip prompts | Yes |

## Examples

### Basic Usage

```bash
npm init -y
```

### Advanced Usage

```bash
npm init -y --scope=@test
```

## Expected Output

Generates package.json; outputs "Wrote to /path/package.json".

## Related

- [[commands/npm-install-express]]
