---
id: cmd-touch-readme-001
data: touch README.md
tags:
  - bash
  - file-creation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.910Z'
verified: false
validated: true
submitted: true
---
# touch-readme

## Command

```bash
touch README.md
```

## Description

Creates an empty README.md file. Part of GitLab's standard setup instructions displayed post-clone; XSS execution occurs around this block due to prior injections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `touch` | Create empty file(s) | Yes |
| `README.md` | Target file name | Yes |

## Examples

### Basic Usage

```bash
touch README.md
```

### Advanced Usage

```bash
touch README.md  # As in GitLab setup
```

## Expected Output

File created; no output.

## Related

- [[commands/git-add-readme]]
- [[procedures/Create-Blank-Project-to-Host-XSS-Payload]]
