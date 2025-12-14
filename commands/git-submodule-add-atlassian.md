---
data: >-
  git submodule add https://bitbucket.org/atlassian/atlasboard-atlassian-package
  packages/atlassian
tags:
  - git
  - submodule
type: command
output: Clones the repository and registers it as a submodule
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.337Z'
id: c1abe4b1-735f-4793-a4f0-1dfccd532440
verified: false
validated: true
submitted: true
---
# git-submodule-add-atlassian

## Command

```bash
git submodule add https://bitbucket.org/atlassian/atlasboard-atlassian-package packages/atlassian
```

## Description

Adds the atlasboard-atlassian-package repository as a Git submodule in the 'packages/atlassian' directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `submodule add` | Git subcommand for adding submodules | Yes |
| `https://bitbucket.org/atlassian/atlasboard-atlassian-package` | Remote repository URL | Yes |
| `packages/atlassian` | Local path for the submodule | Yes |

## Examples

### Basic Usage

```bash
git submodule add https://bitbucket.org/atlassian/atlasboard-atlassian-package packages/atlassian
```

### Advanced Usage

```bash
git submodule add -b branch https://repo packages/path
```

## Expected Output

Cloning progress and 'Submodule 'packages/atlassian' added' confirmation.

## Related

- [[commands/git-init]]
- [[procedures/Integrate-Atlassian-Package]]
