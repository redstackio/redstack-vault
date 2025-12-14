---
id: cmd-006
data: git push
tags:
  - git
  - push
  - deploy
type: command
output: |-
  To git@gitlab.com:dummy/test-wiki.git
   * [new branch]      master -> master
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.722Z'
verified: false
validated: true
submitted: true
---
# git-push-to-wiki

## Command

```bash
git push
```

## Description

Pushes the committed malicious HTML to the remote GitLab wiki repository, deploying the XSS payload publicly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (default) | Pushes to upstream branch (master) | N/A |

## Examples

### Basic Usage

```bash
git push
```

### Advanced Usage

```bash
git push origin master
```

## Expected Output

Changes uploaded; output confirms branch push to remote URL.

## Related

- [[Related Procedure: Upload-Malicious-HTML-to-GitLab-Wiki]]
