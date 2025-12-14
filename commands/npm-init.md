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
updated_at: '2025-12-14T03:16:13.981Z'
id: 14d12dbd-cdee-4cc9-8140-d3b2cc11ed48
verified: false
validated: true
submitted: true
---
# npm-init

## Command

```bash
npm init -y
```

## Description

Initializes a new Node.js project by creating a package.json file with default values, skipping interactive prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-y` | Auto-yes to all prompts | Yes |

## Examples

### Basic Usage

```bash
npm init -y
```

### Advanced Usage

```bash
npm init -y --scope=@myorg
```

## Expected Output

Creates package.json with basic fields like name, version, and main.

## Related

- [[commands/npm-install-tianma-static]]
