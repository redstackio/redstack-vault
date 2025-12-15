---
data: npm install
tags:
  - install
  - dependencies
type: command
output: Installation logs for packages like express and undici
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.219Z'
id: 4852f67e-cdfc-4ce9-b4d4-52442a87cb12
verified: false
validated: true
submitted: true
---
# npm-install

## Command

```bash
npm install
```

## Description

Installs Node.js dependencies from package.json, including express for the server and undici for vulnerable multipart handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Installs from package.json | Yes |

## Examples

### Basic Usage

```bash
npm install
```

### Advanced Usage

```bash
npm install --save-dev
```

## Expected Output

up to date, audited X packages in Xs

## Related

- [[commands/node-server-start]]
