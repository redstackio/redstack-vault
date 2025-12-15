---
id: cmd-736522-mkdir-poc
data: mkdir poc
tags:
  - setup
  - directory
type: command
output: New directory created (no stdout if successful)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (Git Bash)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.846Z'
verified: false
validated: true
submitted: true
---
# create-poc-directory

## Command

```bash
mkdir poc
```

## Description

Creates a new directory named 'poc' for isolating the proof-of-concept testing environment in the authmagic vulnerability reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc` | Directory name for PoC | Yes |

## Examples

### Basic Usage

```bash
mkdir poc
```

### Advanced Usage

```bash
mkdir -p poc/subdir  # Create parent if needed
```

## Expected Output

No output on success; directory 'poc' is created in the current working directory. Use `ls` to verify.

## Related

- [[commands/change-to-poc-directory]]
- [[procedures/Setup-Testing-Environment-for-Authmagic]]
