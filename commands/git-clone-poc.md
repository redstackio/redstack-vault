---
data: 'git clone https://github.com/inkz/poc-webpack-bundle-analyzer.git'
tags:
  - clone
  - git
  - poc
type: command
output: Clones the repository into a local directory
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.936Z'
id: 88d1984b-44b1-438c-bc42-b57dfcf63120
verified: false
validated: true
submitted: true
---
# git-clone-poc

## Command

```bash
git clone https://github.com/inkz/poc-webpack-bundle-analyzer.git
```

## Description

Clones the POC repository demonstrating XSS in webpack-bundle-analyzer via controlled third-party module structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/inkz/poc-webpack-bundle-analyzer.git` | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/inkz/poc-webpack-bundle-analyzer.git
```

### Advanced Usage

```bash
git clone https://github.com/inkz/poc-webpack-bundle-analyzer.git poc-dir
```

## Expected Output

Cloning into 'poc-webpack-bundle-analyzer'...
remote: Enumerating objects: X, done.
...

## Related

- [[commands/cd-poc-directory]]
- [[procedures/Reproduce-with-Git-Clone-and-Build]]
