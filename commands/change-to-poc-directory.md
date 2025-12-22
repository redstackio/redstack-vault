---
id: cmd-736522-cd-poc
data: cd poc/
tags:
  - navigation
  - directory
type: command
output: Current working directory changed to poc/
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (Git Bash)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.841Z'
verified: false
validated: true
submitted: true
---
# change-to-poc-directory

## Command

```bash
cd poc/
```

## Description

Changes the current working directory to the 'poc' folder created for authmagic testing, preparing for npm operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc/` | Target directory path | Yes |

## Examples

### Basic Usage

```bash
cd poc/
```

### Advanced Usage

```bash
cd poc/ && pwd  # Verify path
```

## Expected Output

Shell prompt updates to include '/poc'. Use `pwd` to confirm.

## Related

- [[commands/create-poc-directory]]
- [[procedures/Setup-Testing-Environment-for-Authmagic]]
