---
data: cd poc/
tags:
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.034Z'
id: 4fbe84c6-f3e8-4432-ba39-5da14a83846a
verified: false
validated: true
submitted: true
---
# cd-poc-directory

## Command

```bash
cd poc/
```

## Description

Changes the current working directory to 'poc/' to prepare for npm initialization and dependency installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc/ | Target directory path | Yes |

## Examples

### Basic Usage

```bash
cd poc/
```

### Advanced Usage

```bash
cd poc/ && ls
```

## Expected Output

Changes directory silently; prompt updates to show /poc.

## Related

- [[commands/mkdir-poc-directory]]
