---
data: npm install 626
tags:
  - installation
  - npm
type: command
output: Installation logs and confirmation of package installation in node_modules
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.190Z'
id: 50e0e9f9-e88b-410e-9662-02fb17fc7d4d
verified: false
validated: true
submitted: true
---
# npm-install-626

## Command

```bash
npm install 626
```

## Description

Installs the 626 Node.js package from the npm registry, defaulting to version 1.1.1 which contains the path traversal vulnerability. Use this to set up a vulnerable environment for testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `626` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install 626
```

### Advanced Usage

```bash
npm install 626@1.1.1
```

## Expected Output

npm WARN deprecated ... (warnings if any)
+ 626@1.1.1
added 1 package in X ms

## Related

- [[Related Procedure|procedures/Install-Vulnerable-626-Module]]
