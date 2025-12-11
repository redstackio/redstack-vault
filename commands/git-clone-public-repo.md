---
data: 'git clone https://github.com/example-repo.git'
tags:
  - git
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 180c389d-eefa-4842-9621-9ee9808d2359
created_at: '2025-12-11T03:48:06.079Z'
updated_at: '2025-12-11T03:48:06.079Z'
verified: false
validated: true
submitted: true
---
# git-clone-public-repo

## Command

```bash
git clone https://github.com/example-repo.git
```

## Description

Clones a public git repository to the local machine for inspection, useful in reconnaissance for finding leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/example-repo.git` | URL of the git repository | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/example-repo.git
```

### Advanced Usage

```bash
git clone --depth 1 https://github.com/example-repo.git
```

## Expected Output

Successful clone creates a local directory with the repository contents.

## Related

- #git
- [[procedures/Discover-Leaked-Credentials-in-Git-Repository]]
