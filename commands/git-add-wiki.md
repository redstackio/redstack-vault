---
id: cmd-git-add-wiki
data: git add hello.wiki
tags:
  - git
  - stage
type: command
output: Staging output
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.123Z'
verified: false
validated: true
submitted: true
---
# git-add-wiki

## Command

```bash
git add hello.wiki
```

## Description

Stages the malicious wiki file for commit in the local wiki repository.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `hello.wiki` | Payload file name | Yes |

## Examples

### Basic Usage

```bash
git add hello.wiki
```

### Advanced Usage

```bash
git add .
```

## Expected Output

'new file:   hello.wiki' in status.

## Related

- [[commands/git-commit-wiki]]
- [[procedures/Deploy-Wiki-Payload-via-Git]]
