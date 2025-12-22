---
id: cmd-398285-yarn-add
data: yarn global add serve
tags:
  - installation
type: command
output: |-
  Success: yarn global v1.x.x
  [1/1] ⌘  serve@9.6.0
  ├── ecstatic@2.2.0
  … (installation details)
  ✓  Done in X.XXs.
executor: bash
platforms:
  - Node.js
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.904Z'
verified: false
validated: true
submitted: true
---
# yarn-global-add-serve

## Command

```bash
yarn global add serve
```

## Description

Installs the serve Node.js package globally using yarn, providing a CLI tool for static file serving with the vulnerable directory listing in v9.6.0.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| global | Installs to global location for CLI access | Yes |
| add | Adds the specified package | Yes |
| serve | Package name (v9.6.0 targeted for vuln) | Yes |

## Examples

### Basic Usage

```bash
yarn global add serve
```

### Advanced Usage

```bash
yarn global add serve@9.6.0
```

## Expected Output

Yarn outputs installation progress, dependencies resolved, and confirmation that serve is now globally available.

## Related

- [[commands/npm-install-serve-global]]
