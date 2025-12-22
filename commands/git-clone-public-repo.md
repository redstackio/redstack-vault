---
id: 69a2084d-e85f-4d3e-9167-99b9777d501e
name: git-clone-public-repo
type: command
executor: bash
data: 'git clone https://github.com/example/public-repo.git'
output: null
created_at: '2025-12-11T06:10:15.527Z'
updated_at: '2025-12-11T06:10:15.527Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - git
  - recon
verified: false
validated: true
submitted: true
---

# git-clone-public-repo

## Command

```bash
git clone https://github.com/example/public-repo.git
```

## Description

Clones a public Git repository to the local machine for inspection, useful in reconnaissance for finding leaked sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | URL of the Git repository | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/example/public-repo.git
```

### Advanced Usage

```bash
git clone --depth 1 https://github.com/example/public-repo.git
```

## Expected Output

Repository cloned successfully to the current directory, with files available for inspection.

## Related

- [[procedures/Discover-Leaked-Credentials-in-Git-Repository]]
