---
data: npm i express
tags:
  - install
  - dependencies
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e95f6409-d959-482a-b183-d75a3f35909d
created_at: '2025-12-13T23:56:19.643Z'
updated_at: '2025-12-13T23:56:19.643Z'
verified: false
validated: true
submitted: true
---
# npm-install-express

## Command

```bash
npm i express
```

## Description

Installs the Express web framework as a project dependency, enabling simple HTTP server creation for serving malicious pages and scripts in XSS attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Alias for install | Yes |
| `express` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i express
```

### Advanced Usage

```bash
npm i express --save-dev
```

## Expected Output

Downloads Express to node_modules, updates package.json dependencies. Output: "added 50 packages" or similar.

## Related

- [[commands/npm-init-project]]
- [[procedures/Set-Up-Malicious-Express-Server-for-XSS]]
