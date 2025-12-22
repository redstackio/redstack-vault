---
id: cmd-git-commit-wiki
data: git commit -m 'Add exploit wiki page'
tags:
  - git
  - commit
type: command
output: Commit hash and summary
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.121Z'
verified: false
validated: true
submitted: true
---
# git-commit-wiki

## Command

```bash
git commit -m 'Add exploit wiki page'
```

## Description

Commits the staged wiki payload file with a descriptive message.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Commit message flag | Yes |
| `'Add exploit wiki page'` | Message text | Yes |

## Examples

### Basic Usage

```bash
git commit -m 'Add exploit wiki page'
```

### Advanced Usage

```bash
git commit -m 'Update wiki' -a
```

## Expected Output

'[master abc1234] Add exploit wiki page
 1 file changed, 10 insertions(+)'

## Related

- [[commands/git-push]]
- [[procedures/Deploy-Wiki-Payload-via-Git]]
