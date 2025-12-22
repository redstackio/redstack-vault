---
id: cmd-uuid-2
data: touch some-file
tags:
  - file-creation
type: command
output: ''
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.328Z'
verified: false
validated: true
submitted: true
---
---

# touch-file

## Command

```bash
touch some-file
```

## Description

Creates an empty file to serve as an initial commit placeholder in empty repositories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `some-file` | Name of the file to create | Yes |

## Examples

### Basic Usage

```bash
touch some-file
```

### Advanced Usage

```bash
touch init.txt
```

## Expected Output

Empty file created with current timestamp.

## Related

- [[commands/git-add-file]]
- [[procedures/Initialize-GitLab-Project-and-Wiki-Repositories]]
