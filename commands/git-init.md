---
data: git init
tags:
  - git
  - initialization
type: command
output: Initializes empty Git repository in /path/to/mywallboard/.git/
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.347Z'
id: 5deb740e-3fe6-491f-9f01-c7bda6938119
verified: false
validated: true
submitted: true
---
# git-init

## Command

```bash
git init
```

## Description

Initializes a new Git repository in the current directory, preparing it for version control and submodule additions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
git init
```

### Advanced Usage

```bash
git init --bare
```

## Expected Output

'Initialized empty Git repository in .git/' message.

## Related

- [[commands/git-submodule-add-atlassian]]
- [[procedures/Integrate-Atlassian-Package]]
