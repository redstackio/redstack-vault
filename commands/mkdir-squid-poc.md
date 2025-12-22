---
id: cmd-mkdir-squid-poc-2023
data: mkdir squid-poc
tags:
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.996Z'
verified: false
validated: true
submitted: true
---
# mkdir-squid-poc

## Command

```bash
mkdir squid-poc
```

## Description

Creates a new directory named `squid-poc` for organizing the Squid vulnerability reproduction files. Use this in initial setup phases to isolate project artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `squid-poc` | Directory name | Yes |

## Examples

### Basic Usage

```bash
mkdir squid-poc
```

### Advanced Usage

```bash
mkdir -p squid-poc/subdir
```

## Expected Output

No output on success; directory created and visible with `ls`.

## Related

- [[commands/cd-squid-poc]]
- [[procedures/Setup-Environment-and-Download-Squid-Source]]
