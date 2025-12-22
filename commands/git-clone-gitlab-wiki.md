---
id: cmd-001
data: git clone git@gitlab.com/dummy/test-wiki.git
tags:
  - git
  - clone
  - gitlab
type: command
output: |-
  Cloning into 'test-wiki'...
  remote: Enumerating objects: 3, done.
  remote: Counting objects: 100% (3/3), done.
  remote: Compressing objects: 100% (2/2), done.
  remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
  Receiving objects: 100% (3/3), done.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.766Z'
verified: false
validated: true
submitted: true
---
# git-clone-gitlab-wiki

## Command

```bash
git clone git@gitlab.com/dummy/test-wiki.git
```

## Description

Clones the GitLab wiki repository associated with a public project, creating a local copy for uploading malicious content like XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| git@gitlab.com/dummy/test-wiki.git | SSH URL of the target wiki repository | Yes |

## Examples

### Basic Usage

```bash
git clone git@gitlab.com/dummy/test-wiki.git
```

### Advanced Usage

```bash
git clone -b master git@gitlab.com/dummy/test-wiki.git my-wiki
```

## Expected Output

Local directory 'test-wiki' created with Git repo initialized; output confirms cloning success and object receipt.

## Related

- [[Related Procedure: Clone-and-Prepare-GitLab-Wiki-Repository]]
