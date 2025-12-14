---
id: cmd-002
data: cd test-wiki
tags:
  - shell
  - navigation
type: command
output: Current directory changed to /path/to/test-wiki
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.758Z'
verified: false
validated: true
submitted: true
---
# cd-to-wiki-directory

## Command

```bash
cd test-wiki
```

## Description

Changes the current working directory to the cloned GitLab wiki repository, preparing for file creation and Git operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| test-wiki | Name of the cloned directory | Yes |

## Examples

### Basic Usage

```bash
cd test-wiki
```

### Advanced Usage

```bash
cd /full/path/to/test-wiki
```

## Expected Output

Shell prompt updates to reflect the new directory; pwd confirms location.

## Related

- [[Related Procedure: Clone-and-Prepare-GitLab-Wiki-Repository]]
