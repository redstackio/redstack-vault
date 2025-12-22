---
data: npm install ghost-cli@latest -g
tags:
  - setup
  - npm
type: command
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
  - Windows
id: c8dc34e5-229a-4839-a7fb-a807651f62d6
created_at: '2025-12-14T04:39:09.660Z'
updated_at: '2025-12-14T04:39:09.660Z'
verified: false
validated: true
submitted: true
---
# npm-install-ghost-cli

## Command

```bash
npm install ghost-cli@latest -g
```

## Description

Installs the latest version of the Ghost CLI package globally using npm, allowing management of Ghost CMS instances from the command line.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally, making the `ghost` command available system-wide | Yes |
| `ghost-cli@latest` | Specifies the package name and the latest version tag | Yes |

## Examples

### Basic Usage

```bash
npm install ghost-cli@latest -g
```

### Advanced Usage

```bash
npm install ghost-cli@1.0.0 -g
```

## Expected Output

Installation progress logs, ending with a success message like "+ ghost-cli@1.x.x" and added to PATH.

## Related

- [[commands/ghost-install-local]]
- [[procedures/Install-Ghost-CLI-Globally]]
