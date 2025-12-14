---
id: cmd-003
data: cd expressCart
tags:
  - navigation
  - directory
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.114Z'
verified: false
validated: true
submitted: true
---
# change-to-expresscart-directory

## Command

```bash
cd expressCart
```

## Description

Changes the current working directory to the cloned expressCart folder to proceed with installation steps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| expressCart | Target directory name | Yes |

## Examples

### Basic Usage

```bash
cd expressCart
```

### Advanced Usage

```bash
cd expressCart && ls
```

## Expected Output

Working directory changed; prompt reflects new path.

## Related

- [[commands/clone-expresscart-repo]]
- [[procedures/Local-Setup-of-Express-Cart-Application]]
