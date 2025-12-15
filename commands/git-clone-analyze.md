---
id: cmd-git-clone-927413
data: 'git clone https://github.com/zomato/repo.git'
tags:
  - git
type: command
output: |
  Cloning into 'repo'...
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.623Z'
verified: false
validated: true
submitted: true
---
# git-clone-analyze

## Command

```bash
git clone https://github.com/zomato/repo.git
```

## Description

Clones a GitHub repo for analysis of potential vulnerabilities in Zomato code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/zomato/repo.git` | Repo URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/user/repo.git
```

### Advanced Usage

```bash
git clone --depth 1 url
```

## Expected Output

Repo downloaded; ready for review.

## Related

- [[Related Procedure: GitHub-Repository-Exploration-for-Vulnerabilities]]
