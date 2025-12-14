---
data: atlasboard new mywallboard
tags:
  - setup
  - atlasboard
type: command
output: Creates directory structure for the dashboard
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.354Z'
id: 8e204114-5aed-4a7e-9f63-1d6affa0ee89
verified: false
validated: true
submitted: true
---
# atlasboard-new-dashboard

## Command

```bash
atlasboard new mywallboard
```

## Description

Creates a new Atlasboard project directory named 'mywallboard' with initial configuration files for building dashboards.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `new` | Subcommand to generate a new project | Yes |
| `mywallboard` | Name of the directory to create | Yes |

## Examples

### Basic Usage

```bash
atlasboard new mywallboard
```

### Advanced Usage

```bash
atlasboard new my-dashboard
```

## Expected Output

Console output indicating creation of directories like 'config', 'packages', and files such as 'package.json' and 'start.js'.

## Related

- [[commands/npm-install-atlasboard]]
- [[procedures/Setup-Atlasboard-Environment]]
