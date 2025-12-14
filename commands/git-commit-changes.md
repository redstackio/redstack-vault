---
id: cmd-005
data: git commit -m "This message is super important"
tags:
  - git
  - commit
type: command
output: |-
  [master (root-commit) abc1234] This message is super important
   1 file changed, 1 insertion(+)
   create mode 100644 index.html
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.725Z'
verified: false
validated: true
submitted: true
---
# git-commit-changes

## Command

```bash
git commit -m "This message is super important"
```

## Description

Commits the staged malicious HTML file to the local Git history of the wiki repository with a commit message.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m | Inline commit message flag | Yes |
| "This message is super important" | Descriptive message | Yes |

## Examples

### Basic Usage

```bash
git commit -m "Add wiki page"
```

### Advanced Usage

```bash
git commit -m "Update index with content" --author="Attacker <fake@evil.com>"
```

## Expected Output

Commit hash generated; output shows files changed and insertion stats.

## Related

- [[Related Procedure: Upload-Malicious-HTML-to-GitLab-Wiki]]
