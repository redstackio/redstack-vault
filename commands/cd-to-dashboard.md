---
data: cd mywallboard/
tags:
  - navigation
  - shell
type: command
output: Shell prompt changes to the new directory
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.351Z'
id: 28036afe-45c8-468c-b1c3-50e282e4b692
verified: false
validated: true
submitted: true
---
# cd-to-dashboard

## Command

```bash
cd mywallboard/
```

## Description

Changes the current working directory to the Atlasboard project folder for subsequent operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `mywallboard/` | Path to the target directory | Yes |

## Examples

### Basic Usage

```bash
cd mywallboard/
```

### Advanced Usage

```bash
cd /full/path/to/mywallboard/
```

## Expected Output

Shell prompt updates to include 'mywallboard', e.g., 'user@host:~/mywallboard$ '.

## Related

- [[commands/atlasboard-new-dashboard]]
- [[procedures/Setup-Atlasboard-Environment]]
