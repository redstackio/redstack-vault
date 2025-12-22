---
data: 'sudo chown git:git /tmp/ggg'
tags:
  - ownership-change
type: command
executor: bash
platforms:
  - Linux
id: 4689eb1a-a69a-4b48-b009-3a9da6b8de88
created_at: '2025-12-11T03:47:39.416Z'
updated_at: '2025-12-11T03:47:39.416Z'
verified: false
validated: true
submitted: true
---
# sudo-chown-git

## Command

```bash
sudo chown git:git /tmp/ggg
```

## Description

Changes file ownership to git user and group for GitLab compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git:git` | User and group | Yes |
| `/tmp/ggg` | Target file | Yes |

## Examples

### Basic Usage

```bash
sudo chown git:git /tmp/ggg
```

## Expected Output

No output; ownership changed.

## Related
- [[procedures/Bypass-Package-Upload-Validation-for-File-Read]]
