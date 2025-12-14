---
id: cmd-cd-project-path-001
data: 'cd #{h @project.path}'
tags:
  - bash
  - navigation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.916Z'
verified: false
validated: true
submitted: true
---
# cd-project-path

## Command

```bash
cd #{h @project.path}
```

## Description

Changes the current directory to the project path. Displayed in GitLab instructions with escaped path interpolation; XSS from nearby branch name can execute before or after this in the browser-rendered block.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cd` | Shell command to change directory | Yes |
| `#{h @project.path}` | Escaped project path variable | Yes |

## Examples

### Basic Usage

```bash
cd /path/to/project
```

### Advanced Usage

```bash
cd #{h @project.path}  # GitLab interpolated display
```

## Expected Output

Directory changes silently; verify with `pwd`.

## Related

- [[commands/git-clone]]
- [[procedures/Create-Blank-Project-to-Host-XSS-Payload]]
