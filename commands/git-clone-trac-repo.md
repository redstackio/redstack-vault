---
data: 'git clone git://meta.git.wordpress.org/'
tags:
  - git
  - setup
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7d87fdf2-489b-409c-a5f5-a366610c3f98
created_at: '2025-12-14T00:11:25.229Z'
updated_at: '2025-12-14T00:11:25.229Z'
verified: false
validated: true
submitted: true
---
# Git Clone Trac Repo

## Command

```bash
git clone git://meta.git.wordpress.org/
```

## Description

This command clones the Git repository containing the custom source code for the WordPress Trac instance, recommended for setting up a local test environment to avoid testing on production.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git://meta.git.wordpress.org/` | URL of the Git repository to clone | Yes |

## Examples

### Basic Usage

```bash
git clone git://meta.git.wordpress.org/
```

### Advanced Usage

```bash
git clone git://meta.git.wordpress.org/ --depth 1
```

## Expected Output

Cloned repository files, including the trac.wordpress.org subfolder, ready for local setup.

## Related

- [[procedures/Setup-Local-Trac-Environment]]
- [[tools/Git]]
