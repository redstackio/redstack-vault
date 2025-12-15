---
id: cmd-git-clone-001
data: 'git clone https://github.com/target/repo.git'
tags:
  - git
  - clone
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.877Z'
verified: false
validated: true
submitted: true
---
# git-clone

## Command

```bash
git clone https://github.com/target/repo.git
```

## Description

Clones a public GitHub repository to a local directory, allowing access to all files and commit history for secret scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/target/repo.git` | URL of the repository to clone | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/mozilla/example-repo.git
```

### Advanced Usage

```bash
git clone --depth 1 https://github.com/target/repo.git  # Shallow clone for recent history only
```

## Expected Output

Cloning into 'repo'...\nremote: Enumerating objects: 100, done.\n... (progress indicators)\nResolving deltas: 100% (50/50), done.

## Related

- [[commands/trufflehog-scan]]
- [[procedures/Discover-Leaked-API-Tokens-in-Public-GitHub-Repositories]]
