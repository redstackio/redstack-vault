---
id: fff11d9c-9346-445e-9cfe-162a1b18c988
name: npm-install-global
type: command
executor: bash
data: npm install -g featurebook@0.0.32
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.835Z'
platforms:
  - Linux
  - Node.js
tags:
  - installation
  - npm
verified: false
validated: true
submitted: true
---

# npm-install-global

## Command

```bash
npm install -g featurebook@0.0.32
```

## Description

This command installs the featurebook package version 0.0.32 globally using npm, making it available system-wide for server setup in vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g, --global` | Installs the package globally | Yes |
| `featurebook@0.0.32` | Specifies the package and vulnerable version | Yes |

## Examples

### Basic Usage

```bash
npm install -g featurebook@0.0.32
```

### Advanced Usage

```bash
npm install -g featurebook@0.0.32 --registry https://registry.npmjs.org/
```

## Expected Output

Output includes fetching metadata, downloading the package, and a success message like "+ featurebook@0.0.32" followed by "added 1 package". Errors if version not found or permissions denied.

## Related

- [[commands/featurebook-serve]]
