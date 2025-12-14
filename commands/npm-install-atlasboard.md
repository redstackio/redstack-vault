---
data: npm install -g atlasboard
tags:
  - installation
  - npm
type: command
output: Installation logs and success message
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.357Z'
id: 2c363f99-1794-43ee-ae11-f72e2055ad9d
verified: false
validated: true
submitted: true
---
# npm-install-atlasboard

## Command

```bash
npm install -g atlasboard
```

## Description

Installs the Atlasboard dashboard framework globally using npm, making the CLI available for creating and managing dashboards in a Node.js environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g` | Installs the package globally, adding it to the system PATH | Yes |
| `atlasboard` | The package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install -g atlasboard
```

### Advanced Usage

```bash
npm install -g atlasboard@latest
```

## Expected Output

Progress logs showing dependency downloads, followed by 'added X packages' and confirmation that the 'atlasboard' binary is installed.

## Related

- [[commands/atlasboard-new-dashboard]]
- [[procedures/Setup-Atlasboard-Environment]]
